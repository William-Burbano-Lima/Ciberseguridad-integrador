import itertools

password = "abc123"

for attempt in itertools.product("abcdefghijklmnopqrstuvwxyz0123456789", repeat=6):
    attempt = ''.join(attempt)
    if attempt == password:
        print(f"Contraseña encontrada: {attempt}")
        break