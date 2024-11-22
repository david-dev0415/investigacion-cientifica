''' 
Task | task module (tareas)

Provides a simple interface for create Data experimental.
.- The ExperimentalData class is used to create tasks with the following attributes:
    .- nameExperiment: Name experiment.
    .- dateCompletion: Date completion of the experiment.
    .- typeExperiment: Type of experiment.
    .- resultsObtained: Results obtained of the experiment.
'''
from datetime import datetime
from collections.abc import Collection

class ExperimentalData():
    listExperimentalData = []
    def __init__(self, nameExperiment, dateCompletion, typeExperiment, resultsObtained: Collection):
        
        if not isinstance(nameExperiment, str):
            raise ValueError(
                "You must enter a string for the name of the task. Example: 'Name Experiment 1', 'Name Experiment 2', etc."
            )
        
        try:
            self.dateCompletion = datetime.strptime(dateCompletion, "%d/%m/%Y")
        except ValueError:
            raise ValueError(
                "You must enter a date in the format 'dd/mm/yyyy'. Example: '12/12/2024', '30/11/2023', etc."
            )
        
        if not isinstance(typeExperiment, str):
            raise ValueError(
                "You must enter a string for the category of the task. Example: 'Work', 'Personal', 'Study', etc."
            ) 
        
        if not all(isinstance(resultsObtained, int) for resultsObtained in resultsObtained):
            raise ValueError(
                "You must enter an float or integer for the results obtained of the experiment. Example: 1.5, 2.0, 3.0, etc."
            )

        self.nameExperiment = nameExperiment
        self.dateCompletion = dateCompletion
        self.typeExperiment = typeExperiment
        self.resultsObtained = list(resultsObtained)

        ExperimentalData.listExperimentalData.append(self)

    @classmethod
    def addExperiment(cls, experiments):
        for experiment in experiments:
            cls(
                nameExperiment=experiment["nameExperiment"],
                dateCompletion=experiment["dateCompletion"],
                typeExperiment=experiment["typeExperiment"],
                resultsObtained=experiment["resultsObtained"]
            )

    def __str__(self):        
        return (            
            f"Experiment: {self.nameExperiment}, " 
            f"Date completion: {self.dateCompletion}, " 
            f"Type experiment: {self.typeExperiment}, " 
            f"Results obtained: {self.resultsObtained}\n "
        )
    
    def showExperiment(self):
        for experiment in ExperimentalData.listExperimentalData:
            print(experiment)
    
    def getAnalysisResultsObtained():
        pass
    
    def printAllExperiments():
        for experiment in ExperimentalData.listExperimentalData:
            print({
                "nameExperiment": experiment.nameExperiment,
                "dateCompletion": experiment.dateCompletion,
                "typeExperiment": experiment.typeExperiment,
                "resultsObtained": experiment.resultsObtained
            })
