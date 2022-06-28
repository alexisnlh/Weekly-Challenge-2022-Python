# Reto #14
# ¿Es un número de Armstrong?
# Fecha publicación enunciado: 04/04/22
# Fecha publicación resolución: 11/04/22
# Dificultad: FÁCIL

# Enunciado: Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista).
# Si no conoces qué es un número de Armstrong, debes buscar información al respecto.


# Función para calcular si el número ingresado es un número Armstrong (o también llamado narcisista)
def isArmstrong(input_string):
    try:
        if int(input_string) >= 0:
            sum = 0
            len_input = len(input_string)
            for number in input_string:
                sum += int(number) ** len_input
            return sum
        else:
            return None
    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    flag_continue = True
    while flag_continue:
        try:
            input_string = input("Introduzca el número para verificar si es un número Armstrong (o también llamado narcisista), y presione ENTER: \n")
            input_string = input_string.rstrip().lstrip()
            if input_string != "":
                # Función para calcular si el número ingresado es un número Armstrong (o también llamado narcisista)
                result = isArmstrong(input_string)
                if result is not None:
                    if result == int(input_string):
                        print(f"El número ingresado ({input_string}) es un número Armstrong.")
                    else:
                        print(f"El número ingresado ({input_string}) no es un número Armstrong.")
                    break
                else:
                    print(f"El número Armstrong del dígito ingresado, {input_string}, no se puede obtener. El número debe ser mayor o igual a cero.")
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