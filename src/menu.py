"""
    Menu main of program 
"""

from .modules import ExperimentalData
from .utils import validations


def run():

    while True:
        print("\n¿Que desea hacer?\n")
        print("1. ✏️ Agregar un experimento")
        print("2. 🔍 Visualizar los experimentos")
        print("3. 🧮 Realizar cálculos")
        print("4. 📊 Comparar experimentos")
        print("5. 📑 Generar informe final")
        print("6. 💾 Exportar informe a archivo de texto")
        print("7. 🔚 Salir")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            resultsObtained = []

            print("\n-------------------")
            print("✏️ Agregar un experimento")
            print("-------------------\n")
            experimentName = input("Ingrese el nombre del experimento: ")
            completionDate = input(
                "Ingrese la fecha de realización del experimento (dd/mm/yyyy): "
            )

            while not validations.isValidDate(completionDate):
                print(
                    "⚠️ Debes ingresar una fecha en el formato 'dd/mm/yyyy'. Ejemplo: '12/12/2024', '30/11/2023', etc."
                )
                completionDate = input(
                    "Ingrese la fecha de realización del experimento (dd/mm/yyyy): "
                )

            while True:  # Internal bucle for the category
                print("\nCategorías:")
                print("1. 🧪 Química")
                print("2. ☣️  Biología")
                print("3. 👨‍🔬 Física")
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

            print(f"\nHas seleccionado la categoría: {experimentCategory}")
            try:
                print(
                    "\n--------------------------------------------------------------------------"
                )
                print(
                    "ℹ️ A continuación, debes ingresar los resultados que arrojó el experimento (ingresa 3 como mínimo)."
                )
                print(
                    "--------------------------------------------------------------------------\n"
                )
                while True:  # Bucle for validation one minimum of 3 results
                    minResultsObtained = int(
                        input("Cuántos resultados obtuvo el experimento: ")
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
                                    f" 🔹 Ingrese el resultado número {i+1} para el experimiento '{experimentName}': "
                                )
                            )
                            resultsObtained.append(result)
                            break
                        except ValueError:
                            print(
                                "⛔ Debes ingresar un número válido para el experimento."
                            )

            except ValueError:
                print(
                    "Debes ingresar un número de resultados obtenidos del experimento."
                )

            experimentsData = [
                {
                    "experimentName": experimentName,
                    "completionDate": completionDate,
                    "experimentCategory": experimentCategory,
                    "resultsObtained": resultsObtained,
                }
            ]            
            ExperimentalData.addExperiment(experimentsData)
            print("\n✅ Experimento agregado con éxito.")

        elif option == "2":
            ExperimentalData.printAllExperiments()
        elif option == "3":
            # Functions.CalculosEstadisticos()
            pass
        elif option == "4":
            # Functions.CalculosEstadisticos()
            pass
        elif option == "5":
            # Functions.GenerarInformes()
            pass
        elif option == "6":
            # Functions.ExportarReporte()
            pass
        elif option == "7":
            print("Has salido del programa.")
            break
        else:
            print("Opción inválida")
