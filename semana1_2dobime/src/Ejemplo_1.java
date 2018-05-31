
import java.util.Scanner;

public class Ejemplo_1 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Inicialización de arreglo
        int[] a = {1, 2, 3, 4, 5, 6, 7};
        //Con está variable vamos a realizar la operación de multiplicación para la solución el programa
        int multi;
        //Con este ciclo repetitivo vamos a recorrer el arreglo
        for (int cont = 0; cont < a.length; cont++) {
            //Aquí se realizar la comperación para utilizar los numeros pares del arreglo 
            if (a[cont] % 2 == 0) {
                //Se imprime para que se diferencien cada tabla de multiplicación
                System.out.println("\n\nTablas de Multiplicar");
                //Con este ciclo vamos a llegar hasta 12, para la tabla y con el contador vamos a ir repitiendo de uno en uno
                for(int num=1; num<=12; num++){
                    //Operación de multiplicación
                    multi = a[cont]*num; 
                    //Se imprime la taba de multiplicación.
                    System.out.printf("\n%d %s %d %s %d",a[cont],"*",num,"=",multi);
                }
                
            }
            
        }

    }
}
