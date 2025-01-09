def cifrar_mensaje(mensaje, clave):
    mensaje_cifrado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            offset = 65 if caracter.isupper() else 97
            mensaje_cifrado += chr((ord(caracter) +
                                   clave - offset) % 26 + offset)
        else:
            mensaje_cifrado += caracter
    return mensaje_cifrado


def main():
    print("Programa de Cifrado")
    mensaje = input("Ingrese el mensaje a cifrar: ")
    clave = int(input("Ingrese la clave de cifrado (número entero): "))
    mensaje_cifrado = cifrar_mensaje(mensaje, clave)
    print(f"Mensaje cifrado: {mensaje_cifrado}")


if __name__ == "__main__":
    main()
