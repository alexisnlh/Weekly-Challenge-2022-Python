import sys
import typer
from rich.console import Console
from rich.prompt import Prompt, IntPrompt

console = Console(color_system="windows")
# Reto #7
# Contando palabras
# Fecha publicación enunciado: 14/02/22
# Fecha publicación resolución: 21/02/22
# Dificultad: MEDIA

# Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
#  - Los signos de puntuación no forman parte de la palabra.
#  - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.


class CountWords:
    """
        Contar las veces que se repite cada palabra
    """
    characters_delete = ",;:.\n!\"'()"

    def __init__(self, words):
        self.words = words

    def process_count(self):
        # Los caracteres que no se cuentan como palabras
        input_string = self.words
        for caracter in self.__class__.characters_delete:
            input_string = input_string.replace(caracter, "")

        mutable_string = input_string.lower().split(" ")
        words_dict = dict()

        for letter in mutable_string:
            words_dict[letter] = words_dict[letter] + 1 if letter in words_dict else 1
            # if letter in words_dict:
            #     words_dict[letter] += 1
            # else:
            #     words_dict[letter] = 1

        for letter in words_dict:
            console.print("{0} se ha repetido [bold]{1}[/bold] veces".format(letter, words_dict[letter]))


def main():
    input_string = Prompt.ask(
        "Introduzca la cadena de texto que desea verificar y presione ENTER (q --> Exit)").rstrip().lstrip()

    if input_string == "":
        main()
        sys.exit("Proceso finalizado!")

    elif input_string == "q":
        sys.exit("Proceso finalizado!")

    CountWords(input_string).process_count()


if __name__ == '__main__':
    typer.run(main)
