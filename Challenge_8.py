# Reto #8
# Decimal a binario
# Fecha publicación enunciado: 18/02/22
# Fecha publicación resolución: 02/03/22
# Dificultad: FÁCIL

# Enunciado: Crea un programa que se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.


# Función para contar las veces que se repite cada palabra
def decimalToBinary(input_string):
    try:
        pass
        number = int(input_string)
        binary = str()

        while number > 0:
            reminder = number % 2
            number //= 2
            binary = str(reminder) + binary
        return binary if int(input_string) > 0 else 0
    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    while True:
        try:
            input_string = input("Introduzca un número decimal, distinto de cero y presione ENTER: \n")
            input_string = input_string.rstrip().lstrip()
            if input_string != "":
                # Función para contar las veces que se repite cada palabra
                print(f"El binario del número decimal {input_string} es: {decimalToBinary(input_string)}")
                break
            else:
                opcion = input("No se introdujo una cadena de texto válida. Desea continuar? (Y/N)\n").lower()
                if opcion == "n" or "no" in opcion:
                    break
        except:
            opcion = input("No se introdujo una cadena de texto válida. Desea continuar? (Y/N)\n").lower()
            if opcion == "n" or "no" in opcion:
                break