"""
    Reto #6
    Invirtiendo cadenas
    Fecha publicación enunciado: 07/02/22
    Fecha publicación resolución: 14/02/22
    Dificultad: FÁCIL

    Enunciado: Crea un programa que invierta el orden de una cadena de texto
    sin usar funciones propias del lenguaje que lo hagan de forma automática.
        - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""


class recursiveReverse:
    """
        Obtener la cadena de texto inversa a la introducida. Option 1 por
        bucle, option 2 por función recursiva
    """
    def __init__(self, input_string, index=0, reversedText=""):
        self.input_string = input_string
        self.index = index
        self.reversedText = reversedText

    def option_1(self):
        # Obtiene el tamaño de la cadena de texto - 1
        textCount = len(self.input_string) - 1

        # Almacena en una lista cada letra de la cadena de texto
        textArray = list(self.input_string)
        reversedText = str()

        for index in range(0, textCount + 1):
            """
                Contruye la nueva cadena de texto invertida obteniendo la letra
                por su posición en la lista inicial (textArray)
            """
            reversedText += textArray[textCount - index]
        return reversedText

    def option_2(self):
        # Obtiene el tamaño de la cadena de texto - 1
        textCount = len(self.input_string) - 1

        # Almacena en una lista cada letra de la cadena de texto
        textArray = list(self.input_string)

        # Almacena la nueva cadena de texto invertida por cada recursividad
        newReversedText = self.reversedText

        """
            Se agrega a la nueva cadena de texto invertida la letra ubicada en
            la posición que se pasa por la variable index en cada recursividad
            de la lista inicial (textArray)
        """
        newReversedText += textArray[textCount - self.index]

        """
            Se verifica que la cuenta (index) sea menor que el tamaño de la
            cadena de texto inicial - 1
        """
        if self.index < textCount:
            # Se aumenta la cuenta index
            newIndex = self.index + 1

            # Se llama a la función para ir construyendo la cadena de texto inversa
            newReversedText = recursiveReverse(self.input_string,
                                               index=newIndex,
                                               reversedText=newReversedText).option_2()
        return newReversedText


# # Función 1 para introducir la cadena de texto y devolver su inversa. Con un bucle
# def reverse(input_string):
#     try:
#         # Obtiene el tamaño de la cadena de texto - 1
#         textCount = len(input_string) - 1
#         # Almacena en una lista cada letra de la cadena de texto
#         textArray = list(input_string)
#         reversedText = str()
#
#         for index in range(0, textCount + 1):
#             # Contruye la nueva cadena de texto invertida obteniendo la letra por su posición en la lista inicial (textArray)
#             reversedText += textArray[textCount - index]
#
#         return reversedText
#     except Exception as error:
#         print("Exception: {}".format(error))


# Funcion 2 para introducir la cadena de texto y devolver su inversa. Sin un bucle, mediante una función recursiva
# def recursiveReverse(input_string, index=0, reversedText=""):
#     try:
#         # Obtiene el tamaño de la cadena de texto - 1
#         textCount = len(input_string) - 1
#         # Almacena en una lista cada letra de la cadena de texto
#         textArray = list(input_string)
#         # Almacena la nueva cadena de texto invertida por cada recursividad
#         newReversedText = reversedText
#         # Se agrega a la nueva cadena de texto invertida la letra ubicada en la posición que se pasa por la variable index en cada recursividad de la lista inicial (textArray)
#         newReversedText += textArray[textCount - index]
#
#         # Se verifica que la cuenta (index) sea menor que el tamaño de la cadena de texto inicial - 1
#         if index < textCount:
#             # Se aumenta la cuenta index
#             newIndex = index + 1
#             # Se llama a la función para ir construyendo la cadena de texto inversa
#             newReversedText = recursiveReverse(input_string, index=newIndex, reversedText=newReversedText)
#
#         return newReversedText
#     except Exception as error:
#         print("Exception: {}".format(error))


if __name__ == '__main__':
    flag_continue = True
    while flag_continue:
        try:
            input_string = input(
                "Introduzca la cadena de texto que desea invertir y presione ENTER: \n").rstrip().lstrip()
            input_option = int(input(
                "Introduzca el número de la función que desea que realice el proceso y presione ENTER:\n1.- Por bucle\n2.- Por función recursiva\n").rstrip().lstrip())

            if input_string != "" and input_option in [1, 2]:
                if input_option == 1:
                    # Función 1 para introducir la cadena de texto y devolver su inversa por bucle
                    print(f"La cadena de texto inversa de la función 1 es: {recursiveReverse(input_string).option_1()}")
                else:
                    # Función 2 para introducir la cadena de texto y devolver su inversa por función recursiva
                    print(f"La cadena de texto inversa de la función 2 es: {recursiveReverse(input_string).option_2()}")
                break
            else:
                while True:
                    opcion = input("No se introdujo una cadena de texto válida o número de función correcta. Desea continuar? (Y/N)\n").lower()
                    if opcion == "y" or "yes" in opcion:
                        break
                    elif opcion == "n" or "no" in opcion:
                        flag_continue = False
                        break
        except (ValueError, Exception):
            while True:
                opcion = input("No se introdujo una cadena de texto válida o número de función correcta. Desea continuar? (Y/N)\n").lower()
                if opcion == "y" or "yes" in opcion:
                    break
                elif opcion == "n" or "no" in opcion:
                    flag_continue = False
                    break