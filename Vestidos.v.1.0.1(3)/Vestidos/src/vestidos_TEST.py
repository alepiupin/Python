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
from vestidos import *

################################################################
#  Funciones de test
################################################################
def test_filtra_por_tallas(registros):
    vestidos_s_m = filtra_por_tallas(registros, ['S', 'M'])
    print('Hay', len(vestidos_s_m), 'vestidos de las tallas S y M y el primero de ellos es', 
          vestidos_s_m[0])

def test_vestido_mas_valorado(registros):
    valoracion, dress_id = vestido_mas_valorado(registros)
    print('El vestido más valorado de estilo \'Casual\' es:', dress_id, 'con', valoracion, 'puntos')
    valoracion, dress_id = vestido_mas_valorado(registros, 'vintage')
    print('El vestido más valorado de estilo \'vintage\' es:', dress_id, 'con', valoracion, 'puntos')
    
def test_agrupa_por_temporada(registros):
    vestidos_temporada = agrupa_por_temporada(registros)
    print('Número de vestidos de cada temporada:')
    for temporada in vestidos_temporada:
        print(temporada, ': ', len(vestidos_temporada[temporada]), '. ', sep='', end=' ')
    
def test_muestra_distribucion_temporadas_estilos(registros):
    muestra_distribucion_temporadas_estilos(registros, ['vintage', 'Casual'])
  
       
################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    registros = lee_vestidos('../data/vestidos.csv')
    print("Número total de vestidos:", len(registros)) 
    print(registros[:5], '\n')
    
    '''
    Elimine los comentarios de las llamadas a los test a medida que
    vaya escribiendo las respectivas funciones
    '''
#    test_filtra_por_tallas(registros)
#    test_vestido_mas_valorado(registros)
#    test_agrupa_por_temporada(registros)
    test_muestra_distribucion_temporadas_estilos(registros)