'''
Un agricultor realiza la siembra de 3 cultivos -papa -yuca -zanahoria;
el cultivo de papá requiere una cantidad x de riego a la semana, la yuca y la zanahoria también.
Consultar en internet dicho procedimiento y establecer esta característica en un programa.
PD litros de agua regados ?
1er día: cuántos litros
2do día //
// //
7mo día : //
'''
import os

cultivo = int(input('\t..:Granja menesex:..\n¿Que cultivo desea analizar?\n[1]Papa\n[2]Yuca\n[3]Zanahoria\n --> '))
if cultivo == 1:
    cultivoStr = 'Papa'
if cultivo == 2:
    cultivoStr = 'Yuca'
if cultivo == 3:
    cultivoStr = 'Zanahoria'
    
print('\t..:Tabla de referencia (Litros por semana):..\n\nPapa = 3 Días (19-28 Litros por semana) \nYuca = 2 Días (37-45 Litros por semana) \nZanahoria= 2 Días (34-42 Litros por semana)\n')

#entrada
#cuántos litos de agua le ha regado a cada cultivo x día?
sumLitrosTotal = 0
for i in range(6):
    print('\t.:Cantidad de litros regados (día ', (i+1), '):.')
    litros = int(input(f'({cultivoStr}) --> '))
    sumLitrosTotal += litros

os.system('cls')

optimo = False #Se asume que no es óptimo

#Papas (¿Suficiente?)
if 19 <= sumLitrosTotal <= 28:
        optimo = True
        
#Yuca (¿Suficiente o no?)
if 37 <= sumLitrosTotal <= 45:
        optimo = True

#Zanahoria (¿Suficiente o no?)
if 34 <= sumLitrosTotal <= 42:
        optimo = True

#salida
print('\t..:Tabla de referencia (Litros por semana):..\nPapa = 19-28 \nYuca = 37-45 \nZanahoria= 34-42')

if optimo == True:
    print(f'\n\t.:({cultivoStr}) = Dentro del rango óptimo:.\nLitros x semana ({sumLitrosTotal})')
if optimo == False:
    print(f'\n\t.:({cultivoStr}) = Fuera del rango óptimo:.\nLitros x semana ({sumLitrosTotal})')



    
    

    
