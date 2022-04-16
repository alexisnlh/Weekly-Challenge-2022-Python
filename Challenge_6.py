# Reto #6
# Invirtiendo cadenas
# Fecha publicación enunciado: 07/02/22
# Fecha publicación resolución: 14/02/22
# Dificultad: FÁCIL

# Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"


# Función 1 para introducir la cadena de texto y devolver su inversa. Con un bucle
def reverse(input_string):
    try:
        # Obtiene el tamaño de la cadena de texto - 1
        textCount = len(input_string) - 1
        # Almacena en una lista cada letra de la cadena de texto
        textArray = list(input_string)
        reversedText = str()

        for index in range(0, textCount + 1):
            # Contruye la nueva cadena de texto invertida obteniendo la letra por su posición en la lista inicial (textArray)
            reversedText += textArray[textCount - index]

        return reversedText
    except Exception as error:
        print("Exception: {}".format(error))


# Funcion 2 para introducir la cadena de texto y devolver su inversa. Sin un bucle, mediante una función recursiva
def recursiveReverse(input_string, index=0, reversedText=""):
    try:
        # Obtiene el tamaño de la cadena de texto - 1
        textCount = len(input_string) - 1
        # Almacena en una lista cada letra de la cadena de texto
        textArray = list(input_string)
        # Almacena la nueva cadena de texto invertida por cada recursividad
        newReversedText = reversedText
        # Se agrega a la nueva cadena de texto invertida la letra ubicada en la posición que se pasa por la variable index en cada recursividad de la lista inicial (textArray)
        newReversedText += textArray[textCount - index]

        # Se verifica que la cuenta (index) sea menor que el tamaño de la cadena de texto inicial - 1
        if index < textCount:
            # Se aumenta la cuenta index
            newIndex = index + 1
            # Se llama a la función para ir construyendo la cadena de texto inversa
            newReversedText = recursiveReverse(input_string, index=newIndex, reversedText=newReversedText)

        return newReversedText
    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    while True:
        try:
            input_string = input("Introduzca la cadena de texto que desea invertir y presione ENTER: \n")
            input_string = input_string.rstrip().lstrip()
            if input_string != "":
                # Función 1 para introducir la cadena de texto y devolver su inversa
                reversedText = reverse(input_string)
                print("La cadena de texto inversa de la función 1 es: {}".format(reversedText))

                # Función 2 para introducir la cadena de texto y devolver su inversa
                newReversedText = recursiveReverse(input_string)
                print("La cadena de texto inversa de la función 2 es: {}".format(newReversedText))
                break
            else:
                opcion = input("No se introdujo una cadena de texto válida. Desea continuar? (Y/N)\n").lower()
                if opcion == "n" or "no" in opcion:
                    break
        except:
            opcion = input("No se introdujo una cadena de texto válida. Desea continuar? (Y/N)\n").lower()
            if opcion == "n" or "no" in opcion:
                break