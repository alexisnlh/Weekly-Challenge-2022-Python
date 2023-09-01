import sys
import re
import typer
from rich.console import Console
from rich.prompt import Prompt

console = Console(color_system="windows")
# Reto #16
# En mayúscula
# Fecha publicación enunciado: 18/04/22
# Fecha publicación resolución: 25/04/22
# Dificultad: FÁCIL

# Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.
# - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.


class Capitalize:
    """
        Modifica el texto ingresado
    """

    pattern = "[^A-zÀ-ú]"

    def __init__(self, input_string):
        self.input_string = input_string

    def capitalize_process(self):
        flag_first = True
        capitalizedText = list()

        for letter in self.input_string:
            # Comprueba si letter es una letra o símbolo/espacio
            check = re.search(self.__class__.pattern, letter, re.IGNORECASE)
            if not check:
                # Si flag_first = True, cambia a mayúscula letter seleccionada y la almacena en la variable letter_modf, si no lo almacena en la variable letter_modf sin modificar
                if flag_first:
                    letter_modf = letter.upper()
                    flag_first = False
                else:
                    letter_modf = letter
            else:
                letter_modf = letter
                flag_first = True
            capitalizedText.append(letter_modf)

        console.print(f"El texto ingresado modificado es: [bold]{''.join(capitalizedText)}[/bold]")


def main():
    input_string = Prompt.ask("Introduzca el texto a procesar, y presione ENTER (q --> Exit)").rstrip().lstrip()
    if input_string == "q":
        sys.exit("Proceso finalizado!")

    # Modifica el texto ingresado
    Capitalize(input_string).capitalize_process()


if __name__ == '__main__':
    typer.run(main)
