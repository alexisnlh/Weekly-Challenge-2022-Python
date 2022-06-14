# Reto #12
# ¿Es un palíndromo?
# Fecha publicación enunciado: 21/03/22
# Fecha publicación resolución: 28/03/22
# Dificultad: MEDIA

# Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
# NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.

# Variables globales (se puede agregar más símbolos según se necesite)
chars_replace = {
    " ": "",
    "\\": "",
    "`": "",
    "*": "",
    "_": "",
    "{": "",
    "}": "",
    "[": "",
    "]": "",
    "(": "",
    ")": "",
    ">": "",
    "#": "",
    "+": "",
    "-": "",
    ".": "",
    ",": "",
    "¡": "",
    "!": "",
    "¿": "",
    "?": "",
    "$": "",
    "&": "",
    "%": "",
    "@": "",
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u"
}


# Función para verificar si el texto ingresado es palíndromo o no
def isPalindrome(input_string):
    input_string = input_string.lower()
    for key, value in chars_replace.items():
        input_string = input_string.replace(key, value)
    return input_string == input_string[::-1]


if __name__ == '__main__':
    while True:
        try:
            input_string = input("Introduzca el texto a verificar si es palíndromo o no, y presione ENTER: \n")
            if input_string != "":
                # Función para verificar si el texto ingresado es palíndromo o no
                result = isPalindrome(input_string)
                if result:
                    print(f"El texto introducido ({input_string}) es palíndromo.")
                else:
                    print(f"El texto introducido ({input_string}) NO es palíndromo.")
                break
            else:
                opcion = input("No se introdujo un texto válido. Desea continuar? (Y/N)\n").lower()
                if opcion == "n" or "no" in opcion:
                    break
        except:
            opcion = input("No se introdujo un texto válido. Desea continuar? (Y/N)\n").lower()
            if opcion == "n" or "no" in opcion:
                break