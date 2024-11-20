import Functions


# Menú para la interacción con el usuario
def menu():
    listaExperimentos = []
    while True:
        print("\nQué desea hacer?")
        print("\n1. Agregar un experimento")
        print("\n2. Visualizar los experimentos")
        print("\n3. Realizar cálculos")
        print("\n4. Comparar experimentos")
        print("\n5. Generar informe final")
        print("\n6. Exportar informe a archivo de texto")
        print("\n7. Salir")

        opcion = input("Selecciones una opción: ")

        if opcion == "1":
            Functions.Registrar(listaExperimentos)
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            pass
        elif opcion == "7":
            print("Ha salido del programa")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
