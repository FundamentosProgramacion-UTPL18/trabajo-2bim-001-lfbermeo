package tarea1_2dobime;

import java.util.Scanner;

public class Tarea1_2dobime {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        //utilización de estás variables para realizar los cálculos para la solución del problema
        double suma = 0, promedio = 0, suma_to = 0;
        //Utilización de arreglos para la impresión del resultado del programa, tanto cadenas como valores decimales
        String[] meses = {"Agosto", "Octubre", "Diciembre", "Total", "Promedio"};
        String[] sucursales = {"Sucursal 1", "Sucursal 2", "Sucursal 3", "Sucursal 4"};
        double[] ventas_mes_1 = {4500.2, 5500.2, 6500.2, 2500.1};
        double[] ventas_mes_2 = {1500.2, 2500.2, 3500.2, 1500.1};
        double[] ventas_mes_3 = {2300.2, 1200.2, 4700.2, 3200.1};

        double[] venta_total_sucursal = new double[4];
        double[] venta_promedio_sucursal = new double[4];
        //Con es te ciclo repetitivo vamos ir calculando los valores que necesitamos para la solución del problema 
        for (int cont = 0; cont < ventas_mes_1.length; cont++) {
            //operación para calcular el valor total de las ventas y se le asigna al valor declarado del arreglo para que vaya recorriendo con el contador 
            suma = ventas_mes_1[cont] + ventas_mes_2[cont] + ventas_mes_3[cont];
            venta_total_sucursal[cont] = suma;
            //En está operación vamos a calcular el promedio de cada una de las sucursales y se le asigna al valor declarado del arreglo para que vaya recorriendo con el contador  
            promedio = suma / 3;
            venta_promedio_sucursal[cont] = promedio;
            //En está operación vamos a calcular la cantidad total de las 4 sucursales y se le asigna al valor declarado del arreglo para que vaya recorriendo con el contador 
            suma_to = suma_to + promedio;
            venta_total_sucursal[cont] = suma_to;

        }
        //Impresión del encabezado del reporte
        System.out.println("\nReporte");
        for (int conta = 0; conta < meses.length; conta++) {
            System.out.printf("\t\t%s", meses[conta]);
        }
        //Con este ciclo vamos ir recorriendo para que se impriman los valores asignados
        for (int cont_1 = 0; cont_1 < venta_promedio_sucursal.length; cont_1++) {
            //Impresión de todos los valores tanto en ventas como sumas y promedios.
            System.out.printf("\n%s\t%.2f\t\t%.2f\t\t%.2f\t\t%-25.2f%-25.2f", sucursales[cont_1], ventas_mes_1[cont_1], ventas_mes_2[cont_1], ventas_mes_3[cont_1], venta_total_sucursal[cont_1], venta_promedio_sucursal[cont_1]);

        }
        //Aquí se imprimirá la suma total de todas las sucrusales fuera de los ciclos repetitivos
        System.out.printf("\n\nTotales de ventas de todas la sucursales es:%.2f", suma_to);
    }
}
