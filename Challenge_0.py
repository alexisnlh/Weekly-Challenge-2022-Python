# Reto #0
# El famoso "FIZZ BUZZ"
# Fecha publicación enunciado: 27/12/21
# Fecha publicación resolución: 03/01/22
# Dificultad: FÁCIL

# Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".


def fizzbuzz():
    try:
        for number in range(1, 101):
            if number % 3 == 0 and number % 5 == 0:
                print("fizzbuzz")
            elif number % 3 == 0:
                print("fizz")
            elif number % 5 == 0:
                print("buzz")
            else:
                print(number)
    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    fizzbuzz()