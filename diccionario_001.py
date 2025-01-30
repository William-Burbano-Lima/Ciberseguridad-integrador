# Simulación de ataque de diccionario
password = "password123"
dictionary = ["123456", "password", "admin", "qwerty", "password123", "abc123"]

for attempt in dictionary:
    print(f"Probando: {attempt}")
    if attempt == password:
        print(f"Contraseña encontrada: {attempt}")
        break