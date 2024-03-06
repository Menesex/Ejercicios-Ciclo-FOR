'''
Un turista realiza un viaje de punto A a un punto B, dentro del rango del punto A al puno B
Debe realizar varias escalas las cuales depeneden de el realizar

diseñe un programa que permita ingresar la cantidad de escalas dentro de las cuales
el turista debe ingresar la distancia a recorrer e ir sumando cada una, al final decir cuanta distancia y etapas realizó
'''
import os
os.system('cls')
etapas = int(input('Ingrese la cantidad de etapas\n -->'))
sumDistancia = 0
for i in range(etapas):
    print ('Distancia recorrida en la etapa ',(i+1))
    distancia = int(input('--> '))
    sumDistancia += distancia

#salida
print(f'Distancia recorrida = {sumDistancia}\nEtapas realidazas = {etapas}')
    
    
    
    