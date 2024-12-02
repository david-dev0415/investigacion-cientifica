"""
    Menu main of program 
"""

from .modules import ExperimentalData
from .utils import validations
from colorama import Fore, init, Back
from .utils.message import warningMessage, errorMessage

# from .utils import goBack


def run():

    init(autoreset=True)

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
            print(Fore.RED + Back.WHITE + "✏️  Agregar un experimento")
            print(
                "--------------------------------------------------------------------------\n"
            )

            experimentName = input("Ingrese el nombre del experimento: ").capitalize()
            while not experimentName:
                warningMessage(
                    " El campo no puede estar vacío. Por favor, ingrese el nombre del experimento."
                )
                experimentName = input(
                    "Ingrese el nombre del experimento: "
                ).capitalize()

            completionDate = input(
                "Ingrese la fecha de realización del experimento (dd/mm/yyyy): "
            )

            while not validations.isValidDate(completionDate):
                warningMessage(
                    " Debes ingresar una fecha en el formato 'dd/mm/yyyy'. Ejemplo: '12/12/2024', '30/11/2023', etc."
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
                    warningMessage(
                        " Debes seleccionar una categoría válida. Intenta de nuevo."
                    )

            print(f"Has seleccionado la categoría: {experimentCategory}\n")
            try:
                print(
                    " 📏 A continuación, debes ingresar los resultados que arrojó el experimento (ingresa 3 como mínimo).\n"
                )
                while True:
                    inputValue = input("¿Cuántos resultados obtuvo el experimento?: ")

                    if inputValue.strip() == "":
                        warningMessage(
                            " El campo no puede estar vacío. Por favor, ingrese un valor."
                        )
                        continue

                    try:
                        minResultsObtained = int(inputValue)
                        if minResultsObtained >= 3:
                            break
                        else:
                            warningMessage(
                                " Debes ingresar un número entero mayor o igual a 3. Intenta de nuevo."
                            )
                    except ValueError:
                        warningMessage(
                            " Debes ingresar un número entero válido. Intenta de nuevo."
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
                            warningMessage(
                                " Debes ingresar un número válido para el experimento, intenta de nuevo."
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

            except ValueError as e:
                errorMessage(
                    " Debes ingresar un número de resultados obtenidos del experimento."
                    + e
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
            ExperimentalData.comparativeResults()
            pass
        elif option == "5":
            print(
                "\n--------------------------------------------------------------------------"
            )
            print("📑 Generando reporte general...")
            print(
                "--------------------------------------------------------------------------\n"
            )
            ExperimentalData.generateReports()
            pass
        elif option == "6":
            print(
                "\n--------------------------------------------------------------------------"
            )
            print("📑 Exportando informe general...")
            print(
                "--------------------------------------------------------------------------\n"
            )
            resultados = ExperimentalData.compareExperiments()
            ExperimentalData.exportExperimentsToFile(resultados)

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
