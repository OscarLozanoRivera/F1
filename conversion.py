import csv
import json

#Posiciones

data = {}
data['pilotoPosiciones'] = []

with open('2010Posiciones.csv', newline='') as pos:  
    reader = csv.DictReader(pos)
    for col in reader:
        data['pilotoPosiciones'].append(col)

print(data['pilotoPosiciones'])
with open('posiciones.json', 'w') as file:
    json.dump(data, file, indent=4)


#Puntos

data = {}
data['pilotoPuntos'] = []

with open('2010Puntos.csv', newline='') as pos:  
    reader = csv.DictReader(pos)
    for col in reader:
        data['pilotoPuntos'].append(col)

print(data['pilotoPuntos'])
with open('puntos.json', 'w') as file:
    json.dump(data, file, indent=4)