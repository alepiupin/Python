# -*- coding: utf-8 -*-
''' Vestidos 

AUTOR: Mariano González
REVISOR: José A. Troyano, Fermín Cruz, Carlos García, Toñi Reina
ÚLTIMA MODIFICACIÓN: 21/1/2018

################################################################
#  Datos del alumno
#
#  Nombre y apellidos: 
#  DNI: 
#  Grupo: 
################################################################

En este ejercicio trabajaremos sobre un dataset de atributos y ventas de vestidos,
http://archive.ics.uci.edu/ml/datasets/Dresses_Attribute_Sales. Este dataset contiene
información sobre los atributos y las ventas online de una serie de vestidos.
Nosotros trabajaremos con los atributos de los vestidos, que se encuentran
en formato CSV. Estas son las primeras líneas del fichero de entrada:

    Dress_ID,Style,Price,Rating,Size,Season,Material
    1006032852,Classic,Low,4.6,M,Summer,null
    1212192089,Casual,Low,0,L,Summer,microfiber
    1190380701,vintage,High,0,L,Autumn,polyster
    966005983,Brief,Average,4.6,L,Spring,silk
    876339541,cute,Low,4.5,M,Summer,chiffonfabric
    1068332458,bohemian,Low,0,M,Summer,null
    1220707172,Casual,Average,0,XL,Summer,cotton
        
Donde:
    Dress_ID: identificador del vestido
    Style: estilo del vestido
    Price: precio del vestido (en forma cualitativa, no numérica)
    Rating: Valoración del vestido por los usuarios, de 0 a 5
    Size: Talla del vestido
    Season: Temporada (estación del año) del vestido
    Material: material del que está fabricado el vestido
        
FUNCIONES DISPONIBLES:
----------------------
- lee_vestidos(fichero):
    Lee el fichero de atributos de los vestidos
- filtra_por_tallas(registros, tallas):
    Obtiene los vestidos de unas tallas determinadas
- vestido_mas_valorado(registros, estilo):
    Obtiene el vestido más valorado de un estilo dado
- agrupa_por_temporada(registros):
    Crea un diccionario que relaciona temporadas con vestidos   
- muestra_distribucion_temporadas_estilos(registros, estilos):
    Dibuja un diagrama de barras con la valoración media de los vestidos
    de cada temporada y de unos estilos dados
'''

import csv
from matplotlib import pylab as plt
from collections import namedtuple

Vestido = namedtuple('Vestido', 'dress_ID style price rating size season material')
# EJERCICIO 1:
def lee_vestidos(fichero):
    ''' Lee el fichero de atributos de los vestidos
        Devuelve una lista de tuplas, donde cada tupla contiene los
        siete atributos de un vestido, en el mismo orden en que
        aparecen en el fichero y con el tipo de dato adecuado
    '''
    with open(fichero,'r',encoding = 'UTF-8') as f:
        lineas = csv.reader(f)
        next(f)
        result = [Vestido(int(linea[0]),linea[1],linea[2],float(linea[3]),linea[4],linea[5],
                          linea[6]) for linea in lineas]
        
        return result
# EJERCICIO 2:
def filtra_por_tallas(registros, tallas):
    ''' Obtiene los vestidos cuya talla es una de las que aparecen en la lista que
        recibe como parámetro de entrada
        Devuelve una lista de tuplas con los vestidos seleccionados
    '''
    result = [registro for registro in registros if registro.size in tallas]
    return result

# EJERCICIO 3:
def vestido_mas_valorado(registros, estilo='Casual'):
    ''' Obtiene el vestido más valorado del estilo dado como parámetro de entrada
        Devuelve una tupla con la valoración y el id del vestido
        Si hay varios vestidos con la misma valoración, devuelve uno cualquiera de ellos
    '''
    vestidos_por_valoracion = dict_id_valoracion(registros, estilo)
    maxima_valoracion = max(vestidos_por_valoracion,key = vestidos_por_valoracion.get)
    return (vestidos_por_valoracion[maxima_valoracion],maxima_valoracion)

def dict_id_valoracion (registros,estilo):
    result = {registro.dress_ID:registro.rating  for registro in registros if registro.style == estilo}
    return result

# EJERCICIO 4:
def agrupa_por_temporada(registros):
    ''' Crea un diccionario que relaciona las temporadas con los vestidos de cada temporada
        Devuelve un diccionario cuyas claves son las temporadas
        y cuyos valores son listas de tuplas con los vestidos de cada temporada
    '''
    result = dict()
    for registro in registros:
        if registro.season in result:
            result[registro.season].append(registro)
        else:
            result[registro.season] = [registro]
    return result

# EJERCICIO 5:
def muestra_distribucion_temporadas_estilos(registros, estilos):
    ''' Toma como entrada una lista de registros y una lista de estilos.
        Dibuja un diagrama de barras con la valoración media de los vestidos
        de cada temporada que son de uno de los estilos indicados
    
        Para dibujar las barras, utilice las siguientes instrucciones:
            plt.bar(range(len(temporadas)), valoraciones_medias, tick_label=temporadas)
            plt.show()
        donde valoraciones_medias es una lista con las valoraciones medias de los
        vestidos de cada temporada que son de uno de los estilos especificados en la lista estilos,
        y temporadas es una lista con las temporadas
    '''
    dict_por_temporadas = agrupa_por_temporada(registros)
    valoraciones_medias = calcula_lista_media(dict_por_temporadas, estilos)
    temporadas = list(dict_por_temporadas.keys())
    plt.bar(range(len(temporadas)), valoraciones_medias, tick_label=temporadas)
    plt.show()
    
def calcula_lista_media(dict, estilos):
    result = []
    suma_valoraciones = 0
    for clave,valor in dict.items():
        lista_rating = [vestido.rating for vestido in valor if vestido.style in estilos]
        result.append((sum(lista_rating))/len(lista_rating))
    return result
    

