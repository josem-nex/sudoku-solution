import math
import numpy as np


class Solution(object):
    def __init__(self, board=0):
        if Solution.IsValidTable(board):
            self.Sudo_Inicial = board
            self.Sudo_Solucion = Solution.SudoSolution(board)
        else:
            raise TypeError("board debe ser un tablero válido")

    def IsValidTable(board):
        """IsValidTable

        Args:
            board (int[][]): El tablero inicial
        Returns:
            bool: Verdadero si es un tablero válido, Falso en caso contrario.
        """
        if not isinstance(board, list):
            return False
        n = len(board)
        if not (math.floor(math.sqrt(n)) * math.floor(math.sqrt(n)) == n):
            return False
        return Solution.es_valido(board)
    
    
    def es_valido(board):
        """es_valido

        Args:
            board (int[][]): El tablero inicial

        Returns:
            bool: Verdadero si el tablero incial es válido, falso en caso contrario 
        """
        # Verificar que el tablero es una matriz cuadrada de 9x9
        if len(board) != 9 or any(len(fila) != 9 for fila in board):
            return False

        # Verificar que cada fila contenga números únicos del 1 al 9 o 0
        for fila in board:
            valores_validos = [False] * 10
            for valor in fila:
                if valor < 0 or valor > 9 or (valores_validos[valor] and valor != 0):
                    return False
                valores_validos[valor] = True

        # Verificar que cada columna contenga números únicos del 1 al 9 o 0
        for columna in range(9):
            valores_validos = [False] * 10
            for fila in range(9):
                valor = board[fila][columna]
                if valor < 0 or valor > 9 or (valores_validos[valor] and valor != 0):
                    return False
                valores_validos[valor] = True

        # Verificar que cada subcuadrícula de 3x3 contenga números únicos del 1 al 9 o 0
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                valores_validos = [False] * 10
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        valor = board[x][y]
                        if valor < 0 or valor > 9 or (valores_validos[valor] and valor != 0):
                            return False
                        valores_validos[valor] = True

        # Si todas las verificaciones pasaron, entonces el tablero es válido
        return True

    def IsValidPosition(fil, col, board):
        """IsValidPosition

        Args:
            fil (int): Representa la fila en la que se insertó el valor
            col (int): Representa la columna en la que se insertó el valor
            board (int[][]): El tablero actual del sudoku

        Returns:
            bool: Si es un valor válido o no el insertado en la posicion fil,col 
        """
        # Este método recibe un tablero de sudoku y una fila y una columna
        # en dicha fil,col se ha introducido un nuevo número y se verifica
        # si es posible ubicarlo en dicha posición retornando true or false
        for i in range(len(board)):
            # revisar si ese número no se repite en la fila ni en la columna
            if i != fil:
                if board[i][col] == board[fil][col]:
                    return False
            if i != col:
                if board[fil][i] == board[fil][col]:
                    return False
        # obtener la posicion del "cuadrado" (sqrt(n),sqrt(n)) donde se encuentra el número
        # ubicado y verificar que no se repite ahí
        value = int(len(board) ** 0.5)
        filin = (fil // value) * value
        colin = (col // value) * value
        for w in range(filin, filin + value):
            for e in range(colin, colin + value):
                if w != fil and e != col:
                    if board[fil][col] == board[w][e]:
                        return False
        return True

    def SudoSolution(board, iteration=0):
        """SudoSolution

        Args:
            board (int[][]): El tablero actual del sudoku
            iteration (int, optional): La iteración actual en la que estoy, la primera sería 0 y la última len(board)^2

        Returns:
            int[][]: Una solución correcta al tablero inicial recibido o null en caso de no ser posible.
        """
        # Si llegue a la ultima iteracion ya terminé con un tablero válido
        # me garantizo que es valido porque al poner cada valor ya verificaba que es válido.
        if iteration == len(board)*len(board):
            return board

        # obtengo la fila y la columna en la que estoy a partir de la iteración actual
        fil = iteration // len(board)
        col = iteration % len(board)

        for i in range(1, len(board) + 1):
            # si la posicion actual es diferente de 0 es xq es un valor prefijado y no lo puedo cambiar
            if board[fil][col] != 0:
                return Solution.SudoSolution(board, iteration + 1)
            # si no es 0 le doy un valor y lo pruebo
            board[fil][col] = i
            # si es un valor valido voy a la siguiente iteracion
            if Solution.IsValidPosition(fil, col, board):
                tempSol = Solution.SudoSolution(board, iteration + 1)
                if tempSol is not None:
                    return tempSol
            # si no es un valor válido lo pongo en 0 y repito con el siguiente valor
            board[fil][col] = 0
        return None