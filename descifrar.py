def descifrar_mensaje(mensaje_cifrado, clave):
    mensaje_descifrado = ""
    for caracter in mensaje_cifrado:
        if caracter.isalpha():
            offset = 65 if caracter.isupper() else 97
            mensaje_descifrado += chr((ord(caracter) -
                                      clave - offset) % 26 + offset)
        else:
            mensaje_descifrado += caracter
    return mensaje_descifrado


def main():
    print("Programa de Descifrado")
    mensaje_a_descifrar = input("Ingrese el mensaje cifrado: ")
    clave_descifrado = int(input("Ingrese la clave de descifrado: "))
    mensaje_descifrado = descifrar_mensaje(
        mensaje_a_descifrar, clave_descifrado)
    print(f"Mensaje descifrado: {mensaje_descifrado}")


if __name__ == "__main__":
    main()
