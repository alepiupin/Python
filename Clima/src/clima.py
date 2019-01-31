# -*- coding: utf-8 -*-
''' Análisis de datos climáticos

AUTOR: José A. Troyano
REVISOR: Mariano González, Carlos G. Vallejo
ÚLTIMA MODIFICACIÓN: 22/12/2018

La información meteorológica es una fuente continua de datos que de forma
gratuita es distribuida por distintos servicios (tanto las predicciones como
las medidas reales). En este proyecto vamos a trabajar con datos meteorológicos
históricos. A partir de ellos generaremos distintas funciones de consulta y
visualización que permitirán, entre otras cosas, seleccionar datos de distintos
períodos, mostrar gráficas que resuman las mediciones tomadas en esos períodos,
y determinar la evolución de los patrones climáticos durante distintos períodos.

Trabajaremos con ficheros en formato CSV. Cada registro del fichero de entrada
ocupa una línea y contiene cuatro datos correspondientes a la información
meteorológica de un determinado día (fecha, precipitación, temperatura máxima,
temperatura mínima). Estas son las primeras líneas de un fichero de entrada:
    DATE,PRCP,TMAX,TMIN
    1951-01-01,1.0,9.0,-0.8
    1951-01-02,35.4,8.4,4.4
    1951-01-03,0.0,7.0,1.2
    1951-01-04,0.0,7.6,-2.4
    1951-01-05,0.0,10.6,0.0
    1951-01-06,0.0,10.0,-1.4
    1951-01-07,0.0,12.0,0.0
    1951-01-08,0.0,9.0,3.0

FUNCIONES DISPONIBLES:
----------------------
- lee_registros(fichero):
    lee el fichero de entrada y devuelve una lista de registros
- filtro_por_período(registros, incio, fin):
    selecciona los registros comprendidos entre dos fechas
- medias_por_meses(registros):
    media de precipitaciones y temperaturas por meses
- genera_climograma(precs, t_maxs, t_mins):
    genera un gráfico a partir de los valores para cada mes    
- variaciones_mensuales(historicos, valores):
    mide la variación, mes a mes, entre valores de dos períodos
- variaciones_anuales(historicos, valores):
    mide la variación anual entre valores de dos períodos
- evolucion_variaciones_anuales(registros, periodo_base, periodo_estudio):
    muestra la evolución de las variaciones anuales
'''

import csv
from collections import namedtuple
from matplotlib import pyplot as plt
from datetime import datetime
import pandas as pd
import calendar
import locale

# EJERCICIO 1:
Registro = namedtuple('Registro', 'fecha, lluvia, temp_max, temp_min')
def lee_registros(fichero):
    ''' Lee el fichero de entrada y devuelve una lista de registros
    
    ENTRADA: 
       - fichero: nombre del fichero de entrada -> str
    SALIDA: 
       - lista de registros meteorológicos -> [Registro(datetitme.date, float, float, float)]
    
    Para convertir la fecha de str a date se utilizará la función strptime del
    módulo datetime de la librería estándar de Python. En concreto, usaremos la
    siguiente instrucción:
             fecha = datetime.strptime(cadena_fecha, '%Y-%m-%d').date()
    '''
    with open(fichero,'r',encoding='UTF-8') as f:
        lineas = csv.reader(f)
        next(lineas)
        result = [Registro(datetime.strptime(linea[0], '%Y-%m-%d').date(),float(linea[1]),float(linea[2]),float(linea[3])) for linea in lineas]
        return result


# EJERCICIO 2:
def filtro_por_periodo(registros, inicio, fin):
    ''' Selecciona los registros comprendidos entre dos fechas
    
    ENTRADA: 
       - registros: lista de registros meteorológicos -> [Registro(datetitme.date, float, float, float)]
       - inicio: fecha inicial de la selección -> str
       - fin: fecha final de la selección -> str
    SALIDA: 
       - lista de registros seleccionados -> [Registro(datetitme.date, float, float, float)]
    
    Las fechas se reciben en formato cadena, por lo que habrá que procesarlas
    con la función datetime:
        fecha = datetime.strptime(cadena_fecha, '%Y-%m-%d').date()
    '''
    inicio = datetime.strptime(inicio, '%Y-%m-%d').date() 
    fin = datetime.strptime(fin, '%Y-%m-%d').date()
    result = [registro for registro in registros if inicio<=registro.fecha<=fin]
    return result

