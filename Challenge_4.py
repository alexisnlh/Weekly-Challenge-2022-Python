import sys
import typer
from rich.console import Console
from rich.prompt import Prompt, IntPrompt, FloatPrompt

console = Console(color_system="windows")
"""
    Reto #4
    Área de un polígono
    Fecha publicación enunciado: 24/01/22
    Fecha publicación resolución: 31/01/22
    Dificultad: FÁCIL

    Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea
    capaz de calcular y retornar el área de un polígono.
    - La función recibirá por parámetro sólo UN polígono a la vez.
    - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
    - Imprime el cálculo del área de un polígono de cada tipo.
"""


class CalculateArea:
    """
        Calcular y retornar el área de un polígono
    """
    def __init__(self, base=None, height=None, side=None, length=None, width=None):
        self.base = base
        self.height = height
        self.side = side
        self.length = length
        self.width = width

    # Calcular y retornar el área de un triángulo
    def area_triangulo(self):
        area = (self.base * self.height) / 2
        console.print(f"[green]El área del triángulo es: [bold]{area}[/bold][/green]")

    # Calcular y retornar el área de un cuadrado
    def area_cuadrado(self):
        area = self.side * self.side
        console.print(f"[green]El área del cuadrado es: [bold]{area}[/bold][/green]")

    # Calcular y retornar el área de un rectángulo
    def area_rectangulo(self):
        area = self.length * self.width
        console.print(f"[green]El área del cuadrado es: [bold]{area}[/bold][/green]")


def main():
    option = IntPrompt.ask(
        "Introduzca qué polígono seleccionar y presione ENTER: \n(1 --> Triángulo, 2 --> Cuadrado, 3 --> Rectángulo, 4 --> Exit)",
        choices=["1", "2", "3", "4"], show_choices=False)

    if option == 1:
        # Ingresa los valores de base y altura
        base_input = FloatPrompt.ask(
            "¿Cuánto es la base del triángulo? y presione ENTER")
        height_input = FloatPrompt.ask(
            "¿Cuánto es la altura del triángulo? y presione ENTER")

        # Calcular y retornar el área de un triángulo
        CalculateArea(base=base_input,
                      height=height_input).area_triangulo()

    elif option == 2:
        # Ingresa la medida de un lado
        side_input = FloatPrompt.ask(
            "¿Cuánto es la medida de un lado del cuadrado? y presione ENTER")

        # Calcular y retornar el área de un cuadrado
        CalculateArea(side=side_input).area_cuadrado()

    elif option == 3:
        # Ingresa los valores de longitud y ancho
        length_input = FloatPrompt.ask(
            "¿Cuánto es la longitud del rectángulo? y presione ENTER")
        width_input = FloatPrompt.ask(
            "¿Cuánto es el ancho del rectángulo? y presione ENTER")

        # Calcular y retornar el área de un rectángulo
        CalculateArea(length=length_input,
                      width=width_input).area_rectangulo()

    else:
        sys.exit("Proceso finalizado!")


if __name__ == '__main__':
    typer.run(main)
