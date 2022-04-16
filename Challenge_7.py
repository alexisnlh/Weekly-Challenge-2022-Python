# Reto #7
# Contando palabras
# Fecha publicación enunciado: 14/02/22
# Fecha publicación resolución: 21/02/22
# Dificultad: MEDIA

# Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
#  - Los signos de puntuación no forman parte de la palabra.
#  - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.


# Función para contar las veces que se repite cada palabra
def countWords(input_string):
    try:
        # Los caracteres que no se cuentan como palabras
        quitar = ",;:.\n!\"'()"
        for caracter in quitar:
            input_string = input_string.replace(caracter, "")

        mutableString = input_string.lower().split(" ")
        wordsDict = dict()

        for word in mutableString:
            if word in wordsDict:
                wordsDict[word] += 1
            else:
                wordsDict[word] = 1

        for word in wordsDict:
            print("{0} se ha repetido {1} veces".format(word, wordsDict[word]))
    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    while True:
        try:
            input_string = input("Introduzca la cadena de texto que desea invertir y presione ENTER: \n")
            input_string = input_string.rstrip().lstrip()
            if input_string != "":
                # Función para contar las veces que se repite cada palabra
                countWords(input_string)
                break
            else:
                opcion = input("No se introdujo una cadena de texto válida. Desea continuar? (Y/N)\n").lower()
                if opcion == "n" or "no" in opcion:
                    break
        except:
            opcion = input("No se introdujo una cadena de texto válida. Desea continuar? (Y/N)\n").lower()
            if opcion == "n" or "no" in opcion:
                break