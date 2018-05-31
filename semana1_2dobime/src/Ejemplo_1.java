
import java.util.Scanner;

public class Ejemplo_1 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int[] a = {1, 2, 3, 4, 5, 6, 7};
        int multi;
        for (int cont = 0; cont < a.length; cont++) {
            if (a[cont] % 2 == 0) {
                System.out.println("\n\nTablas de Multiplicar");
                for(int num=1; num<=12; num++){
                    multi = a[cont]*num; 
                    System.out.printf("\n%d %s %d %s %d",a[cont],"*",num,"=",multi);
                }
                
            }
            
        }

    }
}
