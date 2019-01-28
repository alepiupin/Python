'''
Created on 25 oct. 2018

@author: alejandro
'''
x = [(101,4),(4, 4), (5,100),(5, 34),(5, 45)]
for recorrido in range(1,len(x)-1):
    for posicion in range(len(x)-recorrido):
        if x[posicion][1] > x[posicion+1][1]:
           temp = x[posicion]
           x[posicion] = x[posicion+1]
           x[posicion + 1] = temp
   
print (x)
    