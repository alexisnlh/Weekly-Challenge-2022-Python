# Reto #13
# Factorial Recursivo
# Fecha publicación enunciado: 28/03/22
# Fecha publicación resolución: 04/04/22
# Dificultad: FÁCIL

# Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.


# Función para calcular el factorial del número ingresado
def factorial(input_string):
    try:
        if int(input_string) > 1:
            number = int(input_string)
            return number * factorial(number - 1)
        elif 0 < int(input_string) <= 1:
            return 1
        else:
            return None
    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    flag_continue = True
    while flag_continue:
        try:
            input_string = input("Introduzca el número para calcular el factorial, y presione ENTER: \n")
            input_string = input_string.rstrip().lstrip()
            if input_string != "":
                # Función para calcular el factorial del número ingresado
                result = factorial(input_string)
                if result is not None:
                    print(f"El factorial del número ingresado, {input_string}, es: {result}")
                    break
                else:
                    print(f"El factorial del número ingresado, {input_string}, no se puede obtener. El número debe ser mayor a cero.")
                    while True:
                        opcion = input("No se introdujo un texto válido. Desea continuar? (Y/N)\n").lower()
                        if opcion == "y" or "yes" in opcion:
                            break
                        elif opcion == "n" or "no" in opcion:
                            flag_continue = False
                            break
            else:
                while True:
                    opcion = input("No se introdujo un texto válido. Desea continuar? (Y/N)\n").lower()
                    if opcion == "y" or "yes" in opcion:
                        break
                    elif opcion == "n" or "no" in opcion:
                        flag_continue = False
                        break
        except:
            while True:
                opcion = input("No se introdujo un texto válido. Desea continuar? (Y/N)\n").lower()
                if opcion == "y" or "yes" in opcion:
                    break
                elif opcion == "n" or "no" in opcion:
                    flag_continue = False
                    break