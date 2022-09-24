from asyncio.windows_events import NULL
import json
data = {}
data['Temporada'] = 2010
data['PilotoCampeon'] = 2010
data['NuCarreras'] = 19
data['pilotos'] = []
data['escuderias'] = []
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


escuderia = ""
nuEscuderias = 0
puntosConst = 0

with open('escuderias.json') as file:
    dataj = json.load(file)
    for const in dataj['escuderias']:
        nuEscuderias+=1
        print(const['Puntos'])
        if int(const['Puntos']) > puntosConst:
            escuderia = const['Escuderia']
            puntosConst = int(const['Puntos'])
        colores = const['Colores'].split("|")
        data['escuderias'].append({
            'nombre': const['Nombre'],
            'escuderia': const['Escuderia'],
            'EscuderiaAbre': const['EscuderiaAbre'],
            'colores': colores,
            'chasis': const['Chasis'],
            'motor': const['Motor'],
            'puntos': const['Puntos']
            })





data['NuEscuderias'] = nuEscuderias
data['EscuderiaCampeona'] = escuderia
data['EscuderiaCampeonaPuntos'] = str(puntosConst)



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
    

nuPilotos = 0

with open('pilotos.json') as file:
    dataj = json.load(file)
    for pil in dataj['pilotos']:
        if pil['Piloto']=='True':
            nuPilotos+=1
        data['pilotos'].append({
            'nombre' : pil['Nombre Piloto'],
            'nom': pil['Abreviacion'],
            'escuderia' : pil['Escuderia'],
            'numCarreras' : pil['NoCarreras']
        })        


        
data['NuPilotos'] = nuPilotos


with open('auto.json', 'w') as file:
    json.dump(data, file, indent=4)


data = NULL


