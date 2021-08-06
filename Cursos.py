global lista
lista = list()

class Curso:
    titulo = ''
    Registros =  []
    Parametros = [] 
   
def registro(title,Lista,Parametros):
    curso = Curso()
    curso.titulo = title
    curso.Registros = Lista
    curso.Parametros = Parametros
    lista.append(curso)
    listar(len(Lista),len(Parametros))
    #print("\nRegistros:\n",title,Lista,Parametros)

def listar(cantDatos,cantPara):
    for a in lista:
        print ("\nRegistros Finales\n",a.titulo, "-",a.Registros, "-", a.Parametros)

    print ("\nCurso:", a.titulo)

    for x in range(0,cantDatos):
        print ("\nNombre:", a.Registros[x][0],"Nota:",a.Registros[x][1])
   
    for x in range(0,cantPara):
        print ("\nParametro",x,":",a.Parametros[x])

