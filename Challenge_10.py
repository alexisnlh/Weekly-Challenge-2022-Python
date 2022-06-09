# Reto #10
# Expresiones equilibradas
# Fecha publicación enunciado: 07/03/22
# Fecha publicación resolución: 14/03/22
# Dificultad: MEDIA

# Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
# - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
# - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
# - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
# - Expresión no balanceada: { a * ( c + d ) ] - 5 }


# Función para verificar los paréntesis, llaves y corchetes de la expresión ingresada
def isBalanced(input_string):
    try:
        # Contadores por cada signo a verificar
        count_parenth_open = 0
        count_parenth_close = 0
        count_keys_open = 0
        count_keys_close = 0
        count_square_open = 0
        count_square_close = 0

        # Se verifican los signos en la expresión y se aumentan los contadores de cada uno para luego compararlos
        for letter in input_string:
            if letter == "(":
                count_parenth_open += 1
            elif letter == ")":
                count_parenth_close += 1
            elif letter == "{":
                count_keys_open += 1
            elif letter == "}":
                count_keys_close += 1
            elif letter == "[":
                count_square_open += 1
            elif letter == "]":
                count_square_close += 1

        # Crea el mensaje de retorno con la información verificada
        if count_parenth_open == count_parenth_close and count_keys_open == count_keys_close and count_square_open == count_square_close:
            message = "La expresión aritmética se ha verificado y está balanceada correctamente!"
        else:
            message = "La expresión aritmética está desbalanceada. Tiene"

            if count_parenth_open != count_parenth_close:
                if count_parenth_open > count_parenth_close:
                    message += " '(' de mas,"
                else:
                    message += " ')' de mas,"

            if count_keys_open != count_keys_close:
                if count_keys_open > count_keys_close:
                    message += " '{' de mas,"
                else:
                    message += " '}' de mas,"

            if count_square_open != count_square_close:
                if count_square_open > count_square_close:
                    message += " '[' de mas,"
                else:
                    message += " ']' de mas,"

            # Verifica si el mensaje tiene ',' al final para eliminarlo
            if message[-1] == ",":
                message = message[:-1]
        return message
    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    while True:
        try:
            input_string = input("Introduzca la expresión aritmética a verificar y presione ENTER: \n")
            if input_string != "":
                # Función para verificar los paréntesis, llaves y corchetes de la expresión ingresada
                print(isBalanced(input_string))
                break
            else:
                opcion = input("No se introdujo una expresión aritmética válida. Desea continuar? (Y/N)\n").lower()
                if opcion == "n" or "no" in opcion:
                    break
        except:
            opcion = input("No se introdujo una expresión aritmética válida. Desea continuar? (Y/N)\n").lower()
            if opcion == "n" or "no" in opcion:
                break