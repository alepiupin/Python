'''
Created on 22 ene. 2019

@author: alejandro
'''
import csv
from collections import namedtuple
from matplotlib import pylab as plt

Bicicleta = namedtuple('Bicicleta', 'mes dia hora temperatura humedad viento alquiladas')

def leer_fichero(ruta):
    with open(ruta,'r',encoding='UTF-8') as f:
        linea = csv.reader(f)
        next(linea)
        result = [Bicicleta(int(x[0]),int(x[1]),int(x[2]),float(x[3]),float(x[4]),
                            float(x[5]),int(x[6])) for x in linea]
    return result

def suma_alquiladas(registros):
    return sum([x.alquiladas for x in registros])

def proporcion_fin_de_semana(registros):
    bicicleta_fin_semana = sum([x.alquiladas for x in registros if x.dia == 0 or x.dia == 6])
    return bicicleta_fin_semana/suma_alquiladas(registros)

def filtra_por_meses(registros,meses):
    result = [x for x in registros if x.mes in meses]
    return  result

def agrupa_por_dias(registro):
    result = dict()
    for x in registro:
        if x.dia in result:
            result[x.dia].append(x)
        else:
            result[x.dia] = [x]
    return result