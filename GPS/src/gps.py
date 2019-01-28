'''
Created on 2 nov. 2018

@author: alejandro
'''
import csv
from datetime import datetime
from math import sin, cos, sqrt, atan2, radians
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from ipykernel.tests.test_serialize import point

def readFile (path):
    with open (path) as file:
        tupla = csv.reader(file)
        result = [(datetime.strptime(read[0], '%H:%M:%S'),float(read[1]),float(read[2]),float(read[3])) for read in tupla]
        return result
    
def coordinates_point (point):
    result = [(lat,lon) for _,lat,lon,_ in point]
    return result 


def time_moment(point):
     result = point[0]
     return result
 
def distancia_haversine(coord_a, coord_b):
    radio_tierra = 6373.0
    latitud_a, longitud_a = radians(coord_a[0]), radians(coord_a[1])
    latitud_b, longitud_b = radians(coord_b[0]), radians(coord_b[1])    
    inc_lat  = latitud_b - latitud_a
    inc_long = longitud_b - longitud_a

    a = sin(inc_lat / 2)**2 + cos(latitud_a) * cos(latitud_b) * sin(inc_long / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return radio_tierra * c

def distancia_haversine3d(coord_a,coord_b):
    distancia3d = sqrt((distancia_haversine(coord_a, coord_b))**2 + (coord_b[2]-coord_a[2])**2)
    return distancia3d

def filtered_time(start,end, data):
    start = datetime.strptime(start,'%H:%M:%S') 
    end = datetime.strptime(end,'%H:%M:%S')
    result = [(time,lat,lon,alt) for time,lat,lon,alt in data if time >= start and time <= end]
    return result

def distance_range(points): 
    total_distance = 0
    for i in range(len(points)-1):
        distance2points = distancia_haversine3d((points[i][1],points[i][2],points[i][3]), (points[i+1][1],points[i+1][2],points[i+1][3]))
        total_distance = total_distance + distance2points
    return total_distance    
     
def speed_range(points):
    totaltime = 0
    for i in range(len(points)-1):
        timebetween2 = (points[i+1][0]-points[i][0]).seconds/3600
        totaltime = timebetween2 + totaltime    
    return (distance_range(points)/totaltime) 

def unevenness(points):
    total_unevennes_up = 0
    total_unevennes_down = 0
    for i in range(len(points)-1):
        unevenness = abs(points[i+1][3] - points[i][3])
        if points[i][3] < points[i+1][3]:
            total_unevennes_up += unevenness
        elif points[i][3] > points[i+1][3]:
            total_unevennes_down += unevenness
    return (total_unevennes_up, total_unevennes_down)

def profile_graphics(points):
    y = [alt for _,_,_,alt in points]
    x = [distance_range(points)*i/len(y) for i in range(len(y))]
    plt.plot(x,y)
    plt.show()
    
def speed_graphics(points):
    y = []
    for i in range(len(points)-1):
     if ((points[i+1][0] - points[i][0]).seconds/3600) != 0:
         y.append((distancia_haversine3d((points[i][1],points[i][2],points[i][3]), (points[i+1][1],points[i+1][2],points[i+1][3])))/((points[i+1][0] - points[i][0]).seconds/3600))
         
    x = [distance_range(points)*i/len(y) for i in range(len(y))]    
    plt.plot(x,y)
    plt.show()
    
    
def map_rute(points, mapa, lado=9, lat_base=-36.665, long_base=5.282, escala=0.23):
        lats_longs = coordinates_point(points)
        img = mpimg.imread(mapa)
        plt.figure(figsize=(lado, lado))
        plt.imshow(img, zorder=0, extent=[0, lado, 0, lado])    
        xs = [(x + lat_base) * lado  / 0.23 for x, _ in lats_longs]
        ys = [(y + long_base) * lado / 0.23 for _, y in lats_longs]
        plt.scatter(ys, xs, zorder=1, s=10, color='blue')
        plt.axis('off')
        plt.show()
            
     
    
         