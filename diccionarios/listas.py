#Diccionario Entrenadores
datos = {
    u'Alemania': {
        'entrenador': {
            'edad': u'58',
            'nombre': u'LOEW Joachim'
        }
    },
    u'Arabia Saudi': {
        'entrenador': {
            'edad': u'50',
            'nombre': u'PIZZI Juan Antonio'
        }
    },
    u'Argentina': {
        'entrenador': {
            'edad': u'58',
            'nombre': u'SAMPAOLI Jorge'
        }
    },
    u'Australia': {
        'entrenador': {
            'edad': u'66',
            'nombre': u'VAN MARWIJK Bert'
        }
    },
    u'Brasil': {
        'entrenador': {
            'edad': u'57',
            'nombre': u'TITE'
        }
    },
    u'Belgica': {
        'entrenador': {
            'edad': u'44',
            'nombre': u'MARTINEZ Roberto'
        }
    },
    u'Colombia': {
        'entrenador': {
            'edad': u'68',
            'nombre': u'PEKERMAN Jose'
        }
    },
    u'Costa Rica': {
        'entrenador': {
            'edad': u'53',
            'nombre': u'RAMIREZ Oscar'
        }
    },
    u'Croacia': {
        'entrenador': {
            'edad': u'51',
            'nombre': u'DALIC Zlatko'
        }
    },
    u'Dinamarca': {
        'entrenador': {
            'edad': u'64',
            'nombre': u'HAREIDE Age'
        }
    },
    u'Egipto': {
        'entrenador': {
            'edad': u'62',
            'nombre': u'CUPER Hector'
        }
    },
    u'Espana': {
        'entrenador': {
            'edad': u'50',
            'nombre': u'HIERRO Fernando'
        }
    },
    u'Francia': {
        'entrenador': {
            'edad': u'49',
            'nombre': u'DESCHAMPS Didier'
        }
    },
    u'Inglaterra': {
        'entrenador': {
            'edad': u'47',
            'nombre': u'SOUTHGATE Gareth'
        }
    },
    u'Islandia': {
        'entrenador': {
            'edad': u'51',
            'nombre': u'HALLGRIMSSON Heimir'
        }
    },
    u'Japon': {
        'entrenador': {
            'edad': u'63',
            'nombre': u'NISHINO Akira'
        }
    },
    u'Marruecos': {
        'entrenador': {
            'edad': u'49',
            'nombre': u'RENARD Herve'
        }
    },
    u'Mexico': {
        'entrenador': {
            'edad': u'57',
            'nombre': u'Juan CARLOS OSORIO'
        }
    },
    u'Nigeria': {
        'entrenador': {
            'edad': u'64',
            'nombre': u'ROHR Gernot'
        }
    },
    u'Panama': {
        'entrenador': {
            'edad': u'62',
            'nombre': u'GOMEZ Hernan'
        }
    },
    u'Peru': {
        'entrenador': {
            'edad': u'60',
            'nombre': u'GARECA Ricardo'
        }
    },
    u'Polonia': {
        'entrenador': {
            'edad': u'60',
            'nombre': u'NAWALKA Adam'
        }
    },
    u'Portugal': {
        'entrenador': {
            'edad': u'63',
            'nombre': u'SANTOS Fernando'
        }
    },
    u'RI de Iran': {
        'entrenador': {
            'edad': u'65',
            'nombre': u'QUEIROZ Carlos'
        }
    },
    u'Republica de Corea': {
        'entrenador': {
            'edad': u'47',
            'nombre': u'SHIN Taeyong'
        }
    },
    u'Rusia': {
        'entrenador': {
            'edad': u'54',
            'nombre': u'CHERCHESOV Stanislav'
        }
    },
    u'Senegal': {
        'entrenador': {
            'edad': u'42',
            'nombre': u'CISSE Aliou'
        }
    },
    u'Serbia': {
        'entrenador': {
            'edad': u'44',
            'nombre': u'KRSTAJIC Mladen'
        }
    },
    u'Suecia': {
        'entrenador': {
            'edad': u'55',
            'nombre': u'ANDERSSON Janne'
        }
    },
    u'Suiza': {
        'entrenador': {
            'edad': u'54',
            'nombre': u'PETKOVIC Vladimir'
        }
    },
    u'Tunez': {
        'entrenador': {
            'edad': u'55',
            'nombre': u'MAALOUL Nabil'
        }
    },
    u'Uruguay': {
        'entrenador': {
            'edad': u'71',
            'nombre': u'TABAREZ Oscar'
        }
    }
}
diccionario_confederaciones = {'Alemania': {'confederacion': 'UEFA'},

 'Arabia Saudi': {'confederacion': 'AFC'},

 'Argentina': {'confederacion': 'CONMEBOL'},

 'Australia': {'confederacion': 'AFC'},

 'Belgica': {'confederacion': 'UEFA'},

 'Brasil': {'confederacion': 'CONMEBOL'},

 'Colombia': {'confederacion': 'CONMEBOL'},

 'Costa Rica': {'confederacion': 'Concacaf'},

 'Croacia': {'confederacion': 'UEFA'},

 'Dinamarca': {'confederacion': 'UEFA'},

 'Egipto': {'confederacion': 'CAF'},

 'Espana': {'confederacion': 'UEFA'},

 'Francia': {'confederacion': 'UEFA'},

 'Inglaterra': {'confederacion': 'UEFA'},

 'Islandia': {'confederacion': 'UEFA'},

 'Japon': {'confederacion': 'AFC'},

 'Marruecos': {'confederacion': 'UEFA'},

 'Mexico': {'confederacion': 'Concacaf'},

 'Nigeria': {'confederacion': 'CAF'},

 'Panama': {'confederacion': 'Concacaf'},

 'Peru': {'confederacion': 'CONMEBOL'},

 'Polonia': {'confederacion': 'UEFA'},

 'Portugal': {'confederacion': 'UEFA'},

 'RI de Iran': {'confederacion': 'AFC'},

 'Republica de Corea': {'confederacion': 'AFC'},

 'Rusia': {'confederacion': 'UEFA'},

 'Senegal': {'confederacion': 'CAF'},

 'Serbia': {'confederacion': 'UEFA'},

 'Suecia': {'confederacion': 'UEFA'},

 'Suiza': {'confederacion': 'UEFA'},

 'Tunez': {'confederacion': 'CAF'},

 'Uruguay': {'confederacion': 'CONMEBOL'}}
