
from tkinter import DoubleVar, Tk , Scale , Label, X, LEFT, HORIZONTAL,SUNKEN,W,BOTTOM
from tkinter.constants import VERTICAL
from openpyxl import *

def ventana():
    root = Tk()
    ancho_ventana = 400
    alto_ventana = 400
    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    root.resizable(False,False)

    root.title("Practica 1")

    statusbar = Label(root,relief=SUNKEN, anchor=W)
    statusbar.pack(side=BOTTOM, fill=X)
    labels=[]
    lb1 = Label(root,text='VET')
    lb1.pack()
    labels.append(lb1)
    lb2 = Label(root,text='ALO')
    lb2.pack()
    labels.append(lb2)
    lb3 = Label(root,text='WEB')
    lb3.pack()
    labels.append(lb3)
    lb4 = Label(root,text='HAM')
    lb4.pack()
    labels.append(lb4)
    lb5 = Label(root,text='BUT')
    lb5.pack()
    labels.append(lb5)
    print(labels)
    def mostrarPosicionEnCarrera(numCarrera):
        for num in range(1,6):
            labels[num-1].config(text=suma[num][numCarrera+1])


    def show(event):
        s = 'El valor del control deslizante' + str(var.get())
        mostrarPosicionEnCarrera(int(var.get()))
    var=DoubleVar()
    scl = Scale(statusbar,orient=HORIZONTAL,length=400,from_=1,to=19,label='Arrastre el control deslizante',tickinterval=1,resolution=1,variable=var,activebackground='blue',state='active')
    scl.bind('<ButtonRelease-1>',show)
    scl.pack()

    root.mainloop()

#https://programmerclick.com/article/48241690471/





if __name__ == "__main__":
    excel=load_workbook('f:/Oscar/Documentos/Futbol/F1/2010.xlsx',data_only=True)
    sheet = excel['Hoja1']
    titulos=[   'Carrera',
                'BHR',
                'AUS',
                'MYS',
                'CHN',
                'ESP',
                'MON',
                'TUR',
                'CAN',	
                'EUR',
                'GBR',
                'GER',
                'HUN',	
                'BEL',	
                'ITA',
                'SIN',
                'JPN',	
                'RCO',
                'BRA',
                'ABU'
    ]
    pxp={
        1: 25,
        2: 18,
        3: 15,
        4: 12,
        5: 10,
        6: 8,
        7: 6,
        8: 4,
        9: 2,
        10:1
    }	
                                                                                        
    #Obtener Datos
    Datos= []
    for celda_fila in range(ord('A'),ord('V')):
        columna=[]
        for celda_columna in range(1,29):
            columna.append(sheet[chr(celda_fila)+str(celda_columna)].value)
        Datos.append(columna)
    Carreras=[]
    for col in range(0,len(Datos[0])):
        columna=[]
        for d in Datos:
            columna.append(d[0])
        Carreras.append(columna)
    #print(Datos[1])
    suma=[
        ['Car','BHR','AUS','MYS','CHN','ESP','MON','TUR','CAN','EUR','GBR','GER','HUN','BEL','ITA','SIN','JPN','RCO','BRA','ABU']
        ]

    for piloto in Datos[1][1:]:
        suma.append([piloto[:3],0])

    for Carrera in Datos[2:]:
        for n,posicion in enumerate(Carrera[1:]):
            puntos=0
            if posicion!='Ret' and posicion!=None and posicion!='DNS' and piloto:
                if int(posicion)<11:
                    puntos=pxp[int(posicion)]
            ultimo=suma[n+1].pop()
            suma[n+1].append(ultimo)
            suma[n+1].append(ultimo+puntos)
        
    for piloto in suma:
        print(piloto)
    ventana()


    
