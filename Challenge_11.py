# Reto #11
# Eliminando caracteres
# Fecha publicación enunciado: 14/03/22
# Fecha publicación resolución: 21/03/22
# Dificultad: FÁCIL

# Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.


# Función para verificar las dos cadenas de caracteres ingresadas
def printNonCommon(str1, str2):
    list_1 = list()
    list_1[:0] = str1
    list_2 = list()
    list_2[:0] = str2
    out1 = list()
    out2 = list()

    for letter in list_1:
        if letter not in str2:
            out1.append(letter)
    out1 = "".join(out1)

    for letter in list_2:
        if letter not in str1:
            out2.append(letter)
    out2 = "".join(out2)

    return out1, out2


# Otra solución utilizando funciones de orden superior
def printNonCommonWithFilter(str1, str2):
    list_1 = list()
    list_1[:0] = str1
    list_2 = list()
    list_2[:0] = str2

    out1 = [letter for letter in list_1 if letter not in str2]
    out1 = "".join(out1)
    out2 = [letter for letter in list_2 if letter not in str1]
    out2 = "".join(out2)

    return out1, out2


if __name__ == '__main__':
    while True:
        try:
            str1 = input("Introduzca la primera cadena de caracteres y presione ENTER: \n")
            str2 = input("Introduzca la segunda cadena de caracteres y presione ENTER: \n")
            if str1 != "" and str2 != "":
                # Función para verificar las dos cadenas de caracteres ingresadas
                out1, out2 = printNonCommon(str1.lower(), str2.lower())
                print(f"Los caracteres presentes en la primera cadena pero no en la segunda cadena son (utilizando función printNonCommon): {out1}")
                print(f"Los caracteres presentes en la segunda cadena pero no en la primera cadena son (utilizando función printNonCommon): {out2}")

                # Otra solución utilizando funciones de orden superior
                out1, out2 = printNonCommonWithFilter(str1.lower(), str2.lower())
                print(f"\nLos caracteres presentes en la primera cadena pero no en la segunda cadena son (utilizando función printNonCommonWithFilter): {out1}")
                print(f"Los caracteres presentes en la segunda cadena pero no en la primera cadena son (utilizando función printNonCommonWithFilter): {out2}")
                break
            elif str1 == "":
                opcion = input("No se introdujo la primera cadena de caracteres válida. Desea continuar? (Y/N)\n").lower()
                if opcion == "n" or "no" in opcion:
                    break
            elif str2 == "":
                opcion = input("No se introdujo la segunda cadena de caracteres válida. Desea continuar? (Y/N)\n").lower()
                if opcion == "n" or "no" in opcion:
                    break
        except:
            opcion = input("No se introdujo la cadena de caracteres válida. Desea continuar? (Y/N)\n").lower()
            if opcion == "n" or "no" in opcion:
                break