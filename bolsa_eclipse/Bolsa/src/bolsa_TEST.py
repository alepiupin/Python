'''
Created on 21 nov. 2018

@author: jorge
'''
from bolsa import *

def muestra_datos(precios):
    for e in precios:
        print('{}'.format(e), precios[e][:5]) 

def test_traza_curvas(precios):
    # Test de la función traza_curvas
    colores = ['blue', 'red', 'orange', 'grey']    
    traza_curvas(precios, colores)
    
def test_traza_curva(bbva_precios):
    # Test de la función traza_curva
    traza_curva(bbva_precios, label='BBVA')
    traza_curva(bbva_precios, color='black')

def test_calcula_incrementos(precios, colores):
    # Test de la función calcula incrementos
    incrementos = {e: calcula_incrementos(precios[e]) 
                   for e in empresas}
    traza_curvas(incrementos, colores)
    
def test_calcula_media_movil(precios, empresas, colores):
    # Test de la función media_movil
    bbva_precios = precios['BBVA']
    incrementos = {e: calcula_incrementos(precios[e]) for e in empresas}

    bbva_movil = calcula_media_movil(bbva_precios, ventana=10)
    precios_media = {'Precios': bbva_precios, 'Media': bbva_movil}
    traza_curvas(precios_media, ['blue', 'red'])
    medias = {e: calcula_media_movil(incrementos[e], ventana=10) for e in empresas}
    traza_curvas(medias, colores)
    
def test_similitud_coseno():
    # Test de la función similitud_coseno
    print(similitud_coseno([1, 2, 3], [2, 4, 6]))       # Dos vectores paralelos
    print(similitud_coseno([1, 2, 3], [-2, -4, -6]))    # Dos vectores opuestos
    print(similitud_coseno([1, 0, 1], [0, 1, 0]))       # Dos vectores ortogonales
    print(similitud_coseno([1, 2, 3], [1.7, 4.3, 5.8])) # Dos vectores parecidos

def test_empresas_mas_parecidas():
    # Test de la función empresa_mas_parecida
    empresa_base = 'BBVA'
    bancos = ['CABK', 'BKT', 'SAB', 'SAN', 'POP', 'BBVA']
    constructoras = ['ACS', 'FER', 'FCC']
    energia = ['ELE', 'REE', 'ENG', 'GAS', 'IBE']
    empresas = bancos + constructoras + energia
    precios = lee_precios_empresas(empresas)
    (empresa, similitudes) = busca_empresa_mas_parecida(precios, empresa_base, empresas)
    print('La empresa más parecida a ' + empresa_base + ' es ' + empresa)
    for e in similitudes.keys():
        print("{:5}  {:5.3f}".format(e, similitudes[e]))
    
if __name__ == '__main__':
    # Test de la función lee_precios_empresa
    #bbva_precios = lee_precios_empresa('BBVA')
    #muestra_datos(bbva_precios[:20])
    # Test de la función lee_precios_empresas
 #   empresas = ['BBVA', 'SAN', 'ACS', 'GAS']
 #   precios = lee_precios_empresas(empresas)
 #   colores = ['blue', 'red', 'orange', 'grey']
    
    #test_traza_curva(precios["BBVA"])
    #test_traza_curvas(precios)
    #test_calcula_incrementos(precios, colores)
    #test_calcula_media_movil(precios, empresas, colores)    
    #test_similitud_coseno() 
 #   test_empresas_mas_parecidas()

   
   
        