from asyncio.windows_events import NULL
import csv
import json
from operator import truediv
from tkinter import N

data = {}
data['Temporada'] = 2010
data['PilotoCampeon'] = 2010
data['EscuderiaCampeona'] = 2010
data['NuConstructores'] = 2010
data['NuPilotos'] = 2010
data['NuCarreras'] = 27
data['pilotos'] = []
data['carreras'] = []

dicCarreras= {
    "BHR" :[1,"Bahrein"],
    "AUS" :[2,"Australia"] ,
    "MYS" :[3,"Malasya"] ,
    "CHN" :[4,"China"] ,
    "ESP" :[5,"España"] ,
    "MON" :[6,"Mónaco"] ,
    "TUR" :[7,"Turqía"] ,
    "CAN" :[8,"Canadá"] ,
    "EUR" :[9,"Europa"] ,
    "GBR" :[10,"Gran Bretaña"],
    "GER" :[11,"Alemania"],
    "HUN" :[12,"Hungría"],
    "BEL" :[13,"Bélgica"],
    "ITA" :[14,"Italia"],
    "SIN" :[15,"Singapur"],
    "JPN" :[16,"Japón"],
    "RCO" :[17,"Corea del Sur"],
    "BRA" :[18,"Brasil"],
    "ABU" :[19,"Abu Dabi"]
}


def verificarPiloto(posiciones, abre):
    for pil in posiciones:
        try:
            print(pil["Ret"])
            if pil[0] == abre:
                return True
        except KeyError:
            pass
    return False



for car in dicCarreras:
    posiciones = []
    retirados = []
    nc = []
    lider = []
    pilotoLider = NULL
    with open('posiciones.json') as file:
        dataj = json.load(file)
        pilotosanalizados= 0
        abre = ""
        for col in dataj['pilotoPosiciones']:
            with open('puntos.json') as file2:
                dataj2 = json.load(file2)     
                for piloto in dataj2['pilotoPuntos']:
                    if piloto['Abreviacion'] == col ['Abreviacion']:
                        if pilotoLider==NULL or int(pilotoLider[car]) < int (piloto[car]):
                            pilotoLider = piloto 
                        posiciones.append({
                            col[car] : [piloto['Abreviacion'],piloto[car]]    #Falta posición en el mundial
                            })        
                lider = [pilotoLider['Abreviacion'],pilotoLider[car]]
        pilotosanalizados+1
        if pilotosanalizados == 28:
            break
    print(car)
    data['carreras'].append({
            'numero': dicCarreras[car][0],
            'nombre': "Gran Premio de "+dicCarreras[car][1],
            'abreviacion': car,
            'lugar': dicCarreras[car][1],
            'lider' : lider,
            'pole':NULL,
            'vueltaR':["Vet","1.3.2"],
            'posiciones':posiciones})
    

with open('posiciones.json') as file:
    dataj = json.load(file)
    for col in dataj['pilotoPosiciones']:
        data['pilotos'].append({
            'nombre': col['Piloto'],
            'nom':    col['Abreviacion'],
            'edad':NULL,
            'escuderia':NULL,
            'descripcion':[]})
with open('auto.json', 'w') as file:
    json.dump(data, file, indent=4)


data = NULL