import sys
import typer
from rich.console import Console
from rich.prompt import Prompt

console = Console(color_system="windows")
# Reto #17
# La carrera de obstáculos
# Fecha publicación enunciado: 25/04/22
# Fecha publicación resolución: 02/05/22
# Dificultad: MEDIA

# Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos
# - La función recibirá dos parámetros:
#    - Un array que sólo puede contener String con las palabras "run" o "jump"
#    - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
# - La función imprimirá cómo ha finalizado la carrera:
#    - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará el símbolo de esa parte de la pista
#    - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#    - Si hace "run" en "|" (valla), se variará la pista por "/".
# - La función retornará un Boolean que indique si ha superado la carrera. Para ello tiene que realizar la opción correcta en cada tramo de la pista


class Race:
    """
        Verificar si un/a atleta ha superado correctamente una carrera de obstáculos
    """

    athlete_state = {
        "run": "_",
        "jump": "|"
    }

    def __init__(self, runjump_list, track_string):
        self.runjump_list = runjump_list
        self.track_string = track_string

    def checkRace(self):
        pista_list = list()
        pista_list[:0] = self.track_string
        result = list()
        count = 0

        # Se verifican que los string coincidan
        for elements in zip(self.runjump_list, self.track_string):
            if elements[1] == self.__class__.athlete_state[elements[0]]:
                result.append(elements[1])
            else:
                if elements[1] == "_" or elements[1] == "?":
                    result.append("x")
                else:
                    result.append("/")

        # Se verifica que ambos string introducidos, convertidos a lista, tengan el mismo tamaño
        if len(self.runjump_list) != len(self.track_string):
            if len(self.runjump_list) > len(self.track_string):
                count = len(self.runjump_list) - len(self.track_string)
            elif len(self.runjump_list) < len(self.track_string):
                count = len(self.track_string) - len(self.runjump_list)
            for element in range(0, count):
                result.append("?")

        console.print(f"\nLos valores iniciales de la carrera son: [bold]{', '.join(self.runjump_list)}[/bold].\nLos valores iniciales de la pista son:[bold]{self.track_string}[/bold]\nLa pista resultante es: [bold]{''.join(result)}[/bold]")


def main():
    flag_run_jump = True
    flag_track = True
    runjump_list = list()
    track_string = str()

    while flag_run_jump:
        input_string = Prompt.ask(
            "\nIntroduzca una opción entre 'run' o 'jump', y presione ENTER. Si desea finalizar el ingreso de datos escriba 'YES' o 'Y' (q --> Exit)", choices=["run", "jump", "YES", "Y", "yes", "y", "q"], show_choices=False).lower()
        if input_string == "q":
            sys.exit("Proceso finalizado!")
        elif input_string in ["YES", "Y", "yes", "y"]:
            break
        else:
            runjump_list.append(input_string)

    while flag_track:
        input_string = Prompt.ask(
            "\nIntroduzca una opción entre '_' (suelo) o '|' (valla), y presione ENTER. Si desea finalizar el ingreso de datos escriba 'YES' o 'Y' (q --> Exit)", choices=["_", "|", "YES", "Y", "yes", "y", "q"], show_choices=False).lower().rstrip().lstrip()
        if input_string == "q":
            sys.exit("Proceso finalizado!")
        elif input_string in ["YES", "Y", "yes", "y"]:
            break
        else:
            track_string += input_string

    Race(runjump_list, track_string).checkRace()


if __name__ == '__main__':
    typer.run(main)
