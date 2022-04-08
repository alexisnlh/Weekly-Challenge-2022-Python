# Reto #3
# ¿Es un número primo?
# Fecha publicación enunciado: 17/01/22
# Fecha publicación resolución: 24/01/22
# Dificultad: MEDIA

# Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.


# Función para comprobar si un número es o no primo
def esPrimo(number, num=2):
    try:
        if number < 1:
            return False
        if number == num:
            return True
        elif number % num != 0:
            return esPrimo(number, num=num + 1)
        else:
            return False
    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    for number in range(1, 101):
        # Función para comprobar si un número es o no primo
        result = esPrimo(number)
        if result:
            print(number)