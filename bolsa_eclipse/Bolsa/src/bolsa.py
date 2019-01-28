'''
Created on 21 nov. 2018

@author: jorge
'''
from matplotlib import pyplot as plt


def lee_precios_empresa(empresa, ruta='../datos/',
                        extension='.MC.txt'):

    fichero = ruta + empresa + extension
    with open(fichero, "r", encoding="UTF-8") as f:
        result = [float(linea) for linea in f]
    return result
    
    
def lee_precios_empresas(empresas, ruta='../datos/'
                         , extension='.MC.txt'):

    result = {empresa: 
              lee_precios_empresa(empresa,
                                  ruta, extension)
              for empresa in empresas}
    return result

    
def traza_curva(serie, label='Valor', color='blue'):
    ''' Traza una curva a partir de una serie de puntos
    
    ENTRADA: 
       - serie: lista de valores numéricos -> [float]
       - label: eqtiqueta que se mostrará 
       en la gráfica -> str
       - color: que se usará para 
       trazar la curva -> str
    SALIDA EN PANTALLA:
       - gráfica con la evolución de la serie a lo largo del tiempo

    Utiliza el método plot del paquete matplotlib. Usaremos dos de los
    parámetros más importantes del método plot para controlar un poco el
    estilo de la gráfica:
        - label: etiqueta que se le asocia a la curva
        - color: color del trazo
    El método legend del objeto plt nos permite visualizar la leyenda con
    las etiquetas.
    '''
    plt.plot(serie, label=label, color=color)
    plt.legend()
    plt.show()  

    
def traza_curvas(series, colores):
    '''
    Para resolver este ejercicio 
    seguiremos los siguientes pasos:
    - Calcular una lista 
    con los nombres de las series 
    (las claves del diccionario)
    - Calcular una lista paralela 
    a la anterior cuyos elementos serán las series 
    (los valores del diccionario)
    - Recorrer en paralelo las dos 
    listas anteriores, 
    junto con la lista de colores,
    para generar los distintos 
    trazos de la gráfica
    '''
    
    claves = series.keys()
    valores = series.values()
    for nombre, serie, color in zip(claves, valores, colores):
        plt.plot(serie, label=nombre, color=color)
    plt.legend()
    plt.show()

    
def calcula_incrementos(serie):
    ''' Calcula incrementos porcentuales 
    (tantos por 1) a partir de una serie
    
    ENTRADA: 
       - serie: lista de valores numéricos -> [float]
    SALIDA: 
       - lista de incrementos -> [float] 

    Se calcula el incremento de la posición "i" 
    con respecto a la posición
    "i-1". 
    La lista de salida tendrá, por tanto, 
    una posición menos. 
    Los
    valores resultantes se encuentran centrados 
    en el 0 y estarán normalizados
    en cuanto a la magnitud. 
    Por ejemplo un valor de 0.05 implica una subida
    diaria del 5%, y una bajada del 1% 
    se corresponderá con -0.01.
    '''
    final = serie[1:]
    inicial = serie[0:-1]
    diferenciales = zip(inicial, final)
    result = [(fin - inicio) / inicio for inicio, fin in diferenciales ]
    
    return result


def calcula_media_movil(serie, ventana=5):
    ''' Calcula la media móvil de una serie
    
    ENTRADA: 
       - serie: lista de valores numéricos -> [float]
       - ventana: número de valores que se usarán para calcular la media móvil -> int
    SALIDA: 
       - lista de medias móviles -> [float] 

    La ventana indica el número de valores de la serie que se utilizan
    para calcular la media. Por defecto se usa una ventana de 5. El valor
    de la posición i es la media de los valores comprendidos en las posiciones
    [i-ventana, i] de la serie.
    El primer punto de la serie para el que se puede calcular la media móvil
    será "serie[ventana]". A los puntos anteriores se les asignará como valor
    de media móvil la correspondiente a este primer punto.
    '''
    pass


def similitud_coseno(serie_a, serie_b):
    ''' Similitud del coseno de dos series de valores
    
    ENTRADA: 
       - serie_a: primera serie de valores numéricos -> [float]
       - serie_b: segunda serie de valores numéricos -> [float]
    SALIDA: 
       - similitud del coseno entre ambas series -> float 

    Dadas dos series de valores:
        [a1, a2, ..., an]
        [bi, b2, ..., bn]
    Para calcular la similitud del coseno es necesario, en primer lugar,
    calcular los siguientes sumandos:
        aa = a1 * a1 + a2 * a2 + ... + an * an
        bb = b1 * b1 + b2 * b2 + ... + bn * bn
        ab = a1 * b1 + a2 * b2 + ... + an * bn
    A partir de ellos, la similitud del coseno entre las dos series se 
    calcula con la siguiente expresión:
        ab / (sqrt(aa) * sqrt(bb))
    '''
    pass


def busca_empresa_mas_parecida(precios, empresa, empresas):
    ''' Empresa más parecida a otra de una lista de empresas
    
    ENTRADA: 
       - empresa: nombre de la empresa de la que queremos buscar parecidas -> str
       - empresas: nombres de las empresas con las que comparar -> [str]
    SALIDA: 
       - empresa más parecida y diccionario de similitudes -> (str, {str: float}) 

    Toma como entrada el nombre de una empresa y un diccionario de cotizaciones.
    Produce como salida una tupla con dos informaciones:
        - El nombre de la empresa más parecida
        - Un diccionario con las similitudes con cada empresa
    Se usa la similitud del coseno sobre los incrementos para determinar cuál
    es la empresa con cotizaciones más parecidas.
    
    Para resolver este ejercicio seguiremos los siguientes pasos:
    - Cargar las cotizaciones de la 'empresa' en la lista 'precios_empresa' y
      calcular los incrementos en la lista 'inc_empresa'
    - Cargar las cotizaciones de la lista 'empresas' en el diccionario
      'precios_empresas' y calcular los correspondientes incrementos en
      el diccionario 'inc_empresas'
    - Calcular las similitudes de 'empresa' con cada una de las 'empresas'
      y guardarlas en el diccionario 'similitudes'
    - Calcular el nombre de la empresa más parecida con la siguiente instrucción:
            
            mas_parecida = max(similitudes, key=similitudes.get)
    '''
    pass

    