# Reto #17
# La carrera de obstáculos
# Fecha publicación enunciado: 25/04/22
# Fecha publicación resolución: 02/05/22
# Dificultad: MEDIA

# Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos
# - La función recibirá dos parámetros:
#    - Un array que sólo puede contener String con las palabras "run" o "jump"
#    - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
# - La función imprimirá cómo ha finalizado la carrera:
#    - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará el símbolo de esa parte de la pista
#    - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#    - Si hace "run" en "|" (valla), se variará la pista por "/".
# - La función retornará un Boolean que indique si ha superado la carrera. Para ello tiene que realizar la opción correcta en cada tramo de la pista


# Función para verificar si un/a atleta ha superado correctamente una carrera de obstáculos
def checkRace(run_jump_list, pista_string):
    try:
        pista_list = list()
        pista_list[:0] = pista_string
        AthleteState = {
            "run": "_",
            "jump": "|"
        }
        result = list()
        result_type = True

        # Se verifican que los string coincidan
        for elements in zip(run_jump_list, pista_list):
            if elements[1] == AthleteState[elements[0]]:
                result.append(elements[1])
            else:
                result_type = False
                if elements[1] == "_" or elements[1] == "?":
                    result.append("x")
                else:
                    result.append("/")

        # Se verifica que ambos string introducidos, convertidos a lista, tengan el mismo tamaño
        if len(run_jump_list) != len(pista_list):
            result_type = False
            if len(run_jump_list) > len(pista_list):
                count = len(run_jump_list) - len(pista_list)
            elif len(run_jump_list) < len(pista_list):
                count = len(pista_list) - len(run_jump_list)
            for element in range(0, count):
                result.append("?")

        print(f"Los valores iniciales de la carrera son: {', '.join(run_jump_list)}.\nLos valores iniciales de la pista son: {pista_string}\nLa pista resultante es: {''.join(result)}")
        return result_type
    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    flag_continue = True
    flag_run_jump = True
    flag_pista = True
    flag_stop = False
    run_jump_list = list()
    pista_string = str()

    while flag_continue:
        try:
            # Obtener los inputs de run o jump ingresados por el usuario
            while flag_run_jump:
                input_string = input("Introduzca una opción entre 'run' o 'jump', y presione ENTER. Si desea finalizar el ingreso de datos escriba 'YES' o 'Y': \n").lower()

                # Se eliminan los espacios en blanco al inicio y final de la cadena de texto ingresada
                input_string = input_string.rstrip().lstrip()

                if input_string != "" and input_string in ["run", "jump", "y", "yes"]:
                    if input_string == "y" or "yes" in input_string:
                        flag_run_jump = False
                        flag_continue = False
                    else:
                        run_jump_list.append(input_string)
                else:
                    while True:
                        opcion = input("No se introdujo un texto válido. Desea continuar? (Y/N)\n").lower()
                        if opcion == "y" or "yes" in opcion:
                            break
                        elif opcion == "n" or "no" in opcion:
                            flag_stop = True
                            flag_run_jump = False
                            flag_pista = False
                            flag_continue = False
                            break

            # Obtener los inputs de _ o | ingresados por el usuario
            while flag_pista:
                input_string = input("Introduzca una opción entre '_' (suelo) o '|' (valla), y presione ENTER. Si desea finalizar el ingreso de datos escriba 'YES' o 'Y': \n").lower()

                # Se eliminan los espacios en blanco al inicio y final de la cadena de texto ingresada
                input_string = input_string.rstrip().lstrip()

                if input_string != "" and input_string in ["_", "|", "?", "y", "yes"]:
                    if input_string == "y" or "yes" in input_string:
                        flag_pista = False
                        flag_continue = False
                    else:
                        pista_string += input_string
                else:
                    while True:
                        opcion = input("No se introdujo un texto válido. Desea continuar? (Y/N)\n").lower()
                        if opcion == "y" or "yes" in opcion:
                            break
                        elif opcion == "n" or "no" in opcion:
                            flag_stop = True
                            flag_pista = False
                            flag_continue = False
                            break

            if not flag_stop:
                # Función para verificar si un/a atleta ha superado correctamente una carrera de obstáculos
                result = checkRace(run_jump_list, pista_string)
                print(f"El resultado es {result}")
                break

        except:
            while True:
                opcion = input("No se introdujo un texto válido. Desea continuar? (Y/N)\n").lower()
                if opcion == "y" or "yes" in opcion:
                    break
                elif opcion == "n" or "no" in opcion:
                    flag_continue = False
                    break