# EJERCICIO 3:
def medias_por_meses(registros):
    ''' Media de precipitaciones y temperaturas por meses
    
    ENTRADA: 
       - registros: lista de registros meteorológicos -> [Registro(datetitme.date, float, float, float)]
    SALIDA: 
       - media de precipitaciones por cada mes -> [float]
       - media de temperaturas máximas por cada mes -> [float]
       - media de temperaturas mínimas por cada mes -> [float]
     
    Si para un determinado mes no hay registros, se incluirá el valor 0 en
    las posiciones correspondientes de las listas.
    '''
    media_precipitaciones = []
    media_temp_max = []
    media_temp_min = []
    precipitaciones_mes = []
    temp_max_mes = []
    temp_min_mes = []
    dict_por_meses = dict_meses(registros)
    for mes in dict_por_meses:
        for registro in dict_por_meses[mes]:
            precipitaciones_mes.append(registro.lluvia)
            temp_max_mes.append(registro.temp_max)
            temp_min_mes.append(registro.temp_min)
        
        media_precipitaciones.append(sum(precipitaciones_mes)/len(precipitaciones_mes))
        media_temp_max.append(sum(temp_max_mes)/len(temp_max_mes))
        media_temp_min.append(sum(temp_min_mes)/len(temp_min_mes))
        precipitaciones_mes = []
        temp_max_mes = []
        temp_min_mes = []
    return media_precipitaciones,media_temp_max,media_temp_min
def dict_meses(registros):
    result = dict()
    for registro in registros:
        if registro.fecha.month in result:
            result[registro.fecha.month].append(registro)
        else:
            result[registro.fecha.month] = [registro]
    return result
# EJERCICIO 4:
def genera_climograma(precs, t_maxs, t_mins):
    ''' Genera un gráfico a partir de los valores para cada mes
    
    ENTRADA: 
       - precs: media de precipitaciones por cada mes -> [float]
       - t_maxs: media de temperaturas máximas por cada mes -> [float]
       - t_mins: media de temperaturas mínimas por cada mes -> [float]
    SALIDA EN PANTALLA:
       - climograma a partir de los datos recibidos
    
    El climograma es una gráfica que integra distintas informaciones sobre
    el clima. Por lo general incluye (por cada mes) las precipitaciones, las
    temperaturas máximas y las mínimas.
    En nuestra versión del climograma, las precipitaciones se muestran con un
    diagrama de barras, y las temperaturas máximas y mínimas con sendas líneas
    (en rojo y azul).
    Se usarán las siguientes instrucciones para generar la gráfica:
        ax = plt.gca()
        ax.set_ylabel("Litros")
        plt.bar(indices, precs, color='aqua')
        plt.xticks(indices, meses, rotation=80, fontsize=10)
        ax2 = ax.twinx()
        plt.plot(t_maxs, color='red')
        plt.plot(t_mins, color='blue')
        ax2.set_ylabel("Grados")
        plt.show()
    Donde meses e indices son dos listas con la siguiente información:
        - meses: nombres de los meses
        - indices: números del 0 al 11 correspondientes a los 12 meses
    
    Generaremos la lista de nombres usando las utilidades que nos proporcionan
    los módulos 'calendar' y 'locale' de la librería estándar de Python: 
        locale.setlocale(locale.LC_ALL, '')
        meses = [calendar.month_name[i] for i in range(1, 13)]
    '''
    indices = list(range(0,12))
    locale.setlocale(locale.LC_ALL, '')
    meses = [calendar.month_name[i] for i in range(1, 13)]
    ax = plt.gca()
    ax.set_ylabel("Litros")
    plt.bar(indices, precs, color='aqua')
    plt.xticks(indices, meses, rotation=80, fontsize=10)
    ax2 = ax.twinx()
    plt.plot(t_maxs, color='red')
    plt.plot(t_mins, color='blue')
    ax2.set_ylabel("Grados")
    plt.show()

# EJERCICIO 5:
def variaciones_mensuales(historicos, valores_periodo):
    ''' Mide la variación entre valores de dos períodos
    
    ENTRADA:
       - historicos: medias mensuales históricas de lluvia, temp_max, temp_min -> ([float], [float], [float])
       - valores_periodo: medias mensuales de lluvia, temp_max, temp_min de un período -> ([float], [float], [float])
    SALIDA:
       - variaciones mensuales del período con respecto a los datos históricos -> ([float], [float], [float])
    
    Las tres listas de salida tendrán un valor para cada mes, que se calculará
    restando el correspondiente valor histórico al valor actual.
    '''
    lluvia = []
    temp_max = []
    temp_min = []
    for x in range(3):
        for i in range(12):
            if x == 0:
                lluvia.append(historicos[x][i]-valores_periodo[x][i])
            if x == 1:
                temp_max.append(historicos[x][i]-valores_periodo[x][i])
            if x == 2:
                temp_min.append(historicos[x][i]-valores_periodo[x][i])
    return lluvia,temp_max,temp_min
