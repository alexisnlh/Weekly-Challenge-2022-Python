"""
    Reto #1
    ¿Es un anagrama?
    Fecha publicación enunciado: 03/01/22
    Fecha publicación resolución: 10/01/22
    Dificultad: MEDIA

    Enunciado: Escribe una función que reciba dos palabras (String) y
    retorne verdadero o falso (Bool) según sean o no anagramas.
    Un Anagrama consiste en formar una palabra reordenando TODAS las letras de
    otra palabra inicial.
    NO hace falta comprobar que ambas palabras existan.
    Dos palabras exactamente iguales no son anagrama.
"""


class Anagrama:
    """
        Función 1 para introducir dos palabras y verificar si es un anagrama
        (return True) o no (return False)
    """
    def __init__(self, string_1, string_2):
        self.string_1 = string_1
        self.string_2 = string_2

    def option_1(self):
        result_1 = ''.join(sorted(self.string_1, reverse=True))
        result_2 = ''.join(sorted(self.string_2, reverse=True))

        if self.string_2 == result_1 or self.string_1 == result_2:
            print(
                " El resultado es VERDADERO. La palabra {0} es un anagrama de {1}.".format(
                    self.string_1, self.string_2))
        else:
            print(
                " El resultado es FALSO. La palabra {0} no es un anagrama de {1}.".format(
                    self.string_1, self.string_2))

    # Función 2 para introducir dos palabras y verificar si es un anagrama
    # (return True) o no (return False)
    def option_2(self):
        if sorted(self.string_1) == sorted(self.string_2):
            print(
                " El resultado es VERDADERO. La palabra {0} es un anagrama de {1}.".format(
                    self.string_1, self.string_2))
        else:
            print(
                " El resultado es FALSO. La palabra {0} no es un anagrama de {1}.".format(
                    self.string_1, self.string_2))


if __name__ == '__main__':
    flag_continue = True
    while flag_continue:
        try:
            opcion = int(input(
                "Introduzca qué función ejecutar (1 o 2)? y presione ENTER: \n"))
            input_1 = input(
                "Introduzca la primera palabra y presione ENTER: \n").lower()
            input_2 = input(
                "Introduzca la segunda palabra y presione ENTER: \n").lower()

            if opcion == 1:
                option = Anagrama(input_1, input_2)
                option.option_1()
                break
            elif opcion == 2:
                option = Anagrama(input_1, input_2)
                option.option_2()
                break
            else:
                while True:
                    opcion = input("No seleccionaste una opción válida. Desea continuar? (Y/N)\n").lower()
                    if opcion == "y" or "yes" in opcion:
                        break
                    elif opcion == "n" or "no" in opcion:
                        flag_continue = False
                        break
        except KnownException:
            while True:
                opcion = input("No seleccionaste una opción válida. Desea continuar? (Y/N)\n").lower()
                if opcion == "y" or "yes" in opcion:
                    break
                elif opcion == "n" or "no" in opcion:
                    flag_continue = False
                    break
