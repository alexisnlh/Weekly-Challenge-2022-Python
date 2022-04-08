# Reto #4
# Área de un polígono
# Fecha publicación enunciado: 24/01/22
# Fecha publicación resolución: 31/01/22
# Dificultad: FÁCIL

# Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.


# Función para calcular y retornar el área de un polígono
def calc_area(base=None, height=None, side=None, length=None, width=None):
    try:
        if base is not None and height is not None:
            return (base * height) / 2

        elif side is not None:
            return side * side

        elif length is not None and width is not None:
            return length * width

    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    while True:
        try:
            opcion = int(input("Introduzca qué polígono seleccionar (1, 2 o 3) y presione ENTER:\n1. Triángulo\n2. Cuadrado\n3. Rectángulo\n"))

            if opcion == 1:
                # Ingresa los valores de base y altura
                base_input = int(input("¿Cuánto es la base del triángulo? y presione ENTER:\n"))
                height_input = int(input("¿Cuánto es la altura del triángulo? y presione ENTER:\n"))

                # Función para calcular y retornar el área de un triángulo
                area = calc_area(base=base_input, height=height_input)
                print("El área del triángulo es: {}".format(area))
                break

            elif opcion == 2:
                # Ingresa la medida de un lado
                side_input = int(input("¿Cuánto es la medida de un lado del cuadrado? y presione ENTER:\n"))

                # Función para calcular y retornar el área de un cuadrado
                area = calc_area(side=side_input)
                print("El área del cuadrado es: {}".format(area))
                break

            elif opcion == 3:
                # Ingresa los valores de longitud y ancho
                length_input = int(input("¿Cuánto es la longitud del rectángulo? y presione ENTER:\n"))
                width_input = int(input("¿Cuánto es el ancho del rectángulo? y presione ENTER:\n"))

                # Función para calcular y retornar el área de un rectángulo
                area = calc_area(length=length_input, width=width_input)
                print("El área del cuadrado es: {}".format(area))
                break

            else:
                opcion = input("No seleccionaste una opción válida. Desea continuar? (Y/N)\n").lower()
                if opcion == "n" or "no" in opcion:
                    break
        except:
            opcion = input("No seleccionaste una opción válida. Desea continuar? (Y/N)\n").lower()
            if opcion == "n" or "no" in opcion:
                break