'''
    Menu main of program 
'''
from .modules import ExperimentalData
from .utils import validations

def run():

    while True:
        print("\nWhat do you want to do?")
        print("\n1. ✏️ Agregar un experimento")
        print("\n2. 🔍 Visualizar los experimentos")
        print("\n3. 🧮 Realizar cálculos")
        print("\n4. 📊 Comparar experimentos")
        print("\n5. 📑 Generar informe final")
        print("\n6. 💾 Exportar informe a archivo de texto")
        print("\n7. 🔚 Salir")

        option = input("\nSeleccione una opción: ")

        if option == "1":
            resultsObtained = []

            print("\n-------------------")
            print("✏️ Add a experiment")
            print("-------------------\n")                       
            nameExperiment = input("Enter the name of the experiment: ")
            dateCompletion = input("Enter the date of completion of the experiment (dd/mm/yyyy): ")

            while not validations.isValidDate(dateCompletion):
                print("⚠️ You must enter a date in the format 'dd/mm/yyyy'. Example: '12/12/2024', '30/11/2023', etc.")
                dateCompletion = input("Enter the date of completion of the experiment (dd/mm/yyyy): ")

            typeExperiment = input("\nEnter the type of experiment:")
            
            try:
                print("\n--------------------------------------------------------------------------")
                print("⚠️ Note: you must enter a minimum of 3 results obtained of the experiment.")
                print("--------------------------------------------------------------------------\n")
                minResultsObtained = int(input("Enter the number of results obtained of the experiment: "))

                for i in range(minResultsObtained):
                    while True:
                        try:
                            result = float(input(f" 🔹 Enter the result {i+1} obtained of the '{nameExperiment}': "))
                            resultsObtained.append(result)
                            break
                        except ValueError:
                            print("⛔ You must enter a valid number for the result.")

            except ValueError:
                print("You must enter a number for the results obtained of the experiment.")

            experimentsData = [
                {
                    "nameExperiment": nameExperiment,
                    "dateCompletion": dateCompletion,
                    "typeExperiment": typeExperiment,
                    "resultsObtained": resultsObtained
                }
            ]
            print(experimentsData)
            ExperimentalData.addExperiment(experimentsData)

            # Test of prompts
            # print("\n✅ Added experiment successfully.")
            # print("\n-------------------")
            # print(f"Name of the experiment: {nameExperiment}")
            # print(f"Date of completion of the experiment: {dateCompletion}")
            # print(f"Type of experiment: {typeExperiment}")
            # print(f"Results obtained of the experiment: {resultsObtained}")            
        elif option == "2": 
            ExperimentalData.printAllExperiments()            
        elif option == "3":
            #Functions.CalculosEstadisticos()
            pass
        elif option == "4":
            #Functions.CalculosEstadisticos()
            pass
        elif option == "5":
            #Functions.GenerarInformes()
            pass
        elif option == "6":
            #Functions.ExportarReporte()
            pass
        elif option == "7":
            print("Has salido del programa.")
            break
        else:
            print("Opción inválida")