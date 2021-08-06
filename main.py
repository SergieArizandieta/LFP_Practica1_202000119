from cargar import *

#Menu desplegado
def menu():
    print('1.Cargar archivo\n2.Mostrar reporte en consola\n3.Exportar reporte\n4.Salir')

menu()
option = int(input("Ingrese una opcion: "))

while option !=0:
    if option == 1:
        print("Opcion 1")
        purificacion()
    elif option == 2:
        print("Opcion 2")
        Exportconsole()
    elif option == 3:
        print("Opcion 3")
       
    elif option == 4:
        print("Opcion 4")
        exit()
    else:
        print("Opcion invalida.")

    print()
    menu()
    option = int(input("Ingrese una opcion: "))
