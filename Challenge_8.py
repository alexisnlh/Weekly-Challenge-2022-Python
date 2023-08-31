import sys
import typer
from rich.console import Console
from rich.prompt import FloatPrompt

console = Console(color_system="windows")
# Reto #8
# Decimal a binario
# Fecha publicación enunciado: 18/02/22
# Fecha publicación resolución: 02/03/22
# Dificultad: FÁCIL

# Enunciado: Crea un programa que se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.


class DecimalToBinary:
    """
        Transformar número decimal a binario
    """
    def __init__(self, input_decimal):
        self.input_decimal = input_decimal

    def transform_process(self):
        number = round(float(self.input_decimal))
        binary = str()

        while number > 0:
            reminder = number % 2
            number //= 2
            binary = str(reminder) + binary
        console.print(
            f"El binario del número decimal {self.input_decimal} es: [bold]{binary if round(float(self.input_decimal)) > 0 else 0}[/bold]")


def main():
    input_decimal = FloatPrompt.ask(
        "Introduzca un número decimal, distinto de cero y presione ENTER")

    DecimalToBinary(input_decimal).transform_process()


if __name__ == '__main__':
    typer.run(main)
