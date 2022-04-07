# Reto #1
# ¿Es un anagrama?
# Fecha publicación enunciado: 03/01/22
# Fecha publicación resolución: 10/01/22
# Dificultad: MEDIA

# Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.


# Función 1 para introducir dos palabras y verificar si es un anagrama (return True) o no (return False)
def anagrama_1():
    try:
        input_1 = input("Introduzca la primera palabra y presione ENTER: \n").lower()
        input_2 = input("Introduzca la segunda palabra y presione ENTER: \n").lower()
        result_1 = ''.join(sorted(input_1, reverse=True))
        result_2 = ''.join(sorted(input_2, reverse=True))

        if input_2 == result_1 or input_1 == result_2:
            print(" El resultado es VERDADERO. La palabra {0} es un anagrama de {1}.".format(input_1, input_2))
        else:
            print(" El resultado es FALSO. La palabra {0} no es un anagrama de {1}.".format(input_1, input_2))
    except Exception as error:
        print("Exception: {}".format(error))


# Función 2 para introducir dos palabras y verificar si es un anagrama (return True) o no (return False)
def anagrama_2():
    try:
        input_1 = input("Introduzca la primera palabra y presione ENTER: \n").lower()
        input_2 = input("Introduzca la segunda palabra y presione ENTER: \n").lower()

        if sorted(input_1) == sorted(input_2):
            print(" El resultado es VERDADERO. La palabra {0} es un anagrama de {1}.".format(input_1, input_2))
        else:
            print(" El resultado es FALSO. La palabra {0} no es un anagrama de {1}.".format(input_1, input_2))
    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    while True:
        try:
            opcion = int(input("Introduzca qué función ejecutar (1 o 2)? y presione ENTER: \n"))
            if opcion == 1:
                # Función 1 para introducir dos palabras y verificar si es un anagrama (return True) o no (return False)
                anagrama_1()
                break
            elif opcion == 2:
                # Función 2 para introducir dos palabras y verificar si es un anagrama (return True) o no (return False)
                anagrama_2()
                break
            else:
                opcion = input("No seleccionaste una opción válida. Desea continuar? (Y/N)\n").lower()
                if opcion == "n" or "no" in opcion:
                    break
        except:
            opcion = input("No seleccionaste una opción válida. Desea continuar? (Y/N)\n").lower()
            if opcion == "n" or "no" in opcion:
                break