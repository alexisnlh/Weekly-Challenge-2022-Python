import typer
from rich.console import Console

console = Console(color_system="windows")
"""
    Reto #0
    El famoso "FIZZ BUZZ"
    Fecha publicación enunciado: 27/12/21
    Fecha publicación resolución: 03/01/22
    Dificultad: FÁCIL

    Enunciado: Escribe un programa que muestre por consola (con un print) los
    números de 1 a 100 (ambos incluidos y con un salto de línea entre cada
    impresión), sustituyendo los siguientes:
    - Múltiplos de 3 por la palabra "fizz".
    - Múltiplos de 5 por la palabra "buzz".
    - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


class FizzBuzz:
    """
        Función para imprimir los números del 1 al 100 (ambos incluidos) y si
        es múltipo de 3 imprimir "fizz", si es múltiplo de 5 imprimir "buzz"
        y si es múltiplo de 3 y 5 imprimir "fizzbuzz
    """
    @staticmethod
    def print_fizzbuzz():
        console.print("Programa FizzBuzz! 💥", style='bold green')
        for number in range(1, 101):
            if number % 3 == 0 and number % 5 == 0:
                console.print("fizzbuzz", style='bold purple')
            elif number % 3 == 0:
                console.print("[bright_white]-->[/bright_white] [bright_white on bright_red]fizz[/bright_white on bright_red]")
            elif number % 5 == 0:
                console.print("[bright_white]-->[/bright_white] [bright_white on blue1]buzz[/bright_white on blue1]")
            else:
                console.print(f"{number}", style='color(63)')


if __name__ == '__main__':
    typer.run(FizzBuzz.print_fizzbuzz)
