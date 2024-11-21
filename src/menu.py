'''
    Menu main of program 
'''
from .modules import ExperimentalData

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
            typeExperiment = input("Enter the type of experiment: ")            
            
            try:
                print("\n-----------------------------------------------------------------------")           
                print("Note: you must enter a minimum of 3 results obtained of the experiment.")
                print("-----------------------------------------------------------------------")
                minResultsObtained = int(input("Enter the number of results obtained of the experiment: "))

                while True:
                    if minResultsObtained < 3:
                        print("⚠️ you must enter a minimum of 3 results obtained of the experiment.\n")
                        minResultsObtained = int(input("Enter the number of results obtained of the experiment: "))
                    else:
                        break
                
                for i in range(minResultsObtained):
                    result = float(input(f" 🔹 Enter the result {i+1} obtained of the '{nameExperiment}': "))
                    resultsObtained.append(result)

            except ValueError:
                print("You must enter a number for the results obtained of the experiment.")

            # Test of prompts
            print("\n✅ Added experiment successfully.")
            print("\n-------------------")
            print(f"Name of the experiment: {nameExperiment}")
            print(f"Date of completion of the experiment: {dateCompletion}")
            print(f"Type of experiment: {typeExperiment}")
            print(f"Results obtained of the experiment: {resultsObtained}")            
        elif option == "2":
            print("-----------------------------")
            print("\nVisualizar experimentos\n")
            print("-----------------------------")
            experiments_data = [
                {
                    "nameExperiment": "Experiment 1",
                    "dateCompletion": "12/12/2024",
                    "typeExperiment": "Math 1",
                    "resultsObtained": 1.5
                },
                {
                    "nameExperiment": "Experiment 2",
                    "dateCompletion": "12/12/2024",
                    "typeExperiment": "Math 2",
                    "resultsObtained": 2.5
                }
            ]
            # Test
            ExperimentalData.addExperiment(experiments_data)
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