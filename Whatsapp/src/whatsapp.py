'''
Created on 28 dic. 2018

@author: alejandro
'''
import datetime
from datetime import timedelta
import re
from collections import namedtuple, Counter
import matplotlib.pyplot as plt
from pywt import _thresholding

Mensaje = namedtuple('Mensaje', 'fecha hora usuario texto')
    
ANDROID_RE = r'(\d\d?/\d\d?/\d\d?) (\d\d?:\d\d) - ([^:]+): (.+)'
IOS_RE = r'\[(\d\d?/\d\d?/\d\d?) (\d\d?:\d\d):\d\d\] ([^:]+): (.+)'

def carga_log(fichero, os='android', debug=False):
    if os=='android':
        regex = ANDROID_RE
    elif os=='ios':
        regex = IOS_RE
    else:
        raise Exception('OS no permitido')
        
    log = []
    with open(fichero, encoding='utf8') as f:        
        for linea in f:
            # Aplicamos la expresión regular sobre cada línea
            matches = re.findall(regex, linea)
            if matches:  # Si se encuentran coincidencias para los patrones
                fecha_str, hora_str, usuario, texto = matches[0]
                fecha = datetime.datetime.strptime(fecha_str, '%d/%m/%y').date()
                hora = datetime.datetime.strptime(hora_str, '%H:%M').time()
                log.append(Mensaje(fecha,hora,usuario, texto))
    if debug:
        print(str(len(log)) + " mensajes leidos")
        usuarios = list({x.usuario for x in log})
        fechas = [x.fecha for x in log]
        print("Usuarios: ",usuarios ,  "\n" + "Intervalo de fechas: ",fechas[0] , "->" ,fechas[-1])
        
    return log

def indexa_por_usuarios(log):
    res = dict()
    for x in log:
        if x.usuario in res:
            res[x.usuario].append(x)
        else: 
            res.update({x.usuario : [x]})
        
    return res

def indexa_por_campo(log,campo):
    result = dict()
    for x in log:
        key = getattr(x, campo)
        if  key in result:
            result[key].append(x)
        else:
            result[key] = [x]
    return result