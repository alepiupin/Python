'''
Created on 28 dic. 2018

@author: alejandro
'''

from whatsapp import *

FICHERO = '../data/bigbangtheory_es.txt'
plt.rcParams["figure.figsize"] = [10, 8]
NUM_PALABRAS_NUBE = 100

def test_indexa_por_usuario(log):
    indice_por_usuario = indexa_por_usuarios(log)
    for usuario in sorted(indice_por_usuario):
        print("Mensajes para ", usuario,":", len(indice_por_usuario[usuario]))
        print("Primer mensaje de", usuario,":", indice_por_usuario[usuario][0])
        
def test_indexa_por_campo(log):
    indice_por_usuario = indexa_por_campo(log, 'usuario')
    for usuario in sorted(indice_por_usuario):
        print("Mensajes para ", usuario,":", len(indice_por_usuario[usuario]))
        print("Primer mensaje de", usuario,":", indice_por_usuario[usuario][0])
if __name__ == '__main__':
    
    # Test de la función carga_log
    log = carga_log(FICHERO, debug=True)
  
    #Test indexa por usuario
   # test_indexa_por_usuario(log)
    test_indexa_por_campo(log)
    