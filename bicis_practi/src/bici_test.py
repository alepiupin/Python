'''
Created on 22 ene. 2019

@author: alejandro
'''
from bici import *

def test_lee_fichero(registros):
    print(len(registros), registros[:2])
    
def test_filtra_por_meses(filtrados):
    print(len(filtrados), filtrados[:2])
    
def test_agrupa_por_dias(grupos):
    for dia in grupos:
        print(dia, len(grupos[dia]), grupos[dia][:1])
        
def muestra_distribucion_dias(registros):
    nombres_dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
    por_dia = agrupa_por_dias(registros)
    conteos_dias = [suma_alquiladas(por_dia[dia]) for dia in range(7)]
    conteos_dias = [sum([x.alquiladas for x in por_dia[dia]]) for dia in range(7)] #SIN LA FUNCION suma_alquiladas
    plt.bar(range(len(nombres_dias)), 
            conteos_dias, tick_label=nombres_dias)
    plt.show()
    
if __name__ == '__main__':
    registros = leer_fichero('../data/bicicletas.csv')
   # Test de la función lee_biciletas
 #   test_lee_fichero(registros)
 
    # Test de la función proporcion_fin_de_semana
    #proporcion = proporcion_fin_de_semana(registros)
    #print(proporcion)
    
    # Test de la función filtra_por_meses
  #  filtrados = filtra_por_meses(registros, [2,3,4])
  #  test_filtra_por_meses(filtrados)
    
    # Test de la función agrupa_por_dias
  #  grupos = agrupa_por_dias(registros)
  #  test_agrupa_por_dias(grupos)
  
    # Test de la función muestra_distribucion_dias
    muestra_distribucion_dias(registros)