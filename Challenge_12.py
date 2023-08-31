import sys
import typer
from rich.console import Console
from rich.prompt import Prompt

console = Console(color_system="windows")
# Reto #12
# ¿Es un palíndromo?
# Fecha publicación enunciado: 21/03/22
# Fecha publicación resolución: 28/03/22
# Dificultad: MEDIA

# Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
# NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.


class IsPalindrome:
    """
       Verificar si el texto ingresado es palíndromo o no
    """

    # Se puede agregar más símbolos según se necesite
    chars_replace = {
        " ": "",
        "\\": "",
        "`": "",
        "*": "",
        "_": "",
        "{": "",
        "}": "",
        "[": "",
        "]": "",
        "(": "",
        ")": "",
        ">": "",
        "#": "",
        "+": "",
        "-": "",
        ".": "",
        ",": "",
        "¡": "",
        "!": "",
        "¿": "",
        "?": "",
        "$": "",
        "&": "",
        "%": "",
        "@": "",
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u"
    }

    def __init__(self, input_string):
        self.input_string = input_string

    def check_process(self):
        for key, value in self.__class__.chars_replace.items():
            self.input_string = self.input_string.replace(key, value)

        if self.input_string == self.input_string[::-1]:
            console.print(f"[green]El texto introducido ({self.input_string}) es palíndromo.[/green]")
        else:
            console.print(f"[red]El texto introducido ({self.input_string}) NO es palíndromo.[/red]")


def main():
    input_string = Prompt.ask("Introduzca el texto a verificar si es palíndromo o no, y presione ENTER (q --> Exit)").lower()

    if input_string == "":
        console.print("[red]No se introdujo un texto válido![/red]")
        main()
        sys.exit("Proceso finalizado!")

    elif input_string == "q":
        sys.exit("Proceso finalizado!")

    IsPalindrome(input_string).check_process()


if __name__ == '__main__':
    typer.run(main)
