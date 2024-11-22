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
from collections.abc import Collection  # For validate results saved on collection


class ExperimentalData:
    listExperimentalData = []

    def __init__(
        self,
        experimentName,
        completionDate,
        experimentCategory,
        resultsObtained: Collection,
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

        ExperimentalData.listExperimentalData.append(self)

    @classmethod
    def addExperiment(cls, experiments):
        for experiment in experiments:
            cls(
                experimentName=experiment["experimentName"],
                completionDate=experiment["completionDate"],
                experimentCategory=experiment["experimentCategory"],
                resultsObtained=experiment["resultsObtained"],
            )

    def __str__(self):
        return (
            f"Experimento: {self.experimentName}, "
            f"Completion Date: {self.completionDate}, "
            f"Experiment Type: {self.experimentCategory}, "
            f"Results obtained: {self.resultsObtained}\n "
        )

    def showExperiment(self):
        for experiment in ExperimentalData.listExperimentalData:
            print(experiment)

    def getAnalysisResultsObtained():
        pass

    def printAllExperiments():
        if not ExperimentalData.listExperimentalData:
            print("⚠️  No hay experimentos registrados.")
        for i, experiment in enumerate(ExperimentalData.listExperimentalData, start=1):
            print(f"Experimento {i}:")
            print(f"Nombre del experimento: {experiment.experimentName}")
            print(f"Fecha de realización: {experiment.completionDate}")
            print(f"Tipo de experimento: {experiment.experimentCategory}")
            print(f"Resultados obtenidos: {experiment.resultsObtained}")
            for j, result in enumerate(experiment.resultsObtained, start=1):
                print(f"        Resultado {j} : {result}")
