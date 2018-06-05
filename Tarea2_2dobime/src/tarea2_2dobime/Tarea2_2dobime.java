package tarea2_2dobime;

import java.util.Scanner;

public class Tarea2_2dobime {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Inicialización de varibles, para calcular el promedio total del arreglo 3
        double suma=0,promedio=0;
        //Aquí vamos a presentar la cabecera del reporte
        String[] cabecera = {"Arreglo1", "Arreglo2", "Resultado"};
        //Inicialización de arreglos a utilizarse, para la terminanción del programa
        double [] arreglo1 = {110, 220, 430, 140, 250, 460};
        double [] arreglo2 = {10, 20, 30, 40, 50, 60};
        //Se le asigna y inicializa el arreglo3,suma y promedio
        double [] arreglo3 = new double [6];
        double [] arre_suma = new double [6];
        double [] arre_promedio = new double [6];
        //Con este ciclo repetitivo vamos a ir calculando la divición del arreglo 1 y 2 y guardandolo en el arreglo3
        for (int cont=0; cont < arreglo1.length; cont ++){
            arreglo3[cont]= arreglo1[cont]/ arreglo2[cont];
            
        }                                   
        //Con este ciclo vamos a imprimir la cabecera del reporte
        for (int conta = 0; conta < cabecera.length; conta++) {
            System.out.printf("\t%s", cabecera[conta]);
        }
        //Vamos a presentar los diferentes valores del arreglo 1 y el arreglo 2
        for (int cont_1 = 0; cont_1 < arreglo3.length; cont_1++) {
            //Impresión de todos los valores del arreglo 1,2 y3.
            System.out.printf("\n\t%-17.2f%-17.2f%.2f\n", arreglo1[cont_1],arreglo2[cont_1], arreglo3[cont_1]);
        }
        //Con este ciclo vamos a calcular el promedio del arreglo 3 que nos pide 
        for (int cont_2 = 0; cont_2< arre_promedio.length; cont_2++) {
        suma =suma + arreglo3[cont_2];
        arre_suma [cont_2]=suma;
        promedio = arre_suma[cont_2] /6;
        arre_promedio[cont_2]=promedio;
        }
        //Empresión del promedio
        System.out.printf("\n\nPromedio arreglo3:%.2f", promedio);
    }

}
