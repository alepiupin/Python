'''
Created on 8 ene. 2019

@author: jorge
'''

from bicis import * 
from collections import Counter

def test_lee_bicicletas(registros):
    # Test de la función lee_biciletas
    # La salida esperada de la siguiente instrucción es: 
    #    17379 [Registro(mes=1, dia=6, hora=0, temperatura=0.24, humedad=0.81, viento=0.0, alquiladas=16), 
    #           Registro(mes=1, dia=6, hora=1, temperatura=0.22, humedad=0.8, viento=0.0, alquiladas=40)]
    print(len(registros), registros[:2])
    
def test_proporcion_fin_de_semana(registros):
    # Test de la función proporcion_fin_de_semana
    proporcion = proporcion_fin_de_semana(registros)
    
    # La salida esperada de la siguiente instrucción es: 
    #   0.27996473388386783
    print(proporcion)

def test_filtra_por_meses(registros, meses):
    # Test de la función filtra_por_meses
    filtrados = filtra_por_meses(registros, meses)
    
    # La salida esperada de la siguiente instrucción es: 
    # 4251 [Registro(mes=2, dia=2, hora=0, temperatura=0.16, humedad=0.64, viento=0.1045, alquiladas=8), 
    #       Registro(mes=2, dia=2, hora=1, temperatura=0.16, humedad=0.69, viento=0.1045, alquiladas=3)]
    print(len(filtrados), filtrados[:2])
    
def muestra_distribucion_dias(registros):
    ''' Genera una diagrama de barras con la distribución por días del número de
        bicicletas alquiladas
        
        ENTRADA:
           - registros: lista de registros -> 
           [Registro(int, int, int, float, float, float, int)]
        SALIDA EN PANTALLA:
           - diagrama de barras con el número 
           total de bicicletas alquiladas 
           cada día de la semana
    
        Se usarán las siguientes instrucciones matplotlib para generar el diagrama
        de barras:
            plt.bar(range(len(nombres_dias)), 
            conteos_dias, tick_label=nombres_dias)
            plt.show()
        
        Donde las variables significan lo siguiente:
            - nombres_dias: 
            lista con los nombres de los días
            - conteos_dias: 
            lista con el número de bicicletas 
            alquiladas cada día
    '''
    nombres_dias = ['DOMINGO', 'LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES', 'SABADO']
    por_dias = agrupa_por_dias(registros)
    conteos_dias = [suma_alquiladas(por_dias[str(dia)]) 
                   for dia in range(7)] 
    plt.bar(range(len(nombres_dias)), 
            conteos_dias, tick_label=nombres_dias)
    plt.show()
            
            
            
            
    
def test_agrupa_por_dias(registros):
    # Test de la función agrupa_por_dias
    grupos = agrupa_por_dias(registros)
    
    # La salida esperada de la siguiente instrucción es: 
    # 0 2502 [Registro(mes=1, dia=0, hora=0, temperatura=0.46, humedad=0.88, viento=0.2985, alquiladas=17)]
    # 1 2479 [Registro(mes=1, dia=1, hora=0, temperatura=0.22, humedad=0.44, viento=0.3582, alquiladas=5)]
    # 2 2453 [Registro(mes=1, dia=2, hora=0, temperatura=0.16, humedad=0.55, viento=0.1045, alquiladas=5)]
    # 3 2475 [Registro(mes=1, dia=3, hora=0, temperatura=0.2, humedad=0.64, viento=0.0, alquiladas=6)]
    # 4 2471 [Registro(mes=1, dia=4, hora=0, temperatura=0.18, humedad=0.55, viento=0.0, alquiladas=11)]
    # 5 2487 [Registro(mes=1, dia=5, hora=0, temperatura=0.2, humedad=0.64, viento=0.19399999999999998, alquiladas=17)]
    # 6 2512 [Registro(mes=1, dia=6, hora=0, temperatura=0.24, humedad=0.81, viento=0.0, alquiladas=16)]
    
    for dia in grupos:
        print(dia, len(grupos[dia]), grupos[dia][:1])
    
if __name__ == '__main__':
    
    registros = lee_bicicletas('../data/bicicletas.csv')
    
    #test_lee_bicicletas(registros)
    
    #test_proporcion_fin_de_semana(registros)
    
    #test_filtra_por_meses(registros, [2,3,4])
    
    #test_agrupa_por_dias(registros)
    
    muestra_distribucion_dias(registros)