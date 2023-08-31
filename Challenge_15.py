import sys
import datetime
import re
import typer
from rich.console import Console
from rich.prompt import Prompt

console = Console(color_system="windows")
# Reto #15
# ¿Cuántos días?
# Fecha publicación enunciado: 11/04/22
# Fecha publicación resolución: 18/04/22
# Dificultad: DIFÍCIL

# Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
# - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# - La función recibirá dos String y retornará un Int.
# - La diferencia en días será absoluta (no importa el orden de las fechas).
# - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.


class DaysBetween:
    """
        Obtener la diferencia de días que hay entre dos fechas
    """
    pattern_date = r'([0-9]){2}[\/]([0-9]){2}[\/]([0-9]){4}'

    def __init__(self, input_string_1, input_string_2):
        self.input_string_1 = input_string_1
        self.input_string_2 = input_string_2

    def check_date(self):
        try:
            # Comprueba que el formato es el correcto para ambas cadenas de texto ingresadas, si no, se informa cual no es correcta
            check_1 = re.search(self.__class__.pattern_date, self.input_string_1, re.IGNORECASE)
            check_2 = re.search(self.__class__.pattern_date, self.input_string_2, re.IGNORECASE)

            if check_1 and check_2:
                # Obtiene el campo fecha, cambia el formato a DATE y calcula la diferencia de fechas
                input_date_1 = datetime.datetime.strptime(check_1.group(), '%d/%m/%Y')
                input_date_2 = datetime.datetime.strptime(check_2.group(), '%d/%m/%Y')
                diff_date = abs((input_date_2 - input_date_1).days)
                console.print(f"La diferencia que hay entre [bold]{self.input_string_1}[/bold] y [bold]{self.input_string_2}[/bold] es de [green bold]{diff_date}[/green bold] días.")
                return True, True, diff_date
            else:
                if not check_1:
                    console.print("No se introdujo la primera fecha válida (DD/MM/YYYY)")
                else:
                    console.print("No se introdujo la segunda fecha válida (DD/MM/YYYY)")
        except Exception as error:
            console.print(f"[red]Error en check date: {error}[red]")


def main():
    input_string_1 = Prompt.ask("Introduzca la primera fecha, y presione ENTER (q --> Exit)").rstrip().lstrip()
    if input_string_1 == "q":
        sys.exit("Proceso finalizado!")

    input_string_2 = Prompt.ask("Introduzca la segunda fecha, y presione ENTER (q --> Exit)").rstrip().lstrip()
    if input_string_2 == "q":
        sys.exit("Proceso finalizado!")

    # Obtener la diferencia de días que hay entre dos fechas
    DaysBetween(input_string_1, input_string_2).check_date()


if __name__ == '__main__':
    typer.run(main)
