import sys
import typer
from rich.console import Console
from rich.prompt import Prompt

console = Console(color_system="windows")
# Reto #11
# Eliminando caracteres
# Fecha publicación enunciado: 14/03/22
# Fecha publicación resolución: 21/03/22
# Dificultad: FÁCIL

# Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.


class DeleteCharacters:
    """
        Verificar las dos cadenas de caracteres ingresadas
    """
    def __init__(self, input_string_1, input_string_2):
        self.input_string_1 = input_string_1
        self.input_string_2 = input_string_2

    def print_non_common(self):
        list_1 = list()
        list_1[:0] = self.input_string_1
        list_2 = list()
        list_2[:0] = self.input_string_2
        out1 = list()
        out2 = list()

        for letter in list_1:
            if letter not in self.input_string_2:
                out1.append(letter)
        out1 = "".join(out1)

        for letter in list_2:
            if letter not in self.input_string_1:
                out2.append(letter)
        out2 = "".join(out2)

        console.print(
            f"Los caracteres presentes en la primera cadena pero no en la segunda cadena son (utilizando función [bold]print_non_common[/bold]): [green]{out1}[/green]\nLos caracteres presentes en la segunda cadena pero no en la primera cadena son (utilizando función [bold]print_non_common[/bold]): [blue]{out2}[/blue]")

    def print_non_common_with_filter(self):
        list_1 = list()
        list_1[:0] = self.input_string_1
        list_2 = list()
        list_2[:0] = self.input_string_2

        out1 = [letter for letter in list_1 if letter not in self.input_string_2]
        out1 = "".join(out1)
        out2 = [letter for letter in list_2 if letter not in self.input_string_1]
        out2 = "".join(out2)

        console.print(
            f"\nLos caracteres presentes en la primera cadena pero no en la segunda cadena son (utilizando función [bold]print_non_common_with_filter[/bold]): [green]{out1}[/green]\nLos caracteres presentes en la segunda cadena pero no en la primera cadena son (utilizando función [bold]print_non_common_with_filter[/bold]): [blue]{out2}[/blue]")


def main(input_string_1=None):
    if input_string_1 is None:
        input_string_1 = Prompt.ask("Introduzca la primera cadena de caracteres y presione ENTER (q --> Exit)").lower()
        if input_string_1 == "":
            console.print(
                f"[red]No se introdujo la primera cadena de caracteres válida![/red]")
            main()
            sys.exit("Proceso finalizado!")

        elif input_string_1 == "q":
            sys.exit("Proceso finalizado!")

    input_string_2 = Prompt.ask("Introduzca la segunda cadena de caracteres y presione ENTER (q --> Exit)").lower()
    if input_string_2 == "":
        console.print(
            f"[red]No se introdujo la segunda cadena de caracteres válida![/red]")
        main(input_string_1=input_string_1)
        sys.exit("Proceso finalizado!")

    elif input_string_2 == "q":
        sys.exit("Proceso finalizado!")

    # Verificar las dos cadenas de caracteres ingresadas
    DeleteCharacters(input_string_1, input_string_2).print_non_common()

    # Otra solución utilizando funciones de orden superior
    DeleteCharacters(input_string_1, input_string_2).print_non_common_with_filter()


if __name__ == '__main__':
    typer.run(main)
