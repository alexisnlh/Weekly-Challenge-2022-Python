import sys
import typer
from rich.console import Console
from rich.prompt import Prompt, IntPrompt, FloatPrompt

console = Console(color_system="windows")
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


class RecursiveReverse:
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
            newReversedText = RecursiveReverse(self.input_string,
                                               index=newIndex,
                                               reversedText=newReversedText).option_2()
        return newReversedText


def main():
    input_string = Prompt.ask("Introduzca la cadena de texto que desea invertir y presione ENTER").rstrip().lstrip()

    if input_string == "":
        main()
        sys.exit("Proceso finalizado!")

    option = IntPrompt.ask(
        "Introduzca la opción que desea que realice el proceso y presione ENTER: \n(1 --> Por bucle, 2 --> Por función recursiva, 3 --> Exit)",
        choices=["1", "2", "3"], show_choices=False)

    if option == 1:
        # Función 1 para introducir la cadena de texto y devolver su inversa por bucle
        console.print(
            f"La cadena de texto inversa de la función 1 es: [bright_white on bright_red bold]{RecursiveReverse(input_string).option_1()}[/bright_white on bright_red bold]")

    elif option == 2:
        # Función 2 para introducir la cadena de texto y devolver su inversa por función recursiva
        console.print(
            f"La cadena de texto inversa de la función 2 es: [bright_white on blue1 bold]{RecursiveReverse(input_string).option_2()}[/bright_white on blue1 bold]")

    else:
        sys.exit("Proceso finalizado!")


if __name__ == '__main__':
    typer.run(main)
