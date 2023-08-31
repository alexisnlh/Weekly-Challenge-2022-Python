import sys
import typer
from rich.console import Console
from rich.prompt import Prompt

console = Console(color_system="windows")
# Reto #14
# ¿Es un número de Armstrong?
# Fecha publicación enunciado: 04/04/22
# Fecha publicación resolución: 11/04/22
# Dificultad: FÁCIL

# Enunciado: Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista).
# Si no conoces qué es un número de Armstrong, debes buscar información al respecto.


class IsArmstrong:
    """
        Calcular si el número ingresado es un número Armstrong (o también llamado narcisista)
    """
    def __init__(self, input_number):
        self.input_number = input_number

    def check_process(self):
        if int(self.input_number) >= 0:
            sum = 0
            len_input = len(self.input_number)
            for number in self.input_number:
                sum += int(number) ** len_input
            if sum == int(self.input_number):
                console.print(
                    f"El número ingresado [bold]({self.input_number})[/bold] es un número Armstrong.")
            else:
                console.print(
                    f"El número ingresado [bold]({self.input_number})[/bold] no es un número Armstrong.")
        else:
            console.print(f"[red]El número Armstrong del dígito ingresado, {self.input_number}, no se puede obtener. El número debe ser mayor o igual a cero.[/red]")


def main():
    input_number = Prompt.ask("Introduzca el número para verificar si es un número Armstrong (o también llamado narcisista), y presione ENTER (q --> Exit)").rstrip().lstrip()

    if input_number == "q":
        sys.exit("Proceso finalizado!")

    IsArmstrong(input_number).check_process()


if __name__ == '__main__':
    typer.run(main)
