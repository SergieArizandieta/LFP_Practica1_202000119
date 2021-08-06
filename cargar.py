from tkinter import filedialog, Tk
from Cursos import *

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
        print('No se seleccionó ningun archivo\n')
        return None
    else:
        texto = archivo.readlines()
        archivo.close()
        print('Lectura exitosa\n')
        return texto

#Purificacion de los datos
def purificacion():
    text = open()
    lista = []
    if text is not None:
        Chars = '={<">}, ' 
        CharAux = '={<">} ' 
        for x in range(len(text)):
            if (len(text)-1) != x:
                for specialChar in Chars:
                    text[x] = text[x].replace(specialChar, '').strip()
                text[x] = text[x].replace(";", ',').strip()
            else:
                for specialChar in CharAux:
                    text[x] = text[x].replace(specialChar, '').strip()   
        for txt in text:
            print(txt)
        for x in range(1,len(text)-1):
            temp = text[x].split(',') 
            lista.append(temp)

        
        parametros = text[len(text)-1].split(',') 
       
        print("\n",parametros)   
        print("\n",lista)  
        print("\n",text)
        registro(text[0],lista,parametros)

    else:
        print('No se pudo analizar la entrada\n')






