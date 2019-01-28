# -*- coding: utf-8 -*-
'''
Created on 10 dic. 2018

@author: alfonso.bengoa
'''
import csv
from math import pi
from matplotlib import pyplot as plt
from collections import namedtuple
from collections import Counter
from zope.interface.declarations import named

'''
    Tomaremos los datos de un fichero de entrada llamado moluscos.csv
     en el que se encuentran distintas mediciones de una especie de moluscos (abalones, también conocidos como _orejas de mar). 
     El fichero se encuentra en la carpeta /csv
      Cada línea del fichero de entrada se corresponde con la medición de un molusco y contiene seis informaciones:

        - sexo: M (masculino), F (femenino), I (infante)
        - longitud de la concha
        - diámetro de la concha
        - altura de la concha
        - peso del cuerpo
        - edad en años
    He aquí un fragmento con las primeras líeas del fichero de entrada:,
        sexo,longitud,diametro,altura,peso,edad,
            M,0.455,0.365,0.095,0.514,15,
            M,0.35,0.265,0.09,0.2255,7,
            F,0.53,0.42,0.135,0.677,9,
            M,0.44,0.365,0.125,0.516,10,
            I,0.33,0.255,0.08,0.205,7,
'''
Molusco = namedtuple('Molusco','sexo longitud diametro altura peso edad')
# 1. Consulta y filtrado (2.75 puntos)
#Ejercicio 1
def lee_moluscos(fichero):
    '''
    Lee el fichero de entrada y devuelve una lista de medidas de moluscos
    ENTRADA:
       - fichero: nombre del fichero de entrada
    SALIDA:
       - lista de medidas -> [(int, int, int, float, float, float, int)]
    
    Cada línea del fichero se corresponde con un molusco, y se representa,
    con una tupla con los siguientes valores:
       - sexo: M (masculino), F (femenino), I (infante)
       - longitud de la concha
       - diámetro de la concha
       - altura de la concha
       - peso del cuerpo
       - edad en años
    Tenga cuidado en cargar en la lista cada valor con el tipo que se indica
    '''
    with open(fichero,'r',encoding = 'UTF-8') as f:
        lineas = csv.reader(f)
        next(lineas)
        result = [Molusco(sexo,float(long),float(diam),float(alt),float(peso),int(edad)) for sexo,long,diam,alt,peso,edad in lineas]
    return result

# 2. Consulta y filtrado (7.25 puntos)
#Ejercicio 2
def numero_ejemplares_por_sexo(medidas):
    ''' Calcula el n�mero de ejemplares por sexo presentes en la colección
    ENTRADA:,
       - medidas: lista de medidas -> [(str, float, float, float,float, int)]
    SALIDA:
       - diccionario de frecuencias por sexi -> {str: int}
    
    Toma como entrada una lista de tuplas de medidas. Produce como salida un
    diccionario cuyas claves son los posibles sexos ('M', 'F', 'I') y los valores
    son el número de ejemplares de cada sexo.
    '''
    result = Counter()
    dict_por_sexo = [medida.sexo for medida in medidas]
    result.update(dict_por_sexo)
    return result
    
            
#Ejercicio 3.1
def volumen_estimado(longitud, diametro, altura):
    ''' Estimación del volumen a partir de longitud, diámetro y altura
        el volumen se estima como PI (utilice la constante python 'pi' que
        verá importada en las primeras líneas de este módulo), por el producto de 
        la longitud, el diámetro y la semi-altura
    '''
    return pi*longitud * diametro * (altura/2)

