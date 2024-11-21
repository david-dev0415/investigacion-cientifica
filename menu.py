'''
  Menu main of program 
'''
def run():
      
    while True:
        print("\nWhat do you want to do?")
        print("\n1. Agregar un experimento")
        print("\n2. Visualizar los experimentos")
        print("\n3. Realizar cálculos")
        print("\n4. Comparar experimentos")
        print("\n5. Generar informe final")
        print("\n6. Exportar informe a archivo de texto")
        print("\n7. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            pass
            #Functions.Registrar(listaExperimentos)
        elif opcion == "2":
            #Functions.Visualizar(listaExperimentos)
            pass
        elif opcion == "3":
            #Functions.CalculosEstadisticos()
            pass
        elif opcion == "4":
            #Functions.CalculosEstadisticos()
            pass
        elif opcion == "5":
            #Functions.GenerarInformes()
            pass
        elif opcion == "6":
            #Functions.ExportarReporte()
            pass
        elif opcion == "7":
            print("Has salido del programa.")
            break
        else:
            print("Opción inválida")