import sys
import typer
from rich.console import Console
from rich.prompt import Prompt

console = Console(color_system="windows")
"""
    Reto extra #0
    Convertir palabras en números
    Fecha publicación enunciado: 05/02/25
    Fecha publicación resolución: 05/02/25
    Dificultad: FÁCIL

    Enunciado: Escribe una función que reciba un número escrito en palabras (String)
    y retorne el número correspondiente (Int).
"""


class Convertidor:
    UNIDADES = {
        "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
        "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
        "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
        "diecisiete": 17, "dieciocho": 18, "diecinueve": 19
    }

    DECENAS = {
        "veinte": 20, "treinta": 30, "cuarenta": 40, "cincuenta": 50,
        "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90
    }

    CENTENAS = {
        "cien": 100, "doscientos": 200, "trescientos": 300,
        "cuatrocientos": 400,
        "quinientos": 500, "seiscientos": 600, "setecientos": 700,
        "ochocientos": 800, "novecientos": 900
    }

    ESCALAS = {
        "cien": 100, "mil": 1000, "millón": 1000000, "billones": 1000000000
    }

    def __init__(self, string):
        self.string = string

    def convertir_palabra_a_numero(self):
        palabras = self.string.split()
        total = 0
        actual = 0

        for palabra in palabras:
            if palabra == "y":
                continue

            if palabra in self.UNIDADES:
                actual += self.UNIDADES[palabra]

            elif palabra in self.DECENAS:
                actual += self.DECENAS[palabra]

            elif palabra in self.CENTENAS:
                actual += self.CENTENAS[palabra]

            elif palabra in self.ESCALAS:
                if actual == 0:
                    actual = 1
                total += actual * self.ESCALAS[palabra]
                actual = 0

            else:
                return f"{self.string} no es un número válido."

        return total + actual


def main():
    input_string = Prompt.ask("Introduzca el número en letras y presione ENTER (exit para salir)").lower()

    if input_string == "exit":
        sys.exit("Proceso finalizado!")

    if not input_string:
        console.print("El texto introducido no es válido. Intente de nuevo.")
        main()
    else:
        string_to_number = Convertidor(input_string)
        result = string_to_number.convertir_palabra_a_numero()
        console.print(result)
        main()


if __name__ == '__main__':
    typer.run(main)
