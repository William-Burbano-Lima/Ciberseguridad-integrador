
import sqlite3

# Conectar a base de datos existente

conn = sqlite3.connect("mi_primera_DB")
cursor = conn.cursor()

# Crear una tabla
cursor.execute("""
               
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                edad INTEGER,
                email TEXT
            )
""")

# Insertar datos

cursor.execute("""
            INSERT INTO usuarios (nombre, edad, email)
            VALUES ("Juan", 30, "juan@ejemplo.com")
""")

# Guardar cambios
conn.commit()

# Consultar datos

cursor.execute("SELECT * FROM usuarios")
filas = cursor.fetchall()
for fila in filas:
    print(fila)
    
    
# Cerrar la conexion
conn.close()
