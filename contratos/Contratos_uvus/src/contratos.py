# -*- coding: utf-8 -*-
''' Examen de diciembre 18-19 Fundamentos de Programación (Python)

AUTOR: Mariano González
REVISORES: Carlos García, Fermín Cruz, Toñi Reina
ÚLTIMA MODIFICACIóN: 10/91/2019

################################################################
#  Datos del alumno
#
#  Nombre y apellidos: 
#  DNI: 
#  Grupo: 
################################################################

En este ejercicio trabajaremos sobre un dataset con información
sobre contratos de trabajo. 

Los datos se encuentran almacenados en un fichero en formato CSV.
Estas son las primeras líneas del fichero de entrada (fíjese en que
la primera línea es una cabecera con los nombres de las columnas):

    Numero SS,fecha,codigo,dias,horas,sueldo
    41347712,01/03/2014,77232,239,6,20.8
    75402883,28/07/2014,77232,363,4,24.5
    62583432,15/07/2014,12271,214,4,29.1
    62583432,16/04/2015,50323,324,5,15.7
    ...
            
Donde:
    número SS: número de la Seguridad Social del trabajador.
    Fecha: fecha del contrato.
    Código: código identificativo del campo de actividad del contrato.
    Día: número de días del contrato.
    Hora: número de horas de trabajo al día.
    Sueldo: sueldo bruto por hora.

En el fichero pueden existir distintos contratos para el mismo trabajador.
    
Implemente las funciones con los comentarios EJERCICIO Nº,
eliminando previamente la instrucción pass.
'''

import csv
from datetime import datetime
from matplotlib import pylab as plt
from anaconda_project.internal.conda_api import result
from collections import Counter




# EJERCICIO 1:
def lee_contratos(fichero):
    ''' Lee el fichero de entrada y devuelve una lista de tuplas.
    
        Cada línea del fichero de entrada contiene seis datos:
            número SS: número de la Seguridad Social del trabajador.
            Fecha: fecha del contrato.
            Código: código identificativo del campo de actividad del contrato.
            Día: número de días del contrato.
            Hora: número de horas de trabajo al día.
            Sueldo: sueldo bruto por hora.
            
        Hay que transformar ciertos elementos de la entrada en valores numóricos
        o de tipo fecha para que puedan ser procesados posteriormente.
        
        Para convertir una cadena de texto del estilo de '30/10/2007'
        en una fecha, utilice esta función: 
        fecha = datetime.strptime(fecha_en_cadena, '%d/%m/%Y').date()
        
    '''
    with open(fichero,'r',encoding='UTF-8') as f:
        lineas = csv.reader(f)
        next(lineas)
        result = [(x[0],datetime.strptime(x[1],'%d/%m/%Y').date(),x[2],
                   int(x[3]),int(x[4]),float(x[5])) for x in lineas]
    return result

# EJERCICIO 2
def trabajadores_contratados_actividad(contratos, codigo):
    ''' Recibe una lista de tuplas con la información sobre los contratos y
    el código de una actividad y devuelve un conjunto con los números de la
    Seguridad Social de los trabajadores con contrato en dicha actividad.
    '''
    result = {x[0] for x in contratos if x[2] == codigo}
    return result

# EJERCICIO 3
def dias_contrato_trabajador(contratos, numeroSS):
    ''' Recibe una lista de tuplas con la información sobre los contratos y
    el número de la Seguridad Social de un trabajador y devuelve el total de
    días de trabajo acumulados por los contratos del trabajador.
    '''
    suma = 0
    for x in contratos:
        if x[0] == numeroSS:
            suma += x[3]            
    return suma
                
# EJERCICIO 4
def trabajador_mas_dias(contratos):
    ''' Recibe una lista de tuplas con la información sobre los contratos,
    y busca el trabajador que acumula más días de contrato. Devuelve una tupla formada por
    el número de días totales y el número de la Seguridad Social del trabajador.
    En caso de empate a número de días, devuelve uno cualquiera de ellos.
    '''
    dias_acumulados = sorted([(dias_contrato_trabajador(contratos, x[0]),x[0]) for x in contratos], reverse = True)
    return dias_acumulados[0]
    
# EJERCICIO 5
def indexa_contratos_por_actividad(contratos):
    ''' Recibe una lista de tuplas con la información sobre los contratos,
    y devuelve un diccionario en el que las claves son los códigos de actividad
    y los valores asociados son listas con las tuplas correspondientes a
    la información sobre los 3 contratos con mayor duración en días de cada actividad. 
    
    Las listas asociadas a los códigos de actividad deben estar ordenadas
    de mayor a menor duración en días.    
    '''    
    dictporCodigo = indexa_codigo(contratos)
    res = max_contrato(dictporCodigo)
    return res

def indexa_codigo(contratos):
    result = dict()
    for contrato in contratos:
        if contrato[2] in result:
            result[contrato[2]].append(contrato)
        else:
            result[contrato[2]]=[contrato]
    return result

def max_contrato(dict_act):
    result = dict()
    for clave,valor in dict_act.items():
        result[clave] = sorted(valor,key = lambda x:x[3],reverse=True)[:3]
    return result
    
# EJERCICIO 6
def muestra_evolucion_contratos(contratos, codigo):
    ''' Recibe una lista de tuplas con la información sobre los contratos y
    el código de una actividad. Muestra una gráfica con la evolución a lo largo
    de los años del número de contratos de la actividad en cuestión.
    
    Para mostrar la gráfica use el siguiente código:
    
        plt.bar(range(len(numero_contratos)), numero_contratos, tick_label=anyos)
        plt.show()
    
    Debe calcular previamente las siguientes listas:
    
    - anyos: lista ordenada con los años DEL PERIODO COMPLETO para el que hay datos
    en la lista de contratos, ordenados crecientemente. Cada año debe aparecer una sola vez.
    Para obtener el año de una fecha f, utilize la expresión f.year
    - numero_contratos: lista con el número de contratos de la actividad dada
    en cada uno de los años de la lista anterior.
    '''
    
    anyos = sorted(list({x[1].year for x in contratos}))
    dic_cont_anyos = anyos_contados(contratos, codigo)
    numero_contratos = [dic_cont_anyos[x] for x in anyos]
    plt.bar(range(len(numero_contratos)), numero_contratos, tick_label=anyos)
    plt.show()
    
def anyos_contados(contratos,codigo):
    res = Counter()
    anyos = [x[1].year for x in contratos if x[2] == codigo]
    res.update(anyos)
    return res 
        
        
