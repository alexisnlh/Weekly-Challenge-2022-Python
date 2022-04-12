import requests
from PIL import Image
from io import BytesIO
import math

url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"

# Función para obtener las dimensiones de la imagen importada por URL
def rationalAspectRatio():
    try:
        # Obtiene la imagen desde la URL
        response = requests.get(url)

        # Abre el contenido de la imagen para obtener su tamaño
        img = Image.open(BytesIO(response.content))
        width, height = img.size
        print("El ancho de la imagen es: {}".format(width))
        print("La altura de la imagen es: {}".format(height))

        # Verifica si tiene ancho y alto distinto de cero. Se calcula el aspect radio
        if width > 0 and height > 0:
            aspectRatio = height / width
            precision = 1e-06
            a = math.floor(aspectRatio)
            (h1, k1, h, k) = (1, 0, int(a), 1)
            while aspectRatio - a > precision * float(k) * float(k):
                aspectRatio = 1.0 / (aspectRatio - a)
                a = math.floor(aspectRatio)
                (h1, k1, h, k) = (h, k, h1 + int(a) * h, k1 + int(a) * k)
            return h, k
        else:
            print("La imagen no tiene un ancho ni altura válido")
            return None, None
    except Exception as error:
        print("Exception: {}".format(error))
        return None, None


if __name__ == '__main__':
    # Función para obtener las dimensiones de la imagen importada por URL
    h, k = rationalAspectRatio()

    if h is not None and k is not None:
        print("El aspect ratio es {0}:{1}".format(k, h))
    else:
        print("No se ha podido calcular el aspect ratio")