# EJERCICIO 6:
def variaciones_anuales(historicos, valores_periodo):
    ''' Mide la variación anual entre valores de dos períodos

    ENTRADA:
       - historicos: medias mensuales históricas de lluvia, temp_max, temp_min -> ([float], [float], [float])
       - valores_periodo: medias mensuales de lluvia, temp_max, temp_min de un período -> ([float], [float], [float])
    SALIDA:
       - variaciones anuales medias del período con respecto a los datos históricos -> (float, float, float)


    Produce como salida tres valores correspondientes a las variaciones anuales
    del segundo período con respecto al primero:
        - var_prec: variación anual media de temperatura
        - var_t_max: variación anual media de la temperatura máxima
        - var_t_min: variación anual media de la temperatura mínima
    
    Para calcular la variación anual media se seguirá el siguiente procedimiento:
        - Calcular las medias por meses de cada período, con la función 'medias_por_meses'
        - Calcular las variaciones mensuales entre ambos períodos con la función 'variaciones_mensuales'
        - Calcular la media de las variaciones mensuales para cada una de las
          tres medidas (lluvia, temperaturas máximas y temperaturas mínimas)
    '''
    historicos_mes=medias_por_meses(historicos)
    valores_periodo_mes = medias_por_meses(valores_periodo)
    lluvia,temp_max,temp_min = variaciones_mensuales(historicos_mes, valores_periodo_mes)
    var_prec = sum(lluvia)/len(lluvia)
    var_t_max = sum(temp_max)/len(temp_max)
    var_t_min = sum(temp_min) / len(temp_min)
    return var_prec,var_t_max,var_t_min

# EJERCICIO 7:
def evolucion_variaciones_anuales(registros, periodo_base, periodo_estudio):
    ''' Muestra la evolución de las variaciones anuales
    
    ENTRADA:
       - registros: lista de registros meteorológicos -> [Registro(datetitme.date, float, float, float)]
       - periodo_base: lista de años del período base -> [int]
       - periodo_estudio: lista de años del período de estudio -> [int]
    SALIDA EN PANTALLA:
       - gráfica con las variaciones en los años del período de estudio (una curva para lluvia
         otra para t_max y otra para t_min) con respecto al período base 
    
    El procedimiento a seguir es el siguiente:
        - Obtener las fechas de inicio y fin del período base. Se añadirá el
          sufijo "-01-01" al primer año, y el sufijo "-12-31" al último año.
        - Filtrar los registros del período base.
        - Para cada año del período de estudio:
           * Filtrar los registros de dicho año.
           * Calcular las variaciones de cada métrica con la función 'variaciones_anuales'
           y añadir cada una de ellas (de lluvia, temperatura máxima y temperatura mínima) 
           a la correspondiente lista de variaciones (vars_prec, vars_tmax, vars_tmin).
           
    Una vez calculadas las listas vars_prec, vars_tmax y vars_tmin con un valor para cada año,
    la gráfica se generará con las siguientes instrucciones. Previamente al trazado de las
    curvas se calculan las medias móviles para filtrar los picos:
        vars_prec = pd.Series(vars_prec).rolling(window=10,center=False).mean()
        vars_tmax = pd.Series(vars_tmax).rolling(window=10,center=False).mean()
        vars_tmin = pd.Series(vars_tmin).rolling(window=10,center=False).mean()
        ax = plt.gca()
        ax.set_ylabel("Litros")
        plt.plot(vars_prec, color='aqua', label='Lluvia')
        plt.legend(loc='lower left')
        ax2 = ax.twinx()
        plt.plot(vars_tmax, color='red', label='T. máxima')
        plt.plot(vars_tmin, color='blue', label='T. mínima')
        ax2.set_ylabel("Grados")
        ax2.set_xticklabels(periodo_estudio)
        plt.legend(loc='lower right')
        plt.show()
    '''
    vars_prec = []
    vars_tmax = []
    vars_tmin = []
    inicio = str(periodo_base[0]) + "-01-01"
    fin = str(periodo_base[-1])+ "-12-31"
    filtro_periodo_base = filtro_por_periodo(registros, inicio, fin)
    filtro_ano_estudio = [registro for registro in registros  if registro.fecha.year in periodo_estudio]
    dict_por_anos_estudio = {ano:[registro for registro in registros if registro.fecha.year == ano] for ano in periodo_estudio}
    for ano in dict_por_anos_estudio:
        prec,t_max,t_min = variaciones_anuales(dict_por_anos_estudio[ano], filtro_periodo_base)
        vars_prec.append(prec)
        vars_tmax.append(t_max)
        vars_tmin.append(t_min)
    vars_prec = pd.Series(vars_prec).rolling(window=10,center=False).mean()
    vars_tmax = pd.Series(vars_tmax).rolling(window=10,center=False).mean()
    vars_tmin = pd.Series(vars_tmin).rolling(window=10,center=False).mean()
    ax = plt.gca()
    ax.set_ylabel("Litros")
    plt.plot(vars_prec, color='aqua', label='Lluvia')
    plt.legend(loc='lower left')
    ax2 = ax.twinx()
    plt.plot(vars_tmax, color='red', label='T. máxima')
    plt.plot(vars_tmin, color='blue', label='T. mínima')
    ax2.set_ylabel("Grados")
    ax2.set_xticklabels(periodo_estudio)
    plt.legend(loc='lower right')
    plt.show()

