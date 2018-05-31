
import java.util.Scanner;

public class Ejemplo_2 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        double[] calificacion_progra = {18, 19, 15, 16, 17, 10};
        double[] calificacion_bd = {10, 12, 13, 20, 17, 20};
        double[] promedios = new double[6];
        
        System.out.println("------------------Reporte de calificaciones-------------");
        for (int cont = 0; cont < calificacion_bd.length; cont++) {
            double suma = calificacion_bd[cont] + calificacion_progra[cont];
            double promedio = suma / 2;
            promedios[cont] = promedio;
        }
        for (int cont_1 = 0; cont_1 < promedios.length; cont_1++) {
            System.out.printf("\nEstudiante%d:\t%.2f\t%.2f\t%.2f",cont_1+1,calificacion_progra[cont_1],calificacion_bd[cont_1],promedios[cont_1]);
        }
    }
}
