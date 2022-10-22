using System.Diagnostics;
using System;
public class Sudo{
    public static void Main(){
        int[,] sudotest = new int[9,9]{    // ENTRADA 
            {0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0},           //ESTE ES UN TABLERO VACÍO
            {0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0},
            {0,0,0,0,0,0,0,0,0},
        };
        PRINT(sudotest);   //Para imprimir la entrada(array sin solucionar)
        System.Console.WriteLine();
        Stopwatch crono = new Stopwatch(); //Creo un cronómetro para ver cuánto demora la ejecución
        crono.Start(); //Inicio el cronómetro
        PRINT(Sudoku(sudotest, 0));     //Escribo la solución para el tablero introducido
        crono.Stop(); //Detengo el cronómetro
        System.Console.WriteLine(crono.Elapsed); //Escribo el tiempo que se ha demorado
    }
    private static bool Verificar(int fil, int col, int[,] board){
        // Este método recibe un tablero de sudoku y una fila y una columna
        // en dicha fil,col se ha introducido un nuevo número y se verifica
        // si es posible ubicarlo en dicha posición retornando true or false
        for (int i = 0; i < board.GetLength(0); i++)
        {
            // revisar si ese número no se repite en la fila ni en la columna
            if(i!=fil)
                if (board[i,col]==board[fil,col]) return false;
            if(i!=col)
                if(board[fil,i]==board[fil,col]) return false;
        }
        // obtener la posicion del "cuadrado" (sqrt(n),sqrt(n)) donde se encuentra el número
        //ubicado y verificar que no se repite ahí
        int value = (int)(Math.Sqrt(board.GetLength(0)));
        int filin = fil/value*value;
        int colin = col/value*value;
        for (int w = filin; w < filin+value; w++)
        {
            for (int e = colin; e < colin+value; e++)
                if(w!=fil&&e!=col)
                    if(board[fil,col]==board[w,e]) return false;
        }
        return true;
    }
    private static int[,] Sudoku(int[,] table, int iteration){
        if(iteration==table.Length) {
            //Si la cantidad de iteraciones llega a la cantidad máxima de espacios
            //del tablero entonces se retorna dicho tablero válido
            return table;}
        //obtener las filas y columna a partir de la iteración actual
        int fil = iteration/table.GetLength(0);
        int col = iteration%table.GetLength(0);
            
        for (int i = 1; i <= table.GetLength(0); i++)
        {
            if(table[fil,col]!=0) {
                //Si el número es diferente de 0 significa que es un valor prefijado
                //del sudoku recibido y no lo podemos cambiar, por tanto hacemos
                //el llamado a la siguiente iteracion
                return Sudoku(table,iteration+1);
            }
            table[fil,col]=i;
            // si la casilla está vacia le coloco un número
            if(Verificar(fil,col,table)){
                //compruebo si el número colocado es correcto
                var tempSol = Sudoku(table, iteration+1); 
                //Hago la siguiente iteración
                if (tempSol is not null)
                //Si se obtiene una respuesta válida la retorno
                    return tempSol;
            }
            //si el valor puesto en la casilla no es válido le vuelvo a colocar el 0
            //0 es equivalente a la casilla vacía
            table[fil,col]=0;
        }
        //si no se obtuvo solución válida retorno null
        return null;
    }
    private static void PRINT(int[,] mask){
        // Método para escribir un array bidimensional
        // en caso de ser null se escribe "null"
        if(mask==null){
            System.Console.WriteLine("null");
            return;
        }
        for (int p = 0; p < mask.GetLength(0); p++)
        {
            for (int o = 0; o < mask.GetLength(1); o++)
            {
                System.Console.Write(mask[p,o]+" ");
                
            }
            System.Console.WriteLine();
        }
    }
}