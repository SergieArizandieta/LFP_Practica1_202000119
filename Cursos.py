from gestion import *

global lista
lista = list()

#Objeto Curso
class Curso:
    titulo = ''
    Registros =  []
    Parametros = [] 
   
#Registrar los datos al objeto
def registro(title,Lista,Parametros,text):
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
    for a in lista:
         print ("--------Bienvenido--------")

   

    #for x in range(0,cantDatos):
        #print ("Nombre:", a.Registros[x][0],"Nota:",a.Registros[x][1])
   
    for x in range(0,cantPara):
        gestionG(a.Parametros[x],lista,cantDatos)
    
    ReporteG(lista,cantDatos)
