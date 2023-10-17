import sys
import typer
from rich.console import Console
from rich.prompt import Prompt

console = Console(color_system="windows")
# Reto #13
# Factorial Recursivo
# Fecha publicación enunciado: 28/03/22
# Fecha publicación resolución: 04/04/22
# Dificultad: FÁCIL

# Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.


class Factorial:
    """
        Calcular el factorial del número ingresado
    """
    def __init__(self, input_number):
        self.input_number = input_number

    def calculate_factorial(self):
        if self.input_number > 1:
            number = self.input_number
            self.input_number -= 1
            return number * self.calculate_factorial()
        elif 0 < int(self.input_number) <= 1:
            return 1
        else:
            return None


def main():
    input_number = Prompt.ask("Introduzca el número para calcular el factorial, y presione ENTER (q --> Exit)")

    if input_number == "q":
        sys.exit("Proceso finalizado!")

    # Calcular el factorial del número ingresado
    result = Factorial(float(input_number)).calculate_factorial()

    if result is not None:
        console.print(
                f"El factorial del número ingresado, [bold]{input_number}[/bold], es: [green]{result}[/green]")
    else:
        console.print(
            f"[red]El factorial del número ingresado, {input_number}, no se puede obtener. El número debe ser mayor a cero.[/red]")


if __name__ == '__main__':
    typer.run(main)
