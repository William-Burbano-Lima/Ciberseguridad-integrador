from cryptography.fernet import Fernet

# generar una clave secreta 

def generate_clave():
    return Fernet.generate_key()

# Guardar la clave en un archivo seguro

def guardar_clave(clave):
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)
        
def cifrar_contraseña(clave, contraseña):
    fernet = Fernet(clave)
    contraseña_cifrada = fernet.encrypt(contraseña.encode())
    return contraseña_cifrada

def descifrar_contraseña(clave, contraseña_cifrada):
    fernet = Fernet(clave)
    contraseña_descifrada = fernet.decrypt(contraseña_cifrada.decode())
    return contraseña_descifrada
    
# Guardar contraseñas cifradas

def guardar_contraseñas_en_archivo(contrasena_cifrada):
    with open("contraseñas.txt", "ab") as archivo:
        archivo.write(contraseña_cifrada + b"\n")
        
# Leer las contraseñas cifradas desde el archivo

def leer_contraseñas_desde_archivo():
    contraseñas = []
    with open("contraseñas.txt", "rb") as archivo:
        for linea in archivo.readlines():
            contraseñas.append(linea.strip())
    return contraseñas
    
    