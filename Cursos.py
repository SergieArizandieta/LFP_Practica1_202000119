from gestion import *

global lista
lista = list()

#Objeto Curso
class Curso:
    titulo = ''
    Registros =  []
    Parametros = [] 
   
#Registrar los datos al objeto
def registro(title,Lista,Parametros):
    if lista:
        del lista[:]
 
 
    curso = Curso()
    curso.titulo = title
    curso.Registros = Lista
    curso.Parametros = Parametros
    lista.append(curso)
    listar(len(Lista),len(Parametros))
  
#Mostrar los datos en consola
def listar(cantDatos,cantPara):         
    acces= 0
    gestionG('asc',[],0,acces)
    gestionG('desc',[],0,acces)
    gestionG('avg',lista,cantDatos,acces)
    gestionG('min',[],0,acces)
    gestionG('max',[],0,acces)
    gestionG('apr',[],0,acces)
    gestionG('rep',[],0,acces)
    acces= 1
    RGeneral= ""
    Rhtml = ""
   
    for a in lista:
         pass
         
    #for x in range(0,cantDatos):
        #print ("Nombre:", a.Registros[x][0],"Nota:",a.Registros[x][1])
   
    for x in range(0,cantDatos):
        RGeneral += ("\nNombre: "+ str( a.Registros[x][0])+" Nota: " + str(a.Registros[x][1]))

    for x in range(0,cantDatos):
        Rhtml += "<td>" + str(a.Registros[x][0]) + "</td>"
        Rhtml += "<td " + Marcador(float(a.Registros[x][1])) + ">" + str(a.Registros[x][1]) + "</td></tr>"
    
 
    for x in range(0,cantPara):
       
        gestionG(a.Parametros[x],lista,cantDatos,acces)
  
    ReporteG(lista,cantDatos,RGeneral,Rhtml)
