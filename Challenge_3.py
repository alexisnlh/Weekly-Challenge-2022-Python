"""
    Reto #3
    ¿Es un número primo?
    Fecha publicación enunciado: 17/01/22
    Fecha publicación resolución: 24/01/22
    Dificultad: MEDIA

    Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
    Hecho esto, imprime los números primos entre 1 y 100.
"""


class EsPrimo:
    """
        Comprobar si un número es o no primo
    """
    def __init__(self, number, check_number):
        self.number = number
        self.check_number = check_number

    def print_number(self):
        if self.number <= 1:
            pass
        else:
            if self.number == self.check_number:
                print(self.number)
            elif self.number % self.check_number != 0:
                EsPrimo(self.number, self.check_number + 1).print_number()
            else:
                pass


if __name__ == '__main__':
    for index in range(1, 101):
        # Comprueba si un número es o no primo
        EsPrimo(index, 2).print_number()
