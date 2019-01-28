'''
Created on 8 ene. 2019

@author: jorge
'''

import csv
from collections import namedtuple
from matplotlib import pylab as plt

Registro = namedtuple(
    'Registro', 'mes dia hora temperatura humedad viento alquiladas')


def lee_bicicletas(fichero):
    ''' Lee el fichero de entrada y devuelve una lista de tuplas
    
    ENTRADA:
       - fichero: nombre del fichero de entrada
    SALIDA:
       - lista de registros -> [Registro(int, int, int, float, float, 
       float, int)]
    
    Cada línea del fichero de entrada contiene siete informaciones
    relativas a la fecha, hora, condiciones meteorológicas y número
    de bicicletas alquiladas:
       - mes: de 1 a 12
       - dia: de 0 (domingo) a 6 (sábado)
       - hora: de 0 a 23
       - temperatura: temperatura del aire
       - humedad: humedad relativa
       - viento: velocidad del viento
       - alquiladas: número de bicicletas alquiladas
    Hay que transformar ciertos elementos de la entrada en valores numéricos
    para que puedan ser procesados posteriormente.
    '''
    result = []
    with open(fichero, "r", encoding="UTF-8") as f:
        lineas = csv.reader(f)
        next(lineas)
        for linea in lineas:
            mes = int(linea[0])
            dia = int(linea[1])
            hora = int(linea[2])
            temperatura = float(linea[3])
            humedad = float(linea[4])
            viento = float(linea[5])
            alquiladas = int(linea[6])
            result.append(
                Registro(
                    mes, dia, hora,
                    temperatura, humedad, viento,
                    alquiladas))
    return result


def proporcion_fin_de_semana(registros):
    ''' Proporcion de bicicletas alquiladas los fines de semana
    
    ENTRADA:
       - registros: lista de registros -> 
       [Registro(int, int, int, float, float, float, int)]
    SALIDA:
       - proporcion de bicicletas alquiladas 
       -> float

    Toma como entrada una lista de tuplas 
    de registros y calcula qué proporción
    de bicicletas se alquila 
    durante los fines de semana:
    '''
    result = [r.alquiladas 
              for r 
              in registros 
              if r.dia == 0 or r.dia == 6]
    return sum(result) / suma_alquiladas(registros)


def suma_alquiladas(registros):
    alquiladas = [r.alquiladas for r in registros]
    return sum(alquiladas)


def filtra_por_meses(registros, meses):
    ''' Selecciona registros por meses
    
    ENTRADA:
       - registros: lista de registros -> 
       [Registro(int, int, int, float, float, float, int)]
       - meses: lista de meses a seleccionar -> 
       [int]
    SALIDA:
       - registros seleccionados -> [Registro(int, int, int, float, float, float, int)]

    Toma una lista de registros y una lista de meses,
     y selecciona
    solo los registros de los meses indicados
    '''
    result = [r for r in registros 
              if r.mes in meses]
    return result


def agrupa_por_dias(registros):
    ''' Crea un diccionario de registros 
    indexado por días
    
    ENTRADA:
       - registros: lista de registros -> [Registro(int, int, int, float, float, float, int)]
    SALIDA:
       - diccionario con listas de registros por día -> {str: [Registro(int, int, int, float, float, float, int)]}

    Toma como entrada una lista de registros, 
    y produce como
    salida un diccionario cuyas claves son los días. Los valores
    del diccionario son listas de registros correspondientes
    a cada día.
    
    La solución debe ser genérica y 
    adaptarse a los datos que
    se reciben como parámetro para calcular 
    el conjunto de claves del
    diccionario.
    '''
    result = dict()
    for registro in registros:
        if(str(registro.dia) in result):
            result[str(registro.dia)]+=[registro]
        else:
            result[str(registro.dia)]=[registro]
    return result














