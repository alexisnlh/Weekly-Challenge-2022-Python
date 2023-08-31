import sys
import typer
from rich.console import Console
from rich.prompt import Prompt

console = Console(color_system="windows")
# Reto #9
# Código Morse
# Fecha publicación enunciado: 02/03/22
# Fecha publicación resolución: 07/03/22
# Dificultad: MEDIA

# Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.


class DecoderStringMorse:
    """
        Transforma texto natural a código morse y viceversa
    """

    naturalDict = {
        "A": ".—",
        "B": "—...",
        "C": "—.—.",
        "CH": "————",
        "D": "—..",
        "E": ".",
        "F": "..—.",
        "G": "——.",
        "H": "....",
        "I": "..",
        "J": ".———",
        "K": "—.—",
        "L": ".—..",
        "M": "——",
        "N": "—.",
        "Ñ": "——.——",
        "O": "———",
        "P": ".——.",
        "Q": "——.—",
        "R": ".—.",
        "S": "...",
        "T": "—",
        "U": "..—",
        "V": "...—",
        "W": ".——",
        "X": "—..—",
        "Y": "—.——",
        "Z": "——..",
        "0": "—————",
        "1": ".————",
        "2": "..———",
        "3": "...——",
        "4": "....—",
        "5": ".....",
        "6": "—....",
        "7": "——...",
        "8": "———..",
        "9": "————.",
        ".": ".—.—.—",
        ",": "——..——",
        "?": "..——..",
        "\"": ".—..—.",
        "/": "—..—."
    }

    def __init__(self, input_string):
        self.input_string = input_string

    def transform_process(self):
        morseText = str()
        morse = False

        # Verifica si el string ingresado es una cadena de texto o código morse
        if not set(self.input_string) <= {'.', '—', ' '}:
            # Texto natural
            flag = False
            morse = True

            for index, letter in enumerate(self.input_string.upper()):
                if letter in self.__class__.naturalDict.keys() or letter == " ":
                    if letter != " ":
                        if not flag:
                            if letter == "C" and self.input_string.upper()[index + 1] == "H":
                                morseText += self.__class__.naturalDict["CH"] + " "
                                flag = True
                            else:
                                morseText += self.__class__.naturalDict[letter] + " "
                        else:
                            flag = False
                            continue
                    else:
                        morseText += " "
                else:
                    console.print(
                        f"No se pudo transformar la cadena de texto/código morse ingresado por no encontrarse el caracter [red bold]{letter}[/red bold]")
                    return None
        else:
            # Código morse
            self.input_string += " "
            subtext = str()
            index = 0

            for letter in self.input_string:
                # Verifica si hay espacio para transformar la letra del código morse
                if letter != " ":
                    index = 0
                    subtext += letter
                else:
                    index += 1

                    # Verifica si es un final de código morse o es un espacio para agregar al texto final
                    if index == 2:
                        morseText += " "
                    else:
                        morseText += list(self.__class__.naturalDict.keys())[list(self.__class__.naturalDict.values()).index(subtext)]
                        subtext = str()
        if morse:
            console.print(
                f"El código morse de la cadena de texto ingresada es: [green bold]{morseText.rstrip()}[/green bold]")
        else:
            console.print(
                f"La cadena de texto del código morse ingresado es: [blue bold]{morseText.rstrip()}[/blue bold]")


def main():
    input_string = Prompt.ask(
        "Introduzca la cadena de texto/código morse y presione ENTER (q --> Exit)").rstrip().lstrip()

    if input_string == "":
        main()
        sys.exit("Proceso finalizado!")

    elif input_string == "q":
        sys.exit("Proceso finalizado!")

    # Transforma texto natural a código morse y viceversa
    DecoderStringMorse(input_string).transform_process()


if __name__ == '__main__':
    typer.run(main)