#Ejercicio 3.2
def filtra_por_volumen(medidas, min_volumen, max_volumen):
    ''' 
    Selecciona tuplas de medidas en función del volumen estimado
    ENTRADA:
       - medidas: lista de medidas -> [(int, int, int, float, float, float, int)]
       - min_volumen: límite inferior del volumen -> float
       - max_volumen: límite superior del volumen -> float
    SALIDA:
       - lista de medidas seleccionadas -> [(int, int, int, float, float, float, int)]
    
    Toma como entrada una lista de tuplas de medidas, y produce como
    salida otra lista de tuplas en la que solo se incluyen aquellas cuyo
    volumen estimado se encuentra entre min_volumen y max_volumen (ambos incluidos).
    '''
    result = [medida for medida in medidas if min_volumen <= volumen_estimado(medida.longitud, medida.diametro, medida.altura) <= max_volumen]  
    return result
#Ejercicio 4
def agrupa_por_volumen(medidas, rangos):
    ''' Crea un diccionario de medidas indexado por rangos de volúmenes
    ENTRADA:
       - medidas: lista de medidas -> [(int, int, int, float, float, float, int)]
       - rangos: listado de rangos de volúmenes -> [(float,float)]
    SALIDA:
       - diccionario indexado por rangos -> {(float, float): [(int, int, int, float, float, float, int)]}
    
    Toma como entrada una lista de tuplas de medidas y una lista de rangos de 
    volúmenes. Cada rango de volumen se determina con una tupla con los límites
    inferior y superior del rango. Por ejemplo, una posible lista de rangos es:
        [(0.0,0.05), (0.05,0.1), (0.1,0.15), (0.15,0.2)]
    
    Produce como salida un diccionario cuyas claves son cada uno de los rangos
    y los valores serán las listas de tuplas de medidas cuyo volumen está dentro
    de cada rango.
    '''
    result = dict()
    for rango in rangos:
        valor = filtra_por_volumen(medidas, rango[0], rango[1])  
        if rango in result:
            result[rango].append(valor) 
        else:
            result[rango] = valor    
    return result
#Ejercicio 5
def muestra_puntos_longitud_diametro(medidas):
    ''' Genera una diagrama de puntos con la distribución por sexo
    ENTRADA:
       - medidas: lista de medidas -> [Medida(int, int, int, float, float, float, int)]
    SALIDA EN PANTALLA:
       - diagrama de puntos con un color distinto para cada uno de los tres sexos.
       
    Toma como entrada una lista de tuplas de medidas y genera un diagrama de puntos
    (longitud,diamentro) usando un color distinto para cada uno de los tres sexos
    presentes en la colección.
    
   Debe usar las siguientes instrucciones matplotlib para generar el diagrama
    de puntos:
        plt.scatter(longitudes_M, diametros_M, color='blue', marker='.')
        plt.scatter(longitudes_F, diametros_F, color='red', marker='.')
        plt.scatter(longitudes_I, diametros_I, color='green', marker='.')
        plt.show()
    
    Para generar el diagrama es necesario construir previamente las siguientes listas:
        longitudes_M: longitudes de los moluscos de sexo 'M'
        diametros_M: diametros de los moluscos de sexo 'M'
        longitudes_F: longitudes de los moluscos de sexo 'F'
        diametros_F: diametros de los moluscos de sexo 'F'
        longitudes_I: longitudes de los moluscos de sexo 'I'
        diametros_I: diametros de los moluscos de sexo 'I
    '''
    longitudes_M = [medida.longitud for medida in medidas if medida.sexo == 'M']
    diametros_M = [medida.diametro for medida in medidas if medida.sexo == 'M']
    longitudes_F = [medida.longitud for medida in medidas if medida.sexo == 'F']
    diametros_F = [medida.diametro for medida in medidas if medida.sexo == 'F']
    longitudes_I = [medida.longitud for medida in medidas if medida.sexo == 'I']
    diametros_I = [medida.diametro for medida in medidas if medida.sexo == 'I']
    plt.scatter(longitudes_M, diametros_M, color='blue', marker='.')
    plt.scatter(longitudes_F, diametros_F, color='red', marker='.')
    plt.scatter(longitudes_I, diametros_I, color='green', marker='.')
    plt.show()
