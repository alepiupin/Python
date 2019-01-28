'''
Created on 28 nov. 2018

@author: jorge
'''


def maximo(lista_x):
    maximo = None
    for x in lista_x:
        if maximo == None or maximo < x:
            maximo = x
    return maximo


def maximo2(diccionario):
    maximo = list(diccionario.keys())[0]
    for x in diccionario.keys():
        if diccionario[maximo]<diccionario[x]:
            maximo = x
    return maximo

def maximo3(diccionario):
    maximo = list(diccionario.keys())[0]
    for x in diccionario.keys():
        if len(diccionario[maximo])<len(diccionario[x]):
            maximo = x
    
    return maximo

if __name__ == '__main__':
    diccionario = {1:"hola", 2:"pepe", 
                   3:"juan", 4:"pili", 5:"remo", 
                   6:"pelota", 7:"nuez", 8:"platano"}
    maximo = max(diccionario, 
                 key = diccionario.get)
    print(maximo)
    maximo = maximo2(diccionario)
    print(maximo)
    maximo = max(diccionario, 
                 key = lambda x: len(diccionario.get(x)))
    print(maximo)
    maximo = maximo3(diccionario)
    print(maximo)

