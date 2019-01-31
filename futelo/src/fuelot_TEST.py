'''
Created on 26 dic. 2018

@author: alejandro
'''
from futelo import *
def muestra_diccionario(datos):
    for k in datos:
        print(str(k) + ":" + str(datos[k]) )
    
def test_equipos_participantes(primera,segunda):
    equipos_primera = equipos_participantes(primera)
    print(len(equipos_primera), equipos_primera)
    equipos_segunda = equipos_participantes(segunda)
    print(len(equipos_segunda), equipos_segunda)    
    
def test_partidos_por_equipos(equipos):
    primera = lee_competicion('../datos/primera/')
    segunda = lee_competicion('../datos/segunda/')
    partidos = primera + segunda
    partidos_de_equipo = partidos_por_equipos(partidos, equipos)   
    print(len(partidos_de_equipo), partidos_de_equipo[:5])
    
def test_partidos_por_fecha(partidos, inicio, fin):
    print(len(partidos_por_fecha(partidos, inicio, fin)))
    print(len(partidos_por_fecha(partidos, inicio, None)))
    print(len(partidos_por_fecha(partidos, None, fin)))
    print(len(partidos_por_fecha(partidos, None, None)))
    
def test_calcula_elo(elo_a,elo_b,goles_a,goles_b):
    print(calcula_elo(elo_a, elo_b, goles_a, goles_b))
    
def test_calcula_ranking_elo(partidos):
    elo = calcula_ranking_elo(primera, ranking_previo={'Cádiz CF':2000})
    print(muestra_ranking(elo, limite=10))
    
def test_calcula_rendimiento(partidos):
    inicio_14 = datetime(2014, 8, 15).date()
    partidos_hasta_14 = partidos_por_fecha(partidos, inicio=None, fin=inicio_14)
    ranking_hasta_14 = calcula_ranking_elo(partidos_hasta_14)
    primera_14_16 = partidos_por_fecha(partidos, inicio=inicio_14, fin=None)
    print(calcula_rendimiento('Real Madrid', primera_14_16, ranking_hasta_14))
    
def test_calcula_ranking_rendimiento(partidos):
    inicio_14 = datetime(2014, 8, 15).date()
    partidos_hasta_14 = partidos_por_fecha(partidos, inicio=None, fin=inicio_14)
    ranking_hasta_14 = calcula_ranking_elo(partidos_hasta_14)
    primera_14_16 = partidos_por_fecha(partidos, inicio=inicio_14, fin=None)
    andaluces = ['Málaga CF', 'Real Betis', 'Sevilla FC', 'RC Recreativo', 
                 'Cádiz CF', 'Xerez CD', 'Granada CF', 'Córdoba CF']
    rendimiento = calcula_ranking_rendimiento(andaluces, primera_14_16, ranking_hasta_14)
    print(muestra_ranking(rendimiento))
if __name__ == '__main__':
  #  primera_15_16 = lee_temporada('../datos/primera/15-16.csv')
  #  print(primera_15_16[:5])
    primera = lee_competicion('../datos/primera/')
    segunda = lee_competicion('../datos/segunda/')
    partidos = primera + segunda
    
    
  #  test_equipos_participantes(primera, segunda) 
    equipos = ['Real Madrid', 'Rayo Vallecano', 'Atlético de Madrid', 'Getafe CF', 'CD Leganés']
 #   test_partidos_por_equipos(equipos)
 #   test_partidos_por_fecha(partidos, datetime(2007, 9, 15).date(), datetime(2008, 7, 1).date())
    #TEST CALCULA ELO
 #   test_calcula_elo(1000, 1000, 3, 3)
    ranking =  {'CD San Roque': 1489, 'Real Balompédica Linense': 1912, 
            'UD Los Barrios': 1636, 'Algeciras CF': 1750}
 #   print(muestra_ranking(ranking,1))
 #   test_calcula_ranking_elo(primera)
    # Test de la función calcula_rendimiento
  #  test_calcula_rendimiento(partidos)
    test_calcula_ranking_rendimiento(partidos)