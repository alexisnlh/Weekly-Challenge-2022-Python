# Reto #2
# La sucesión de Fibonacci
# Fecha publicación enunciado: 10/01/22
# Fecha publicación resolución: 17/01/22
# Dificultad: DIFÍCIL

# Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...

# Función para imprimir los 50 primeros números de la sucesión de Fibonacci
def fibonacci():
    try:
        num_0 = 0
        num_1 = 1
        for number in range(1, 51):
            print(num_0)
            num_next = num_0 + num_1
            num_0 = num_1
            num_1 = num_next
    except Exception as error:
        print("Exception: {}".format(error))


if __name__ == '__main__':
    # Función para imprimir los 50 primeros números de la sucesión de Fibonacci
    fibonacci()