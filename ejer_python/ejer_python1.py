valores = {

"Estudiante 1": {'notas':[10,10,3], 'carrera': 'Sistemas', 'edad': 20},
"Estudiante 2": {'notas':[10,9,3], 'carrera': 'Electronica', 'edad': 19},
"Estudiante 3": {'notas':[9,10,3], 'carrera': 'Contabilidad', 'edad': 18},
"Estudiante 4": {'notas':[8,9,4], 'carrera': 'Sistemas', 'edad': 20},
"Estudiante 5": {'notas':[8,8,5], 'carrera': 'Electronica', 'edad': 19},
"Estudiante 6": {'notas':[3,10,6], 'carrera': 'Contabilidad', 'edad': 18},
"Estudiante 7": {'notas':[2,8,7], 'carrera': 'Sistemas', 'edad': 20},
"Estudiante 8": {'notas':[1,9,3], 'carrera': 'Economia', 'edad': 20},
"Estudiante 9": {'notas':[9,10,2], 'carrera': 'Sistemas', 'edad': 19},

}
#inicialización de variables, que se hará uso
cont_contabilidad=0
cont_sistemas=0
cont_electrónica=0
cont_economia=0
suma_edad=0
#con este ciclo vamos a recorrer el diciionario completo separando lso datos del Estudiante 1,2.... y cada uno de sus datos
for estudiante,datos in valores.items():
	#se le asigna a notas el valor "notas" del diccionario principal
	notas =datos['notas']
	suma = 0
	#Con este ciclo vamos a calcular el promedio de cada uno de los 9 estudiantes
	for nota in notas:
		#operaciones para calcular el promedio
	  suma = suma + nota
	  #Con la función len nos indicará el tamaño de arreglo de cada uno de los estudiantes
	promedio = suma / len(notas)
	#Se imprimirá el promedio de los 9 estudiantes
	print ("%s tiene promedio %.2f" %(estudiante,promedio))  
#Con este ciclo decomparación vamos a ir comparando si es de sistemas, eletrónica.... y vamos a colocandole un contador para que pueda ir contando de uno en uno 
	if (datos["carrera"]=="Sistemas"):
		cont_sistemas=cont_sistemas+1
	elif(datos["carrera"]=="Electronica"):
		cont_electrónica=cont_electrónica+1	
	elif(datos["carrera"]=="Contabilidad"):
		cont_contabilidad=cont_contabilidad+1
	elif(datos["carrera"]=="Economia"):
		 cont_economia=cont_economia+1
		 #Caculamos la suma de las edades, buscandoles en el diccionario edad que está asignada
	suma_edad=suma_edad+datos["edad"]
#Imprimimos el número de estudiantes de cada carrera  
print ("%d estudiante de Sistemas" % (cont_sistemas))					
print ("%d estudiante de Electronica" % (cont_electrónica))	
print ("%d estudiante de Contabilidad" % (cont_contabilidad))	
print ("%d estudiante de Economia" % (cont_economia))
#Calculamos el promedio de edades	
promedio_e=suma_edad/len(valores)
#imprimimos el promedio de las edades 
print ("El promedio de edades de los estudiantes es: %d"%(promedio_e))
	 	