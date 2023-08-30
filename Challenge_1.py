import sys
import typer
from rich.console import Console
from rich.prompt import Prompt

console = Console(color_system="windows")
"""
    Reto #1
    ¿Es un anagrama?
    Fecha publicación enunciado: 03/01/22
    Fecha publicación resolución: 10/01/22
    Dificultad: MEDIA

    Enunciado: Escribe una función que reciba dos palabras (String) y
    retorne verdadero o falso (Bool) según sean o no anagramas.
    Un Anagrama consiste en formar una palabra reordenando TODAS las letras de
    otra palabra inicial.
    NO hace falta comprobar que ambas palabras existan.
    Dos palabras exactamente iguales no son anagrama.
"""


class Anagrama:
    """
        Función 1 para introducir dos palabras y verificar si es un anagrama
        (return True) o no (return False)
    """
    def __init__(self, string_1, string_2):
        self.string_1 = string_1
        self.string_2 = string_2

    def option_1(self):
        result_1 = ''.join(sorted(self.string_1, reverse=True))
        result_2 = ''.join(sorted(self.string_2, reverse=True))

        if self.string_2 == result_1 or self.string_1 == result_2:
            console.print(
                f"[green]El resultado es VERDADERO.[/green] La palabra [dark_green bold]{self.string_1}[/dark_green bold] es un anagrama de [dark_green bold]{self.string_2}[/dark_green bold].")
        else:
            console.print(
                f"[red]El resultado es FALSO.[/red] La palabra [dark_red bold]{self.string_1}[/dark_red bold] no es un anagrama de [dark_red bold]{self.string_2}[/dark_red bold].")

    # Función 2 para introducir dos palabras y verificar si es un anagrama
    # (return True) o no (return False)
    def option_2(self):
        if sorted(self.string_1) == sorted(self.string_2):
            console.print(
                f"[green]El resultado es VERDADERO.[/green] La palabra [dark_green bold]{self.string_1}[/dark_green bold] es un anagrama de [dark_green bold]{self.string_2}[/dark_green bold].")
        else:
            console.print(
                f"[red]El resultado es FALSO.[/red] La palabra [dark_red bold]{self.string_1}[/dark_red bold] no es un anagrama de [dark_red bold]{self.string_2}[/dark_red bold].")


def main():
    option = Prompt.ask("Introduzca qué función ejecutar? y presione ENTER", choices=["1", "2", "exit"])

    if option == "exit":
        sys.exit("Proceso finalizado!")

    input_1 = Prompt.ask("Introduzca la primera palabra y presione ENTER").lower()
    input_2 = Prompt.ask("Introduzca la segunda palabra y presione ENTER").lower()

    if option == "1":
        option = Anagrama(input_1, input_2)
        option.option_1()
        main()

    else:
        option = Anagrama(input_1, input_2)
        option.option_2()
        main()


if __name__ == '__main__':
    typer.run(main)
