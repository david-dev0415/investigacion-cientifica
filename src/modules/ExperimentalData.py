""" 
Task | task module (tareas)

Provides a simple interface for create Experimental Data.
.- The ExperimentalData class is used to create tasks with the following attributes:
    .- nameExperiment: Name experiment.
    .- dateCompletion: Date completion of the experiment.
    .- typeExperiment: Type of experiment.
    .- resultsObtained: Results obtained of the experiment.
"""

from datetime import datetime
from collections.abc import Collection
import os
from pathlib import Path  # For validate results saved on collection
from prettytable import PrettyTable
class ExperimentalData:
    listExperimentalData = []    
    tableStr = ""

    def __init__(
        self,
        experimentName,
        completionDate,
        experimentCategory,
        resultsObtained: Collection,
        experimentId,
    ):

        if not isinstance(experimentName, str):
            raise ValueError(
                "Debes ingresar un nombre para el experimento. Example: 'Experimento 1', 'Experimento 2', etc."
            )

        try:
            self.dateCompletion = datetime.strptime(completionDate, "%d/%m/%Y")
        except ValueError:
            raise ValueError(
                "Debes ingresar una fecha en el formato 'dd/mm/yyyy'. Ejemplo: '12/12/2024', '30/11/2023', etc."
            )

        if not isinstance(experimentCategory, str):
            raise ValueError(
                "Selecciona una de las categorías del experimento: 'Química', 'Biología', 'Física'"
            )

        if not all(isinstance(result, (int, float)) for result in resultsObtained):
            raise ValueError(
                "Puedes ingresar enteros o decimales para los resultados obtenidos del experimento. Ejemplo: [1.5, 2, 3], etc."
            )

        self.experimentName = experimentName
        self.completionDate = completionDate
        self.experimentCategory = experimentCategory
        self.resultsObtained = list(resultsObtained)
        self.experimentId = experimentId

        ExperimentalData.listExperimentalData.append(self)

    @classmethod
    def addExperiment(cls, experiments):
        for experiment in experiments:
            cls(
                experimentName=experiment["experimentName"],
                completionDate=experiment["completionDate"],
                experimentCategory=experiment["experimentCategory"],
                resultsObtained=experiment["resultsObtained"],
                experimentId=experiment["experimentId"],
            )
        ExperimentalData.setTable()

    @classmethod
    def isExperimentRegistered(cls):        
        if not cls.listExperimentalData:
            print("⛔ No se puede exportar información porque no hay experimentos registrados. \nAgrega experimentos primero...")
            return False
        return True

    @classmethod
    def printAllExperiments(cls):
        if not cls.isExperimentRegistered():
            return                
        print(cls.getTableStr())

    @classmethod
    def setTable(cls):
        cls.table = PrettyTable()
        cls.table.field_names = ["Id", "Nombre", "Fecha", "Categoría", "Resultados"]
        
        for exp in ExperimentalData.listExperimentalData:
            cls.table.add_row([
                exp.experimentId, 
                exp.experimentName, 
                exp.completionDate, 
                exp.experimentCategory,
                ", ".join(map(str, exp.resultsObtained))
            ])
        
    @classmethod
    def getTable(cls):        
        return cls.table

    @classmethod
    def getTableStr(cls):
        cls.tableStr = cls.table.get_string()
        return cls.tableStr
    # Falta ingresar datos como: Fecha y hora de exportación, nombre de archivo y nombre de equipo.
    @classmethod
    def exportExperimentsToFile(cls):
        fileName = "informe-experimental.txt"
        folder = "informes-exportados"
        directory = Path.cwd() / folder

        if not cls.isExperimentRegistered():
            return

        if not os.path.exists("informes-exportados"):
            os.makedirs(directory)
            print(f"\nSe ha creado el 📁 '{folder}'.\n")

        try:
            with open(directory / fileName, "w") as f:
                f.write(cls.getTableStr())
                print(f"✅ Informe exportado exitosamente en '{directory / fileName}'.\n")
        except Exception as e:
            print(f"⛔ Error al exportar el informe experimental: {e}")

    @classmethod
    def calculatedResults(cls):

        cls.listExperimentalData = [
            {
                "experimentName": "Experimento 1",
                "experimentId": 1,
                "completionDate": "12/01/2024",
                "experimentCategory": "Química",
                "resultsObtained": [1, 2, 3]
            },
            {
                "experimentName": "Experimento 2",
                "experimentId": 2,
                "completionDate": "12/12/2024",
                "experimentCategory": "Física",
                "resultsObtained": [4, 5, 6]
            }
        ]

        if not cls.isExperimentRegistered():
            return
        
        for exp in cls.listExperimentalData:
            print(f"  🔹 Id: {exp["experimentId"]}, {exp["experimentName"]}")

        experimentInput = int(input("\nIngresa el Id del experimento para calcular los resultados: "))

        for exp in cls.listExperimentalData:
            if exp["experimentId"] == experimentInput:
                print(f"El experimento {exp["experimentName"]} tiene los siguientes resultados: {cls.calculateAverageResults(cls, experimentInput)}")
                return
            else:
                print(f" ⚠️ No se encontró un experimento con el Id {experimentInput}, ingresado.")
                return

    def calculateAverageResults(self, id):
        for exp in self.listExperimentalData:
            if exp["experimentId"] == id:
                return sum(exp["resultsObtained"]) / len(exp["resultsObtained"])
        
