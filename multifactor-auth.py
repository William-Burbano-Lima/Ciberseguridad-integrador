import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import pyotp
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['JWT_SECRET_KEY'] = os.urandom(24)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    totp_secret = db.Column(db.String(32))
    mfa_habilitado = db.Column(db.Boolean, default=False)

def generar_totp_secret():
    return pyotp.random_base32()

def enviar_codigo_2fa(email, codigo):
    remitente = "tu_email@ejemplo.com"
    password = "tu_contraseña"
    
    mensaje = MIMEText(f'Tu código de verificación es: {codigo}')
    mensaje['Subject'] = "Código de Autenticación de Dos Factores"
    mensaje['From'] = remitente
    mensaje['To'] = email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(remitente, password)
        servidor.sendmail(remitente, email, mensaje.as_string())

@app.route('/registro', methods=['POST'])
def registro():
    datos = request.json
    username = datos.get('username')
    email = datos.get('email')
    password = datos.get('password')

    if Usuario.query.filter_by(username=username).first():
        return jsonify({"error": "Usuario ya existe"}), 400

    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    totp_secret = generar_totp_secret()

    nuevo_usuario = Usuario(
        username=username, 
        email=email, 
        password_hash=password_hash,
        totp_secret=totp_secret,
        mfa_habilitado=False
    )
    
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({
        "mensaje": "Usuario registrado",
        "totp_secret": totp_secret
    }), 201

@app.route('/habilitar-2fa', methods=['POST'])
@jwt_required()
def habilitar_2fa():
    usuario = Usuario.query.filter_by(username=request.json.get('username')).first()
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    usuario.mfa_habilitado = True
    db.session.commit()

    return jsonify({"mensaje": "2FA habilitado"})

@app.route('/login', methods=['POST'])
def login():
    datos = request.json
    username = datos.get('username')
    password = datos.get('password')
    codigo_2fa = datos.get('codigo_2fa')

    usuario = Usuario.query.filter_by(username=username).first()
    if not usuario or not bcrypt.check_password_hash(usuario.password_hash, password):
        return jsonify({"error": "Credenciales inválidas"}), 401

    if usuario.mfa_habilitado:
        totp = pyotp.TOTP(usuario.totp_secret)
        if not totp.verify(codigo_2fa):
            return jsonify({"error": "Código 2FA inválido"}), 401

    token_acceso = create_access_token(identity=username)
    return jsonify({"token": token_acceso})

@app.route('/enviar-codigo-2fa', methods=['POST'])
def enviar_codigo():
    email = request.json.get('email')
    usuario = Usuario.query.filter_by(email=email).first()
    
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    totp = pyotp.TOTP(usuario.totp_secret)
    codigo = totp.now()
    
    enviar_codigo_2fa(email, codigo)
    return jsonify({"mensaje": "Código enviado"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# Dependencias requeridas:
# pip install flask flask-sqlalchemy flask-bcrypt flask-jwt-extended pyotp
