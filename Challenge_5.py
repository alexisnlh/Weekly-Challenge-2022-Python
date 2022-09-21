import requests
import math
from PIL import Image
from io import BytesIO


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

url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"


class rationalAspectRatio:
    """
        Obtener las dimensiones de la imagen importada por URL
    """
    def __init__(self, url):
        self.url = url

    def get_aspect_ratio(self):
        # Obtiene la imagen desde la URL
        response = requests.get(self.url)

        # Abre el contenido de la imagen para obtener su tamaño
        img = Image.open(BytesIO(response.content))
        width, height = img.size
        print(f"El ancho de la imagen es: {width}")
        print(f"La altura de la imagen es: {height}")

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
            return x_init, y_init
        else:
            print("La imagen no tiene un ancho ni altura válido")
            return None, None


if __name__ == '__main__':
    # Obtener las dimensiones de la imagen importada por URL
    x, y = rationalAspectRatio(url).get_aspect_ratio()

    if x is not None and y is not None:
        print(f"El aspect ratio es {y}:{x}")
    else:
        print("No se ha podido calcular el aspect ratio")