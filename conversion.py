import csv
import json

#Posiciones

data = {}
data['pilotoPosiciones'] = []

with open('2010Posiciones.csv', newline='') as pos:  
    reader = csv.DictReader(pos)
    for col in reader:
        data['pilotoPosiciones'].append(col)

#print(data['pilotoPosiciones'])
with open('posiciones.json', 'w') as file:
    json.dump(data, file, indent=4)


#Constructores

data = {}
data['escuderias'] = []

with open('2010Escuderias.csv', encoding='utf-8-sig', newline='') as pos:  
    reader = csv.DictReader(pos)
    for col in reader:
        data['escuderias'].append(col)

with open('escuderias.json', 'w') as file:
    json.dump(data, file, indent=4)


#Pilotos

data = {}
data['pilotos'] = []

with open('2010Pilotos.csv', encoding='utf-8-sig', newline='') as pos:  
    reader = csv.DictReader(pos)
    for col in reader:
        data['pilotos'].append(col)

with open('pilotos.json', 'w') as file:
    json.dump(data, file, indent=4)
# for a in data['pilotos']:
#     print(a)


#Puntos

data = {}
data['pilotoPuntos'] = []

with open('2010Puntos.csv', newline='') as pos:  
    reader = csv.DictReader(pos)
    for col in reader:
        data['pilotoPuntos'].append(col)

#print(data['pilotoPuntos'])
with open('puntos.json', 'w') as file:
    json.dump(data, file, indent=4)