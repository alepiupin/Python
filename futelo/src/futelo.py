'''
Created on 26 dic. 2018

@author: alejandro
'''
from os import listdir
import csv
from collections import namedtuple
from datetime import datetime

Partido = namedtuple('Partido', 'fecha local goles_local visitante goles_visitante')

def lee_temporada(ruta):
    with open(ruta,'r', encoding='UTF-8') as f:
        tupla = csv.reader(f)
        result = [(datetime.strptime(fecha, "%d/%m/%Y").date(), equilocal,int(goleslocal),equivisi,int(golvisit)) 
                  for fecha,equilocal,goleslocal,equivisi,golvisit in tupla]
    return result 

def lee_competicion(carpeta):
    result = []
    for fichero in listdir(carpeta):
        result += lee_temporada(carpeta + fichero)
    return result

def equipos_participantes(partidos):
    result = {x[1] for x in partidos}
    result.update({x[3] for x in partidos})
    return result

def partidos_por_equipos(partidos,equipos):
    return [x for x in partidos if x[1] in equipos or x[3] in equipos]

def partidos_por_fecha(partidos, inicio=None, fin=None):
    if inicio == None:
        inicio = datetime.strptime("1/1/1900", "%d/%m/%Y").date()
    if fin == None:
        fin = datetime.utcnow().date()
    return [x for x in partidos if inicio<=x[0]<=fin]

def calcula_elo(elo_a,elo_b,goles_a,goles_b, k=20):
    ea = 1 / (1 + pow(10, (elo_b - elo_a) / 400))
    eb = 1 / (1 + pow(10, (elo_a - elo_b) / 400))
    if goles_a > goles_b:
        ra = 1
        rb = 0
    elif goles_a == goles_b:
        ra = 0.5
        rb = 0.5
    else:
        ra = 0
        rb = 1
    eloa = elo_a + (ra - ea) * k
    elob = elo_b + (rb - eb) * k
    return eloa, elob


def muestra_ranking(ranking,limite = None):
    ran_ordena = sorted(ranking, key = ranking.get, reverse = True)
    result = [(x,ranking[x]) for x in ran_ordena]
    if limite == None:
        return result
    else:
        return result[:limite]  

def calcula_ranking_elo(partidos, ranking_previo=dict()):
    ranking_result = ranking_previo
    partidos.sort()
    for partido in partidos:
        eloa,elob = calcula_elo(ranking_result.get(partido[1],1000), ranking_result.get(partido[3],1000), partido[2], partido[4])
        ranking_result.update({partido[1]: eloa})
        ranking_result.update({partido[3]: elob})
    return ranking_result

def calcula_rendimiento(equipo,partidos,ranking_elo):
    victorias = 0
    derrotas = 0
    sumaelo = 0
    numero_partido = 0
    for partido in partidos:
        if partido[1] == equipo:
            numero_partido += 1
            sumaelo += sum([ranking_elo[x] for x in ranking_elo if x == partido[3]])
            if partido[2] > partido[4]:
                victorias += 1
            elif partido[2] < partido [4]:
                derrotas += 1
        elif partido [3] == equipo:
            numero_partido += 1
            sumaelo += sum([ranking_elo[x] for x in ranking_elo if x == partido[1]])
            if partido[4] > partido[2]:
                victorias += 1
            elif partido[4] < partido [2]:
                derrotas += 1
    if numero_partido == 0:
        numero_partido = 1
    return (sumaelo+(victorias*400)-(derrotas*400))/numero_partido

def calcula_ranking_rendimiento(equipos,partidos,ranking_elo):
    ranking_result = {equipo : calcula_rendimiento(equipo, partidos, ranking_elo)  for equipo in equipos}
    return ranking_result
                
                
            
                
        