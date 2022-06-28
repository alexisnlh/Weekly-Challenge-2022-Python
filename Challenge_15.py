import datetime
import re

# Reto #15
# ¿Cuántos días?
# Fecha publicación enunciado: 11/04/22
# Fecha publicación resolución: 18/04/22
# Dificultad: DIFÍCIL

# Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
# - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# - La función recibirá dos String y retornará un Int.
# - La diferencia en días será absoluta (no importa el orden de las fechas).
# - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.


# Función para obtener la diferencia de días que hay entre dos fechas
def daysBetween(input_string_1, input_string_2):
    try:
        # Comprueba que el formato es el correcto para ambas cadenas de texto ingresadas, si no, se informa cual no es correcta
        check_1 = re.search("([0-9]){2}[\/]([0-9]){2}[\/]([0-9]){4}", input_string_1, re.IGNORECASE)
        check_2 = re.search("([0-9]){2}[/]([0-9]){2}[/]([0-9]){4}", input_string_2, re.IGNORECASE)

        if check_1 and check_2:
            # Obtiene el campo fecha, cambia el formato a DATE y calcula la diferencia de fechas
            input_string_1 = check_1.group()
            input_string_2 = check_2.group()
            input_date_1 = datetime.datetime.strptime(input_string_1, '%d/%m/%Y')
            input_date_2 = datetime.datetime.strptime(input_string_2, '%d/%m/%Y')
            diff_date = abs((input_date_2 - input_date_1).days)
            return True, True, diff_date
        else:
            if not check_1:
                return False, None, None
            else:
                return None, False, None
    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    flag_continue = True
    while flag_continue:
        try:
            input_string_1 = input("Introduzca la primera fecha, y presione ENTER: \n")
            input_string_2 = input("Introduzca la segunda fecha, y presione ENTER: \n")

            # Se eliminan los espacios en blanco al inicio y final de las cadenas de texto ingresadas
            input_string_1 = input_string_1.rstrip().lstrip()
            input_string_2 = input_string_2.rstrip().lstrip()

            # Función para obtener la diferencia de días que hay entre dos fechas
            check_1, check_2, result = daysBetween(input_string_1, input_string_2)

            if check_1 and check_2:
                print(f"La diferencia que hay entre {input_string_1} y {input_string_2} es de {result} días.")
                break
            else:
                if not check_1:
                    while True:
                        opcion = input("No se introdujo la primera fecha válida (DD/MM/YYYY). Desea continuar? (Y/N)\n").lower()
                        if opcion == "y" or "yes" in opcion:
                            break
                        elif opcion == "n" or "no" in opcion:
                            flag_continue = False
                            break
                else:
                    while True:
                        opcion = input("No se introdujo la segunda fecha válida (DD/MM/YYYY). Desea continuar? (Y/N)\n").lower()
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