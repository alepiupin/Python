# -*- coding: utf-8 -*-
'''
Created on 10 dic. 2018

@author: alfonso.bengoa
'''
from moluscos import *

# Test de la función lee_moluscos
def test_lee_moluscos(nombre_fichero):
    print("****test_lee_moluscos****")
    medidas = lee_moluscos(nombre_fichero)
    return medidas

#Test de la función numero_ejemplares_por_sexo
def test_numero_ejemplares_por_sexo(medidas):
    print("\n****test_numero_ejemplares_por_sexo****")
    diccionario = numero_ejemplares_por_sexo(medidas)
    print("La salida esperada:\n1528\n1307\n1342")
    print ("Salida obtenida:")
    print(diccionario['M'])
    print(diccionario['F'])
    print(diccionario['I'])

#Test de la función filtra_por_volumen
def test_filtra_por_volumen(medidas, vol_min, vol_max):
    print("\n****test_filtra_por_volumen****")
    filtradas = filtra_por_volumen(medidas,vol_min, vol_max)
    print("La salida esperada:\n2158 [('F', 0.53, 0.415, 0.15, 0.7775, 20),"+
               " ('F', 0.55, 0.44, 0.15, 0.8945, 19)]")
    print("Salida obtenida:")
    print(len(filtradas), filtradas[:2])

#Test de la función agrupa_por_volumen
def test_agrupa_por_volumen(medidas, lista_rangos):
    print("\n****test_agrupa_por_volumen****")
    grupos = agrupa_por_volumen(medidas, lista_rangos)
    print("La salida esperada:\n"+
    "(0.0, 0.05) 2016 ['M', 0.455, 0.365, 0.095, 0.514, 15)]\n"+
    "(0.05, 0.1) 1767 ['F', 0.53, 0.415, 0.15, 0.7775, 20)]\n"+
    "(0.1, 0.15) 371 ['F', 0.68, 0.55, 0.175, 1.798, 19)]\n"+
    "(0.15, 0.2) 20 ['M', 0.735, 0.59, 0.225, 1.756, 21)]")
    print("Salida obtenida:")
    for rango in grupos:
        print(rango, len(grupos[rango]), grupos[rango][:1])
    
#Test de la función muestra_puntos_longitud_diametro\n"
def test_muestra_puntos_longitud_diametro(medidas):
    print("\n****test_muestra_puntos_longitud_diametro****")
    print("ver el documento pdf de la carpeta doc")
    muestra_puntos_longitud_diametro(medidas)

#Programa principal
medidas = test_lee_moluscos('../data/moluscos.csv')
print("La salida esperada:\n4177 [('M', 0.455, 0.365, 0.095, 0.514, 15),"+
          " ('M', 0.35, 0.265, 0.09, 0.2255, 7)]")
print ("Salida obtenida:")
if medidas==None:
    print("¡Error: No se ha devuelto lista alguna!")
else:
    print(len(medidas), medidas[:2])

    test_numero_ejemplares_por_sexo(medidas)
    test_filtra_por_volumen(medidas, 0.05, 0.2)
    test_agrupa_por_volumen(medidas, [(0.0,0.05), (0.05,0.1), (0.1,0.15), (0.15,0.2)])
    test_muestra_puntos_longitud_diametro(medidas)

