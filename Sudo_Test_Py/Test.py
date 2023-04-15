import numpy as np
import math
import time
import Sudo_Solution as SS
import random


def main():
    # matriz de 9x9 vacía (ceros)
    sudotest = [[0 for i in range(9)] for j in range(9)]
    #aqui puedes poner cualquier test
    test=[  [0,8,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,4,0,0],
            [0,0,3,0,0,0,0,0,0],
            [0,0,0,0,0,2,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,7,0,0,0,0],
            [0,0,0,0,0,0,0,4,0],
            [0,3,0,0,9,0,0,0,0]]
    # imprimo el test antes de darle solucion
    print_board(test)
    # le doy solucion y lo imprimo
    x = SS.Solution(test)
    print_board(x.Sudo_Solucion)
    


def print_board(mask):
    # Método para escribir un array bidimensional
    # en caso de ser None se escribe "None"
    if mask is None:
        print("None")
        return
    for p in range(len(mask)):
        for o in range(len(mask[0])):
            print(mask[p][o], end=" ")
        print()
    print()





main()
