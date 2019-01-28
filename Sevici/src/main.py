'''
Created on 25 oct. 2018

@author: alejandro
'''
import csv
from math import sqrt
from matplotlib import pylab as plt
from matplotlib import image as mpimg
def leer_estaciones(ruta):
    with open (ruta) as fichero:
        tuplas = csv.reader(fichero)
        next(tuplas)
        result = [(linea[0], int(linea[1]),int(linea[2]),int(linea[3]),float(linea[4]),float(linea[5]))  for linea in tuplas] 
    return result

def bicis_libres(estaciones, k = 5):
    result = [(a,b) for a,_,_,b,_,_ in estaciones if b >= k]
    result.sort()
    return result

def calcula_distancia(x1,y1,x2,y2,fb):
    result = sqrt((x2-x1)**2 + (y2-y1)**2)*(1-(fb/100))
    return result

def estaciones_cercanas(estaciones,lat,lon,k=5):
    lis_distancias = [(a,calcula_distancia(lat, lon, b, c, d),b,c,d) for a,_,_,d,b,c in estaciones]
    for recorrido in range(1,len(lis_distancias)-1):
        for posicion in range(len(lis_distancias)-recorrido):
            if lis_distancias[posicion][1] > lis_distancias[posicion + 1][1]:
                temp = lis_distancias[posicion]
                lis_distancias[posicion] = lis_distancias[posicion+1]
                lis_distancias[posicion + 1] = temp
    est_proxim = lis_distancias[:k]
    return est_proxim 
def dibuja_mapa():
    ancho = 9
    aspect_ratio = 1.09
    img = mpimg.imread('../resources/mapa.png')
    plt.figure(figsize=(ancho, ancho * aspect_ratio))
    plt.imshow(img, zorder=0, extent=[0, ancho, 0, ancho * aspect_ratio])    
    plt.axis('off') 
    
def dibuja_estaciones(coordenadas, color="red"):
    ancho = 9
    aspect_ratio = 1.09
    xs = [(x - 37.31) * ancho * aspect_ratio / 0.13 for x, _ in coordenadas]
    ys = [(y + 6.04) * ancho / 0.15 for _, y in coordenadas]
    plt.scatter(ys, xs, zorder=1, s=10, color=color)          
    
def ubicacion_estaciones(estaciones):
    result = [(a,b) for _,_,_,_,a,b in estaciones]
    return result
def ubicacion_libres(estaciones,k=5):
    result=[(b,c) for _,_,_,a,b,c in estaciones if a>=k]    
    return result
if __name__ == '__main__':  
    estaciones = leer_estaciones('../resources/estaciones.csv')
    gps = estaciones_cercanas(estaciones, 37.359123 , -5.986412)
    print("Hay ",len(gps), " estaciones cercas: ", str(gps))
 #   coordenadas_cercanas = [(a,b) for _,_,a,b,_ in gps]
    coordenadas_todas = ubicacion_estaciones(estaciones)
    coordenadas_libres = ubicacion_libres(estaciones)
    dibuja_mapa()
    dibuja_estaciones(coordenadas_todas)
    dibuja_estaciones(coordenadas_libres, color = "green")
    plt.show()
 #   print(coordenadas_libres)