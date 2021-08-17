from tkinter import filedialog, Tk
from cursos import *
ListaNames = []
listNotas= []
listData = []
listParametros = []

       
#OPERACION De lectruta por Tokens (NUEVA)
#Intefaz para abrir el archivo 
def openExtra():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo LFP",
        initialdir = "./",
        filetypes = (
            ("archivos LFP", "*.lfp"),
            ("todos los archivos",  "*.*")
        )
    )
    if archivo is None:
        print('\nNo se seleccionó ningun archivo')
        return None
    else:
        texto = archivo.read()
        archivo.close()
        print('\n"Lectura exitosa"')
        return texto

#Purificacion de los datos
def purificacionExtra():
    text = openExtra()
    titulo = ""
    textTemp = ""

    for txt in text:
        if txt == "=":
            titulo = textTemp
            textTemp = ""
            #print(titulo)
        else:
            textTemp+=txt 
        if txt == "}":
            leertxt(textTemp)
            textTemp =""
    leerParameteos(textTemp)
    #print(listData)
    print(listParametros)

    registro(titulo,listData,listParametros)    

def leertxt(txt):
    textTemp = ""
    for text in txt:
        if text == "{" or text == "," or text == "\n" :
            pass
        else:
            textTemp += text
            if  text == ">":
                leerDatos(textTemp)
                textTemp = ""

def leerDatos(txt):
    look = False
    nombre= ""
    nota = ""
    textTemp = ""
    listaaux = [] 

    for text in txt:
        if text == "<":
            pass
        elif text == '"':
            look =True
            pass
        elif text == ' ' and look == False:
            pass
        else:
            if text == ";":
                look =False
                nombre = textTemp
                textTemp = ""
            else:
                if text == ">":
                    nota =textTemp
                textTemp += text
    
    listaaux.append(nombre)
    listaaux.append(nota)
    listData.append(listaaux)

def leerParameteos(txt):
    print(txt)
    textTemp=""
    for text in txt:
        if text ==" ":
            pass
        else:
            if text == ",":
                listParametros.append(textTemp)
                textTemp = ""
            else:
                textTemp+= text
        
#Antigua manera de lectura    
#Intefaz para abrir el archivo 
def open():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo LFP",
        initialdir = "./",
        filetypes = (
            ("archivos LFP", "*.lfp"),
            ("todos los archivos",  "*.*")
        )
    )
    if archivo is None:
        print('\nNo se seleccionó ningun archivo')
        return None
    else:
        texto = archivo.readlines()
        archivo.close()
        print('\n"Lectura exitosa"')
        return texto

#Purificacion de los datos
def purificacion():
    lista=[]
    text = open()
    parametros= []
    if text is not None:
        Chars = '={<">},' 
        CharAux = '={<">} ' 
        for x in range(len(text)):
            if (len(text)-1) != x:
                for specialChar in Chars:
                    text[x] = text[x].replace(specialChar, '').strip()
                text[x] = text[x].replace(";", ',').strip()
            else:
                for specialChar in CharAux:
                    text[x] = text[x].replace(specialChar, '').strip()   
      
        for x in range(1,len(text)-1):
            temp = text[x].split(',') 
            lista.append(temp)

        parametros = text[len(text)-1].split(',') 
    
        registro(text[0],lista,parametros)
  
    else:
        print('No se pudo analizar la entrada\n')
 
 