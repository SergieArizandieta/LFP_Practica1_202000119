global lista
lista = list()

#Objeto Curso
class Curso:
    titulo = ''
    Registros =  []
    Parametros = [] 
   
#Registrar los datos al objeto
def registro(title,Lista,Parametros):
    curso = Curso()
    curso.titulo = title
    curso.Registros = Lista
    curso.Parametros = Parametros
    lista.append(curso)
    listar(len(Lista),len(Parametros))
  
#Mostrar los datos en consola
def listar(cantDatos,cantPara):
    for a in lista:
        print ("\nRegistros Finales\n",a.titulo, "-",a.Registros, "-", a.Parametros)

    print ("\nCurso:", a.titulo)

    for x in range(0,cantDatos):
        print ("Nombre:", a.Registros[x][0],"Nota:",a.Registros[x][1])
   
    for x in range(0,cantPara):
        print ("Parametro",x,":",a.Parametros[x])

