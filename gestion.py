from typing import ItemsView, List
from cursos import *
from reportes import *

#Variables Globales
Rdesc =""
Ravg =""
Rmin =""
Rmax =""
Rapr =""
Rrep =""

#Gestion general
def gestionG(Parametro,Lista,cantDatos,acces):

    Parametro = Parametro.lower()
    if Parametro.__eq__('asc'):
        asc(Lista,cantDatos,acces)
    elif Parametro.__eq__('desc'):
        desc(Lista,cantDatos,acces)
    elif Parametro.__eq__('avg'):
        avg(Lista,cantDatos,acces)
    elif Parametro.__eq__('min'):
        min(Lista,cantDatos,acces)
    elif Parametro.__eq__('max'):
        max(Lista,cantDatos,acces)
    elif Parametro.__eq__('apr'):
        estudiantes(Lista,cantDatos,'apr',acces)
    elif Parametro.__eq__('rep'):
        estudiantes(Lista,cantDatos,'rep',acces)
      
    else:
        print("\nParametro Invalido:\n")
        print("|"+Parametro+"|")
    
#Ordena los datos ascendemente
def asc(Lista,cantDatos,acces):
    asc = []
    for a in Lista:
       asc = a.Registros
    
    #for x in range(0,cantDatos):
        #print ("Nombre:", asc[x][0],"Nota:",asc[x][1])
  
    band = False
    while band == False:
        band = True
        for i in range(cantDatos-1):
           
            if float(asc[i][1]) > float(asc[i+1][1]):
             
                auxNum=asc[i][1]
                asc[i][1] = asc[i+1][1]
                asc[i+1][1] = auxNum

                auxNombre=asc[i][0]
                asc[i][0] = asc[i+1][0]
                asc[i+1][0] = auxNombre
                band = False
   
    Reportasc(asc,cantDatos,acces)
      
#Ordena los daros Descendentemente
def desc(Lista,cantDatos,acces):
    desc = []
    for a in Lista:
       desc = a.Registros
    
    #for x in range(0,cantDatos):
        #print ("Nombre:", desc[x][0],"Nota:",desc[x][1])

    band = False
    while band == False:
        band = True
        for i in range(cantDatos-1):
            if float(desc[i][1]) < float((desc[i+1][1])):
                auxNum=desc[i][1]
                desc[i][1] = desc[i+1][1]
                desc[i+1][1] = auxNum

                auxNombre=desc[i][0]
                desc[i][0] = desc[i+1][0]
                desc[i+1][0] = auxNombre
                band = False
    Reportdesc(desc,cantDatos,acces)

#Promedio de los datos
def avg(Lista,cantDatos,acces):
    list = []
    avg = float(0)
    for a in Lista:
       list = a.Registros
    
    for x in range(0,cantDatos):
        avg = avg + float(list[x][1])
    avg = avg/ cantDatos
    Reportavg(avg,acces)
  
#Mayor nota
def max(Lista,cantDatos,acces):
    max = float(0)
    list = []
    nombre = ""
    nombreHTML = ""
    for a in Lista:
       list = a.Registros
    for x in range(0,cantDatos):
        if float(list[x][1]) > max:
            max = float(list[x][1])
            
    for x in range(0,cantDatos):
        if float(list[x][1]) == max:
            nombre += (list[x][0] + "\n ")
            nombreHTML  += (list[x][0] + "<br>")
    Reportmax(max,nombre,nombreHTML,acces)
       
#Menor nota
def min(Lista,cantDatos,acces):
    min = float(10000)
    list = []
    nombre = ""
    nombreHTML=""
    for a in Lista:
       list = a.Registros
    for x in range(0,cantDatos):
        if float(list[x][1]) < min:
            min = float(list[x][1])
            
            
    for x in range(0,cantDatos):
        if float(list[x][1]) == min:
            nombre += (list[x][0] + "\n ")
            nombreHTML  += (list[x][0] + "<br>")
  
    Reportmin(min,nombre,nombreHTML,acces)

#Estudiantes aprobados y desaprobados
def estudiantes(Lista,cantDatos,tipo,acces):
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
            if float(list[x][1])>=61:
                ganaron.append(list[x])
                cantGanaron +=  1
        Reporapr(ganaron,cantGanaron,acces)
        
       
   
    if tipo.__eq__('rep'):        
    
        for x in range(0,cantDatos):
            if float(list[x][1])<61:
                perdieron.append(list[x])
                cantPerdieron +=  1
        Reporrep(perdieron,cantPerdieron,acces)
        

       