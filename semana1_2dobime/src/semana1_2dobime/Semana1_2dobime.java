
package semana1_2dobime;

import java.util.Scanner;

public class Semana1_2dobime {

    public static void main(String[] args) {
       Scanner entrada = new Scanner(System.in);
       //Inicialización de variables para el arreglo 
       int [] c = new int [4];
       //Se está dando un valor en específico al arreglo 
       c[0]=10;
        //Con este contador se va recorreindo el arreglo para que lo imprima
        for (int contador=0 ; contador < c.length ; contador++){
            System.out.println(c[contador]);
        }
    }
    
}
