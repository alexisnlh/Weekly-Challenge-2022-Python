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
        if self.base is not None and self.height is not None:
            area = (self.base * self.height) / 2
            print(f"El área del triángulo es: {area}")
        else:
            print(
                "Se debe ingresar un valor numérico válido para la base y altura del triángulo")

    # Calcular y retornar el área de un cuadrado
    def area_cuadrado(self):
        if self.side is not None:
            area = self.side * self.side
            print(f"El área del cuadrado es: {area}")
        else:
            print(
                "Se debe ingresar un valor numérico válido para el lado del cuadrado")

    # Calcular y retornar el área de un rectángulo
    def area_rectangulo(self):
        if self.length is not None and self.width is not None:
            area = self.length * self.width
            print(f"El área del cuadrado es: {area}")
        else:
            print(
                "Se debe ingresar un valor numérico válido para la longitud y el ancho del rectángulo")


if __name__ == '__main__':
    flag_continue = True
    while flag_continue:
        try:
            opcion = int(input(
                "Introduzca qué polígono seleccionar (1, 2 o 3) y presione ENTER:\n1. Triángulo\n2. Cuadrado\n3. Rectángulo\n"))

            if opcion == 1:
                # Ingresa los valores de base y altura
                base_input = int(input(
                    "¿Cuánto es la base del triángulo? y presione ENTER:\n"))
                height_input = int(input(
                    "¿Cuánto es la altura del triángulo? y presione ENTER:\n"))

                # Calcular y retornar el área de un triángulo
                CalculateArea(base=base_input,
                              height=height_input).area_triangulo()
                break

            elif opcion == 2:
                # Ingresa la medida de un lado
                side_input = int(input(
                    "¿Cuánto es la medida de un lado del cuadrado? y presione ENTER:\n"))

                # Calcular y retornar el área de un cuadrado
                CalculateArea(side=side_input).area_cuadrado()
                break

            elif opcion == 3:
                # Ingresa los valores de longitud y ancho
                length_input = int(input(
                    "¿Cuánto es la longitud del rectángulo? y presione ENTER:\n"))
                width_input = int(input(
                    "¿Cuánto es el ancho del rectángulo? y presione ENTER:\n"))

                # Calcular y retornar el área de un rectángulo
                CalculateArea(length=length_input,
                              width=width_input).area_rectangulo()
                break

            else:
                while True:
                    opcion = input(
                        "No seleccionaste una opción válida. Desea continuar? (Y/N)\n").lower()
                    if opcion == "y" or "yes" in opcion:
                        break
                    elif opcion == "n" or "no" in opcion:
                        flag_continue = False
                        break
        except (ValueError, Exception):
            while True:
                opcion = input(
                    "No seleccionaste una opción válida. Desea continuar? (Y/N)\n").lower()
                if opcion == "y" or "yes" in opcion:
                    break
                elif opcion == "n" or "no" in opcion:
                    flag_continue = False
                    break
