# Reto #9
# Código Morse
# Fecha publicación enunciado: 02/03/22
# Fecha publicación resolución: 07/03/22
# Dificultad: MEDIA

# Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.


naturalDict = {
            "A": ".—",
            "B": "—...",
            "C": "—.—.",
            "CH": "————",
            "D": "—..",
            "E": ".",
            "F": "..—.",
            "G": "——.",
            "H": "....",
            "I": "..",
            "J": ".———",
            "K": "—.—",
            "L": ".—..",
            "M": "——",
            "N": "—.",
            "Ñ": "——.——",
            "O": "———",
            "P": ".——.",
            "Q": "——.—",
            "R": ".—.",
            "S": "...",
            "T": "—",
            "U": "..—",
            "V": "...—",
            "W": ".——",
            "X": "—..—",
            "Y": "—.——",
            "Z": "——..",
            "0": "—————",
            "1": ".————",
            "2": "..———",
            "3": "...——",
            "4": "....—",
            "5": ".....",
            "6": "—....",
            "7": "——...",
            "8": "———..",
            "9": "————.",
            ".": ".—.—.—",
            ",": "——..——",
            "?": "..——..",
            "\"": ".—..—.",
            "/": "—..—."
        }


def decoder(input_string):
    try:
        morseText_list = list()
        morseText = str()
        morse = False

        # Verifica si el string ingresado es una cadena de texto o código morse
        if not set(input_string) <= {'.', '—', ' '}:
            # Texto natural
            flag = False
            morse = True

            for index, letter in enumerate(input_string.upper()):
                if letter in naturalDict.keys() or letter == " ":
                    if letter != " ":
                        if not flag:
                            if letter == "C" and input_string.upper()[index + 1] == "H":
                                morseText += naturalDict["CH"] + " "
                                flag = True
                            else:
                                morseText += naturalDict[letter] + " "
                        else:
                            flag = False
                            continue
                    else:
                        morseText += " "
                else:
                    return False, morse, letter

        else:
            # Código morse
            input_string += " "
            subtext = str()

            for letter in input_string:
                # Verifica si hay espacio para transformar la letra del código morse
                if letter != " ":
                    index = 0
                    subtext += letter
                else:
                    index += 1

                    # Verifica si es un final de código morse o es un espacio para agregar al texto final
                    if index == 2:
                        morseText += " "
                    else:
                        morseText += list(naturalDict.keys())[list(naturalDict.values()).index(subtext)]
                        subtext = str()
        return True, morse, morseText.rstrip()
    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    while True:
        try:
            input_string = input("Introduzca la cadena de texto o código morse a transformar y presione ENTER: \n")
            if input_string != "":
                # Función para contar las veces que se repite cada palabra
                result, morse, morseText = decoder(input_string)
                if result:
                    if morse:
                        print(f"El código morse de la cadena de texto ingresada es: {morseText}")
                    else:
                        print(f"La cadena de texto del código morse ingresado es: {morseText}")
                else:
                    print(f"No se pudo transformar la cadena de texto/código morse ingresado por no encontrarse el caracter {morseText}")
                break
            else:
                opcion = input("No se introdujo una cadena de texto o código morse válida. Desea continuar? (Y/N)\n").lower()
                if opcion == "n" or "no" in opcion:
                    break
        except:
            opcion = input("No se introdujo una cadena de texto o código morse válida. Desea continuar? (Y/N)\n").lower()
            if opcion == "n" or "no" in opcion:
                break