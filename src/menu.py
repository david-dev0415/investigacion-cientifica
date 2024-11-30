"""
    Menu main of program 
"""

from .modules import ExperimentalData
from .utils import validations
from .utils import goBack


def run():

    menu = """
¿Qué deseas hacer?

1. ✏️  Agregar un experimento
2. 🔍 Visualizar los experimentos
3. 🧮 Realizar cálculos
4. 📊 Comparar experimentos
5. 📑 Generar informe final
6. 💾 Exportar informe a archivo de texto
7. 🗑️  Eliminar un experimento
8. 🔚 Salir  
    """

    while True:
        print(menu)
        option = input("Seleccione una opción: ")

        if option == "1":
            resultsObtained = []

            print(
                "\n--------------------------------------------------------------------------"
            )
            print("✏️  Agregar un experimento")
            print(
                "--------------------------------------------------------------------------\n"
            )

            # menu_secundario()

            experimentName = input("Ingrese el nombre del experimento: ").capitalize()
            completionDate = input(
                "Ingrese la fecha de realización del experimento (dd/mm/yyyy): "
            )

            # print(
            #     "\n--------------------------------------------------------------------------"
            # )
            # inputBack = input("\nDigite 0 o 'Regresar' para volver al menú anterior: ")
            # goBack(inputBack)
            # print(
            #     "\n--------------------------------------------------------------------------"
            # )

            while not validations.isValidDate(completionDate):
                print(
                    "\n⚠️ Debes ingresar una fecha en el formato 'dd/mm/yyyy'. Ejemplo: '12/12/2024', '30/11/2023', etc.\n"
                )
                completionDate = input(
                    "Ingrese la fecha de realización del experimento (dd/mm/yyyy): "
                )

            while True:  # Internal bucle for the category
                print("\nCategorías:")
                menuCategory = """
    1. 🧪 Química
    2. ☣️  Biología
    3. 👨 Física
                """
                print(menuCategory)
                experimentCategory = input("Ingrese la categoría del experimento: ")

                if experimentCategory == "1":
                    experimentCategory = "Química"
                    break  # Exit of the internal bucle
                elif experimentCategory == "2":
                    experimentCategory = "Biología"
                    break
                elif experimentCategory == "3":
                    experimentCategory = "Física"
                    break
                else:
                    print("⚠️ Debes seleccionar una categoría válida. Intenta de nuevo.")

            print(f"Has seleccionado la categoría: {experimentCategory}\n")
            try:
                print(
                    "ℹ  A continuación, debes ingresar los resultados que arrojó el experimento (ingresa 3 como mínimo).\n"
                )
                while True:  # Bucle for validation one minimum of 3 results
                    minResultsObtained = int(
                        input("¿Cuántos resultados obtuvo el experimento?: ")
                    )
                    if minResultsObtained >= 3:
                        break
                    else:
                        print(
                            "\n⛔ Debes ingresar al menos 3 resultados para el experimento. Intenta de nuevo."
                        )

                for i in range(minResultsObtained):
                    while True:
                        try:
                            result = float(
                                input(
                                    f"\n   🔹 Ingrese el resultado número {i+1} para el experimiento '{experimentName}': "
                                )
                            )
                            resultsObtained.append(result)
                            break
                        except ValueError:
                            print(
                                "⛔ Debes ingresar un número válido para el experimento."
                            )
                experimentsData = [
                    {
                        "experimentName": experimentName,
                        "completionDate": completionDate,
                        "experimentCategory": experimentCategory,
                        "resultsObtained": resultsObtained,
                        "experimentId": len(ExperimentalData.listExperimentalData) + 1,
                    }
                ]
                ExperimentalData.addExperiment(experimentsData)
                print(
                    "\n--------------------------------------------------------------------------"
                )
                print("✅ Experimento agregado con éxito.")
                print(
                    "--------------------------------------------------------------------------"
                )

            except ValueError:
                print(
                    "\n⛔ Debes ingresar un número de resultados obtenidos del experimento."
                )
        elif option == "2":
            print(
                "\n--------------------------------------------------------------------------"
            )
            print("🔍 Visualizar los experimentos")
            print(
                "--------------------------------------------------------------------------\n"
            )
            ExperimentalData.printAllExperiments()
        elif option == "3":
            print(
                "\n--------------------------------------------------------------------------"
            )
            print("🧮 Realizar cálculos")
            print(
                "--------------------------------------------------------------------------\n"
            )
            ExperimentalData.calculatedResults()
        elif option == "4":
            print(
                "\n--------------------------------------------------------------------------"
            )
            print("🔍 Comparando experimentos...")
            print(
                "--------------------------------------------------------------------------\n"
            )
            ExperimentalData.compareExperiments()
            pass
        elif option == "5":
            # Functions.GenerarInformes()
            pass
        elif option == "6":
            ExperimentalData.exportExperimentsToFile()

        elif option == "7":
            print(
                "\n--------------------------------------------------------------------------"
            )
            print("🗑️  Eliminar un experimento")
            print(
                "--------------------------------------------------------------------------\n"
            )
            ExperimentalData.deleteExperiment()

        elif option == "8" or option.lower() == "salir":
            print("Has salido del programa.")
            break
        else:
            print("Opción inválida")


def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Ir al menú secundario")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ")

        print("1. Ir al menú secundario")
        print("0. Salir")

        if opcion == "1":
            menu_secundario()
        elif opcion == "0":
            print("👋 Saliendo...")
            break
        else:
            print("⚠️ Opción no válida. Inténtelo de nuevo.")


def menu_secundario():
    while True:
        print("\nMenu Secundario")
        print("1. Realizar alguna acción")
        print("0. Regresar al menú principal")

        inputBack = input("\nDigite 0 o 'Regresar' para volver al menú anterior: ")

        if inputBack.lower() == "regresar" or inputBack == "0":
            print("🔙 Regresando...")
            return  # Esto regresa al menú principal
        elif inputBack == "1":
            print("🔧 Realizando alguna acción...")
        else:
            print("⚠️ Opción no válida. Inténtelo de nuevo.")


# Ejecutar el menú principal
# menu_principal()
