# SudokuSolution
El objetivo del sudoku es rellenar una cuadrícula de 9 × 9 celdas (81 casillas) dividida en subcuadrículas de 3 × 3 (también llamadas "cajas" o "regiones") con las cifras del 1 al 9 partiendo de algunos números ya dispuestos en algunas de las celdas. La forma inicial del juego es que sean nueve elementos diferenciados, que no se deben repetir en una misma fila, columna o subcuadrícula. Un sudoku bien planteado sólo puede tener una solución, y ha de tener al menos 17 pistas iniciales. La solución de un sudoku siempre es un cuadrado latino, aunque el recíproco en general no es cierto ya que el sudoku establece la restricción añadida de que no se puede repetir un mismo número en una subcuadrícula.
# Implementation
Entrada: 
-Un array bidimensional de enteros que representa el tablero. Tiene la forma NxN donde N es cuadrado perfecto.
-Un número correspondiente a la iteración actual, el cuál en el primer llamado es 0.
Seria de la forma:
```cs
    static int[,] Sudoku(int[,] table, int iteration){
        //código implementado
        return table;
    }
```

Salida: Un array bidimensional que representa la solución válida al tablero recibido, en caso de no tener solución devuelve null.

# Ejemplo:
Entrada:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/300px-Sudoku-by-L2G-20050714.svg.png)

Salida:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Sudoku_resuelto_completo.png/300px-Sudoku_resuelto_completo.png)
