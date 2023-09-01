import sys
import typer
from rich.console import Console
from rich.prompt import Prompt

console = Console(color_system="windows")
# Reto #18
# TRES EN RAYA
# Fecha publicación enunciado: 02/05/22
# Fecha publicación resolución: 09/05/22
# Dificultad: DIFÍCIL

# Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
# - "X" si han ganado las "X"
# - "O" si han ganado los "O"
# - "Empate" si ha habido un empate
# - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
# Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.


class TicTacToe:
    """
        Análisis de la matriz 3x3 compuesta por X, O ó vacío
    """
    def __init__(self, input_board):
        self.input_board = input_board

    def check_board(self):
        self.input_board = self.input_board.replace("[", "").replace("],[", ",").replace("]", "").lower().split(",")
        self.input_board = [value.strip(' ') for value in self.input_board]
        if len(self.input_board) != 9:
            console.print("[red]El tamaño del tablero es incorrecto![/red]")
            return False

        count_x = 0
        count_o = 0

        for value in self.input_board:
            if value == "x":
                count_x += 1
            elif value == "o":
                count_o += 1

        if abs(count_x - count_o) > 1:
            console.print("[red]La cantidad de X u O es incorrecta![/red]")
            return False
        return True

    def win_or_draw(self):
        win_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]
        result = "empate"
        winner = None

        for win_row in win_combinations:
            if self.input_board[win_row[0]] != "" and self.input_board[win_row[0]] == self.input_board[win_row[1]] and self.input_board[win_row[0]] == self.input_board[win_row[2]]:
                winner = f"Ha ganado --> [green]{self.input_board[win_row[0]].upper()}[green]"
                result = self.input_board[win_row[0]]

                if result not in ["empate", "x", "o"]:
                    console.print("[red]Hay un error con los valores introducidos![/red]")
                    return None
        console.print(f"El resultado es: [bold]{winner}[/bold]" if winner is not None else f"El resultado es: [bold]{result}[/bold]")


def main():
    input_board = Prompt.ask("Introduzca la matriz de TicTacToe a verificar, por ejemplo:\n[X, O, X],\n[, X, ],\n[O, O, X]\n y presione ENTER (q --> Exit)")
    if input_board == "q":
        sys.exit("Proceso finalizado!")

    board = TicTacToe(input_board)
    result = board.check_board()
    if not result:
        sys.exit()

    board.win_or_draw()


if __name__ == '__main__':
    typer.run(main)
