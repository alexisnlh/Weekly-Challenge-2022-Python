import sys
import requests
import math
import typer
from PIL import Image
from io import BytesIO
from rich.console import Console

console = Console(color_system="windows")
"""
    Reto #5
    Aspect ratio de una imagen
    Fecha publicación enunciado: 01/02/22
    Fecha publicación resolución: 07/02/22
    Dificultad: DIFÍCIL

    Enunciado: Crea un programa que se encargue de calcular el aspect ratio de
    una imagen a partir de una url.
    - Url de ejemplo:
    https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
    - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de
    1920*1080px.
"""


class RationalAspectRatio:
    """
        Obtener las dimensiones de la imagen importada por URL
    """
    url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

    def get_aspect_ratio(self):
        # Obtiene la imagen desde la URL
        response = requests.get(self.__class__.url)

        # Abre el contenido de la imagen para obtener su tamaño
        img = Image.open(BytesIO(response.content))
        width, height = img.size
        console.print(f"El ancho de la imagen es: {width}", style='bold green')
        console.print(f"La altura de la imagen es: {height}", style='bold blue')

        # Verifica si tiene ancho y alto distinto de cero. Se calcula el aspect radio
        if width > 0 and height > 0:
            aspectRatio = height / width
            precision = 1e-06
            round_aspect = math.floor(aspectRatio)
            (x_end, y_end, x_init, y_init) = (1, 0, int(round_aspect), 1)
            while aspectRatio - round_aspect > precision * float(y_init) * float(y_init):
                aspectRatio = 1.0 / (aspectRatio - round_aspect)
                round_aspect = math.floor(aspectRatio)
                (x_end, y_end, x_init, y_init) = (x_init, y_init, x_end + int(round_aspect) * x_init, y_end + int(round_aspect) * y_init)
            console.print(f"El aspect ratio es [bright_white on blue1]{y_init}:{x_init}[/bright_white on blue1]")
            return x_init, y_init
        else:
            sys.exit("No se ha podido calcular el aspect ratio. La imagen no tiene un ancho ni altura válido")


if __name__ == '__main__':
    typer.run(RationalAspectRatio().get_aspect_ratio)
