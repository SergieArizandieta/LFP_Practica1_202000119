from cargar import *
from reportes import *

if __name__ == "__main__":
    #Menu desplegado
    def menu():
        print('1.Cargar archivo\n2.Mostrar reporte en consola\n3.Exportar reporte\n4.Salir')
    print("\n----------Bienvenido----------\n")
    menu()

    option = int(input("Ingrese una opcion: "))

    while option !=0:
        if option == 1:
            purificacionExtra()
            #purificacion()
        elif option == 2:
            MostrarReportsConsole()
        elif option == 3:
            GenerarReportes()
        elif option == 4:
            print("\nGracias por usar!")
            exit()
        else:
            print("Opcion invalida.")

        print()
        menu()
        option = int(input("Ingrese una opcion: "))
