  
from tkinter import filedialog, Tk

listaT = []

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


def abrir():
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
        texto = archivo.read()
        archivo.close()
        print('Lectura exitosa\n')
        return texto

def Carga():
    txt = abrir()
    if txt is not None:
        print(txt)
    else:
        print('Error lectura')

        
    
def Carga1():
    txt = open()
    if txt is not None:
        print(len(txt))
        listado = []
        for i in txt:
            textotemp = i.replace(' ','').strip()  
            print(textotemp) 
            #listado.append(textotemp)    

        
        for lin in listado:
            print(lin) 
        


    else:
        print('No se pudo analizar la entrada\n')




def Carga2():
    txt = abrir()
    if txt is not None:
        print(txt)
        if(len(txt) > 0):
            for c in txt:
                if c == '\n'or c == ' ':
                    #Se ignora este caracter
                        #print(str(ord(c)) + ' - \\n')
                    pass
                elif c == ' ' :
                    #Se ignora este caracter
                        #print(str(ord(c)) + ' - `space`')
                    pass
                else:
                    auxL = [ord(c), str(c)]
                    listaT.append(auxL)
            for elemento in listaT:
                print('Ascii: ' + str(elemento[0]) + ' - Caracter: ' + str(elemento[1]))
        else:
            print('No hay texto para analizar\n')
    else:
        print('No se pudo analizar la entrada\n')