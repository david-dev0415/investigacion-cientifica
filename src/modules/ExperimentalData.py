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
        experimentType,
        resultsObtained: Collection,
    ):

        if not isinstance(experimentName, str):
            raise ValueError(
                "You must enter a string for the name of the task. Example: 'Name Experiment 1', 'Name Experiment 2', etc."
            )

        try:
            self.dateCompletion = datetime.strptime(completionDate, "%d/%m/%Y")
        except ValueError:
            raise ValueError(
                "You must enter a date in the format 'dd/mm/yyyy'. Example: '12/12/2024', '30/11/2023', etc."
            )

        if not isinstance(experimentType, str):
            raise ValueError(
                "You must enter a string for the category of the task. Example: 'Work', 'Personal', 'Study', etc."
            )

        if not all(isinstance(result, (int, float)) for result in resultsObtained):
            raise ValueError(
                "You must enter a list of floats or integers for the results obtained of the experiment. Example: [1.5, 2.0, 3.0], etc."
            )

        self.experimentName = experimentName
        self.completionDate = completionDate
        self.experimentType = experimentType
        self.resultsObtained = list(resultsObtained)

        ExperimentalData.listExperimentalData.append(self)

    @classmethod
    def addExperiment(cls, experiments):
        for experiment in experiments:
            cls(
                experimentName=experiment["experimentName"],
                completionDate=experiment["completionDate"],
                experimentType=experiment["experimentType"],
                resultsObtained=experiment["resultsObtained"],
            )

    def __str__(self):
        return (
            f"Experiment: {self.experimentName}, "
            f"Completion Date: {self.completionDate}, "
            f"Experiment Type: {self.experimentType}, "
            f"Results obtained: {self.resultsObtained}\n "
        )

    def showExperiment(self):
        for experiment in ExperimentalData.listExperimentalData:
            print(experiment)

    def getAnalysisResultsObtained():
        pass

    def printAllExperiments():
        for experiment in ExperimentalData.listExperimentalData:
            print(
                {
                    "experimentName": experiment.experimentName,
                    "completionDate": experiment.completionDate,
                    "experimentType": experiment.experimentType,
                    "resultsObtained": experiment.resultsObtained,
                }
            )
