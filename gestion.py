from typing import ItemsView, List
from cursos import *
#Gestion general
def gestionG(Parametro,Lista,cantDatos):

    Parametro = Parametro.lower()
    if Parametro.__eq__('asc'):
        print("\nASC")
        asc(Lista,cantDatos)
    elif Parametro.__eq__('desc'):
        print("\nDESC")
        desc(Lista,cantDatos)
    elif Parametro.__eq__('avg'):
        print("\nAVG")
        avg(Lista,cantDatos)
    elif Parametro.__eq__('min'):
        print("\nMIN")
        min(Lista,cantDatos)
    elif Parametro.__eq__('max'):
        print("\nMAX")
        max(Lista,cantDatos)
    elif Parametro.__eq__('apr'):
        print("\nAprobado")
        estudiantes(Lista,cantDatos,'apr')
    elif Parametro.__eq__('rep'):
        print("\nReprobado")
        estudiantes(Lista,cantDatos,'rep')
      
    else:
        print("\nParametro Invalido:\n")
        print("|"+Parametro+"|")
    
#Ordena los datos ascendemente
def asc(Lista,cantDatos):
    asc = []
    for a in Lista:
       asc = a.Registros
    
    #for x in range(0,cantDatos):
        #print ("Nombre:", asc[x][0],"Nota:",asc[x][1])
  
    band = False
    while band == False:
        band = True
        for i in range(cantDatos-1):
            if asc[i][1] > asc[i+1][1]:
                auxNum=asc[i][1]
                asc[i][1] = asc[i+1][1]
                asc[i+1][1] = auxNum

                auxNombre=asc[i][0]
                asc[i][0] = asc[i+1][0]
                asc[i+1][0] = auxNombre
                band = False

    for x in range(0,cantDatos):
        print ("Nombre:", asc[x][0],"Nota:",asc[x][1])
    
#Ordena los daros Descendentemente
def desc(Lista,cantDatos):
    desc = []
    for a in Lista:
       desc = a.Registros
    
    #for x in range(0,cantDatos):
        #print ("Nombre:", desc[x][0],"Nota:",desc[x][1])

    band = False
    while band == False:
        band = True
        for i in range(cantDatos-1):
            if desc[i][1] < desc[i+1][1]:
                auxNum=desc[i][1]
                desc[i][1] = desc[i+1][1]
                desc[i+1][1] = auxNum

                auxNombre=desc[i][0]
                desc[i][0] = desc[i+1][0]
                desc[i+1][0] = auxNombre
                band = False

    for x in range(0,cantDatos):
        print ("Nombre:", desc[x][0],"Nota:",desc[x][1])

#Promedio de los datos
def avg(Lista,cantDatos):
    list = []
    avg = float(0)
    for a in Lista:
       list = a.Registros
    
    for x in range(0,cantDatos):
        avg = avg + float(list[x][1])
    avg = avg/ cantDatos
  
    print('El promedio es de: ',avg)

#Mayor nota
def max(Lista,cantDatos):
    max = float(0)
    list = []
    nombre = ""
    for a in Lista:
       list = a.Registros
    for x in range(0,cantDatos):
        if float(list[x][1]) > max:
            max = float(list[x][1])
            nombre = list[x][0]

    print("La nota mas alta es",max,"De: ",nombre)
       
#Menor nota
def min(Lista,cantDatos):
    min = float(100)
    list = []
    nombre = ""
    for a in Lista:
       list = a.Registros
    for x in range(0,cantDatos):
        if float(list[x][1]) < min:
            min = float(list[x][1])
            nombre = list[x][0]
    print("La nota mas baja es",min,"De: ",nombre)

#Estudiantes aprobados y desaprobados
def estudiantes(Lista,cantDatos,tipo):
    list = []
    ganaron=[]
    perdieron=[]
    cantPerdieron= 0
    cantGanaron= 0
    for a in Lista:
       list = a.Registros
    
    band = False
    while band == False:
        band = True
        for i in range(cantDatos-1):
            if list[i][1] < list[i+1][1]:
                auxNum=list[i][1]
                list[i][1] = list[i+1][1]
                list[i+1][1] = auxNum

                auxNombre=list[i][0]
                list[i][0] = list[i+1][0]
                list[i+1][0] = auxNombre
                band = False

    if tipo.__eq__('apr'):
   
        for x in range(0,cantDatos):
            if float(list[x][1])>60:
                ganaron.append(list[x])
                cantGanaron +=  1

        for x in range(0,cantGanaron):
             print("Nombre:", ganaron[x][0],"Nota:",ganaron[x][1])         
       
   
    if tipo.__eq__('rep'):        
    
        for x in range(0,cantDatos):
            if float(list[x][1])<60:
                perdieron.append(list[x])
                cantPerdieron +=  1
        
        for x in range(0,cantPerdieron):
             print("Nombre:", perdieron[x][0],"Nota:",perdieron[x][1]) 
  

       