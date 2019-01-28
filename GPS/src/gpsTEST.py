'''
Created on 2 nov. 2018

@author: alejandro
'''
import csv
from datetime import datetime
from math import sin, cos, sqrt, atan2, radians
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import gps
from gps import readFile, coordinates_point, time_moment,\
    distance_range, filtered_time, distancia_haversine3d,\
    speed_range, unevenness, speed_graphics, profile_graphics, map_rute
from _datetime import date


data = readFile('../resources/ruta.csv')

def coor_point(point):
    coor = coordinates_point(point)
    return coor

def tim_point(point):
    tim = time_moment(point)
    return tim

def time_range(start,end,data):
    time = filtered_time(start,end,data)
    return time

def distancia3d(coord_a,coord_b):
    distancia = distancia_haversine3d(coord_a,coord_b)
    return distancia

def distanceRange(points):
    distance = distance_range(points)
    return distance

def speed_rang(points):
    time = speed_range(points)
    return time

def unevenness_total(points):
    uneveness = unevenness(points)
    return uneveness

def pro_graphics(points):
    graphics = profile_graphics(points)
    return graphics

def spe_graphics(points):
    grapichs = speed_graphics(points)
    return grapichs

def map_rut(points,mapa):
    mapa2 = map_rute(points,mapa)
    return  mapa2


if __name__ == '__main__': 
    
    #Test de la funcion time_range
 #   primera_parte = time_range('00:00:00', '00:01:30', data)
 #   print(len(primera_parte))
 #   print(primera_parte[:5])
    
    # Test de la función distancia_haversine_3d

    
    # Test de la función distancia_trayecto
  #  print(distanceRange(primera_parte))
    
    # Test de la función velocidad_trayecto
#    print(speed_rang(data))
  #  print(speed_range(primera_parte))
    
    # Test de la función desnivel_acumulado
 #   print(unevenness_total(data))
 #   print(unevenness_total(primera_parte))
    
    # Test de la función mostrar_perfil
 #   pro_graphics(data)
    
    # Test de la función mostrar_velocidad_por_intervalo
#    spe_graphics(data)
    # Test de la función mostrar_ruta_en_mapa
    
   # map_rut(data, '../resources/mapa_ronda.PNG')
    
    
        
    
    
 


    
    
    