diccionario_confederaciones_entrenadores= {'CONMEBOL':[], 'UEFA':[], 'AFC':[], 'Concacaf':[],'CAF':[]}
#Inicialización de suma
suma=0
#Con este reporte 2 vamos a presentar cada uno de los nombres y las edades de los entrenadores por confederaciones
reporte2="REPORTE 2"
#Aquí imprimimos el encabezado del primer reporte
print("Entrenador \t\t\t Edad\n")
#Vamos a recorrer todo el diccionario grande de datos,
for i  in datos.keys():
    #asignamos variables a los datos del diccionario mayor,para utilizarlo en nuestros calculos
    mundial = datos[i]
    nombre = mundial["entrenador"]
    #En el diccionario principal está declarado eddad como cadena aquí vamos cambiarlo a entero
    edades=int(nombre["edad"])
    nombres=nombre["nombre"]
    #Con este print vamos a presentar los nombres y las edades de los diferentes entrenadores
    print("%-35s%s"%(nombre["nombre"],edades)) 
    #Realizamos la operación suma de todas las edades de los entrenadores
    suma = suma +edades
    #Al Diccionario_confederaciones les vamos asignar confederacion con datos del  entrenador  con lista vacia para asignarle valores
    diccionario_confederaciones_entrenadores[diccionario_confederaciones[i]['confederacion']].append(nombre)
#Calculo del promedios con toda la suma de las edades y dividiendole a cantidades de datos con la opción de python "LEN"    
promedio =suma /len(datos)
#Impresión del promedio total de las edades
print("El promedio de edades del  mundial es \t%d\n\n\n" % (promedio))
print("---------------------------------------------------------------------------------------------------")
#Con este ciclo vamos a ir recorriendo el diccionario_confederaciones_entrenadores
for i in diccionario_confederaciones_entrenadores.keys():
    #Inicializacion de suma para el calculo del promedio de edades por confederaciones
    suma_confe=0
    #Le vamos agregando a nuestra concatenación de cadena los datos del diccionario_confe...
    reporte2+=("\n%s\n\n"%(i))
    #Con este ciclo vamos recorriendo el diccionario_confe...
    for d in diccionario_confederaciones_entrenadores[i]:
        #Calculo de suma de edades por confederaciones
        suma_confe=suma_confe+ int(d["edad"])
        #Añadimos a la concatenación de cadenas los datos de nombre y edad de cada uno de los entrenadores por confederaciones
        reporte2+=("%-40s  %s\n"%(d['nombre'],d['edad']))
    #Calculo para el promedio de edad por confederaciones, utilizando la opción de python len, para saber el tamaño de los datos    
    prome_confe = suma_confe/ len(diccionario_confederaciones_entrenadores[i])
    #Añadimos al reporte2, el promedio de edades por confederaciones
    reporte2+=("\nPromedio de edades por confederacion:\t%.2d\n" % (prome_confe))
#impresión de reporte final    
print(reporte2)

