import sys
import typer
from rich.console import Console
from rich.prompt import Prompt

console = Console(color_system="windows")
# Reto #19
# CONVERSOR TIEMPO
# Fecha publicación enunciado: 09/05/22
# Fecha publicación resolución: 16/05/22
# Dificultad: FACIL

# Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.


class TimeToMillis:
    """
        Conversor de días, horas, minutos y segundos en milisegundos
    """
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def convert_process(self):
        try:
            days_in_millis = int(self.kwargs['dias']) * 86400 * 1000
            hours_in_millis = int(self.kwargs['horas']) * 3600 * 1000
            minutes_in_millis = int(self.kwargs['minutos']) * 60 * 1000
            seconds_in_millis = int(self.kwargs['segundos']) * 1000
            millis = days_in_millis + hours_in_millis + minutes_in_millis + seconds_in_millis
            console.print(f"La conversión de {self.kwargs['dias']} días, {self.kwargs['horas']} horas, {self.kwargs['minutos']} minutos y {self.kwargs['segundos']} segundos es: [green bold]{millis}[/green bold]")
        except Exception as error:
            console.print(f"[red]Se introdujo un campo incorrecto: {error}[/red]")


def main():
    dict_options = {
        "dias": "",
        "horas": "",
        "minutos": "",
        "segundos": ""
    }
    for option in dict_options:
        input_string = Prompt.ask(f"Introduzca los {option} y presione ENTER (q --> Exit)")
        if input_string == "q":
            sys.exit("Proceso finalizado!")

        dict_options[option] = input_string

    TimeToMillis(dias=dict_options["dias"], horas=dict_options["horas"], minutos=dict_options["minutos"], segundos=dict_options["segundos"]).convert_process()


if __name__ == '__main__':
    typer.run(main)
