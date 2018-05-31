
import java.util.Scanner;

public class Ejemplo_2 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Declaramos las varaibles para la utilización del porgrama y les asignamos valores a variable calificación progra y calificación bd
        double[] calificacion_progra = {18, 19, 15, 16, 17, 10};
        double[] calificacion_bd = {10, 12, 13, 20, 17, 20};
        double[] promedios = new double[6];
        
        System.out.println("------------------Reporte de calificaciones-------------");
        //Con este ciclo repetitivo vamos a ir recorreindo cada uno de los valores asigandos a calificación progra y calificacción base de datos
        for (int cont = 0; cont < calificacion_bd.length; cont++) {
            //Realizamos la operación de suma y promedio, haciendo uso del contador que va recorriendo cado uno de los varoles asignados
            double suma = calificacion_bd[cont] + calificacion_progra[cont];
            double promedio = suma / 2;
            promedios[cont] = promedio;
        }
        //Con este ciclo vamos ir recorriendo para que se impriman los valores asignados
        for (int cont_1 = 0; cont_1 < calificacion_progra.length; cont_1++) {
            //Realizamos la impresión del reporte tomando en cuenta las posiciones que las vamos recorriendo con el contador_1 e imprimimos con sus respectivas asignaciones y tabuladores.
            System.out.printf("\nEstudiante%d:\t%.2f\t%.2f\t%.2f",cont_1+1,calificacion_progra[cont_1],calificacion_bd[cont_1],promedios[cont_1]);
        }
    }
}
