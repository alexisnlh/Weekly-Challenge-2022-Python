import re

# Reto #16
# En mayúscula
# Fecha publicación enunciado: 18/04/22
# Fecha publicación resolución: 25/04/22
# Dificultad: FÁCIL

# Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.
# - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.


# Función para modificar el texto ingresado
def capitalize(input_string):
    try:
        flag_first = False
        capitalizedText = list()

        for letter in input_string:
            # Comprueba si letter es una letra o símbolo/espacio
            check = re.search("[^A-zÀ-ú]", letter, re.IGNORECASE)
            if not check:
                # Si flag_first = True, cambia a mayúscula letter seleccionada y la almacena en la variable letter_modf, si no lo almacena en la variable letter_modf sin modificar
                if flag_first:
                    letter_modf = letter.upper()
                    flag_first = False
                else:
                    letter_modf = letter
            else:
                letter_modf = letter
                flag_first = True
            capitalizedText.append(letter_modf)

        capitalizedText = "".join(capitalizedText)
        return capitalizedText
    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    flag_continue = True
    while flag_continue:
        try:
            input_string = input("Introduzca el texto a procesar, y presione ENTER: \n")

            # Se eliminan los espacios en blanco al inicio y final de la cadena de texto ingresada
            input_string = input_string.rstrip().lstrip()

            if input_string != "":
                # Función para modificar el texto ingresado
                capitalizedText = capitalize(input_string)
                print(f"El texto ingresado modificado es: {capitalizedText}")
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