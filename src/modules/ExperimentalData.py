from datetime import datetime
from collections.abc import Collection
import os
from pathlib import Path
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
        experimentId=0,
    ):
        if not isinstance(experimentName, str):
            raise ValueError(
                "Debes ingresar un nombre para el experimento. Ejemplo: 'Experimento 1', 'Experimento 2', etc."
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
            print(
                "⛔ No se puede utilizar este recurso porque no hay experimentos registrados. \nRegistra resultados de experimentos primero..."
            )
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

        for exp in cls.listExperimentalData:
            cls.table.add_row(
                [
                    exp.experimentId,
                    exp.experimentName,
                    exp.completionDate,
                    exp.experimentCategory,
                    ", ".join(map(str, exp.resultsObtained)),
                ]
            )

    @classmethod
    def getTable(cls):
        return cls.table

    @classmethod
    def getTableStr(cls):
        cls.tableStr = cls.table.get_string()
        return cls.tableStr

    @classmethod
    def exportExperimentsToFile(cls):
        fileName = "informe-experimental.txt"
        folder = "informes-exportados"
        directory = Path.cwd() / folder

        if not cls.isExperimentRegistered():
            return

        if not os.path.exists(folder):
            os.makedirs(directory)
            print(f"\nSe ha creado la carpeta 📁 '{folder}'.\n")

        try:
            with open(directory / fileName, "w") as f:
                f.write(cls.getTableStr())
                print(
                    f"✅ Informe exportado exitosamente en '{directory / fileName}'.\n"
                )
        except Exception as e:
            print(f"⛔ Error al exportar el informe experimental: {e}")

    @classmethod
    def calculatedResults(cls):
        if not cls.isExperimentRegistered():
            return

        for exp in cls.listExperimentalData:
            print(f"  🔹 Id: {exp.experimentId}, - {exp.experimentName}")

        isFound = False  # Verifica si el ID existe en la lista
        while not isFound:
            experimentInput = int(input("\nPor favor, ingrese el ID del experimento: "))

            for exp in cls.listExperimentalData:
                if exp.experimentId == experimentInput:
                    print(
                        f"\nEl experimento {exp.experimentName} tiene los siguientes resultados: \n"
                        f"Promedio: {cls.calculateAverageResults(experimentInput):2f} \n"
                        f"Mínimo: {cls.calculateMin(experimentInput)} \n"
                        f"Máximo: {cls.calculateMax(experimentInput)}"
                    )
                    isFound = True
                    return
                print(
                    f"\n ⚠️  No se encontró un experimento con el Id {experimentInput}, ingresado."
                )

    @classmethod
    def calculateAverageResults(cls, id):
        for exp in cls.listExperimentalData:
            if exp.experimentId == id:
                return sum(exp.resultsObtained) / len(exp.resultsObtained)

    @classmethod
    def calculateMin(cls, id):
        for exp in cls.listExperimentalData:
            if exp.experimentId == id:
                return min(exp.resultsObtained)

    @classmethod
    def calculateMax(cls, id):
        for exp in cls.listExperimentalData:
            if exp.experimentId == id:
                return max(exp.resultsObtained)

    @classmethod
    def compareExperiments(cls):
        if not cls.isExperimentRegistered():
            return
        avaliableExperiments = len(cls.listExperimentalData)

        if avaliableExperiments < 2:
            print(
                "⚠️  No hay suficientes experimentos para comparar, como mínimo debes tener dos."
            )
            return

        print("Estos son los experimentos disponibles:")

        for exp in cls.listExperimentalData:
            print(f"  🔹 Id: {exp.experimentId}, - {exp.experimentName}")

        while True:
            quantityExperiments = int(input("\n¿Cuántos experimentos desea comparar? "))

            if quantityExperiments > avaliableExperiments:
                print(
                    f"\n ⚠️ Sólo hay {avaliableExperiments} experimentos disponibles para comparar."
                )
                continue
            elif quantityExperiments < 2:
                print(
                    "\n ⚠️  No son suficientes experimentos, para comparar como mínimo debes ingresar dos."
                )
                continue

            experimentResults = (
                {}
            )  # Diccionario para almacenar los resultados de cada experimento

            for i in range(quantityExperiments):
                experimentInput = int(
                    input(f"\nPor favor, ingrese el ID del experimento {i + 1}: ")
                )
                isFound = False
                for exp in cls.listExperimentalData:
                    if exp.experimentId == experimentInput:
                        avg = cls.calculateAverageResults(experimentInput)
                        minVal = cls.calculateMin(experimentInput)
                        maxVal = cls.calculateMax(experimentInput)

                        experimentResults[experimentInput] = {
                            "name": exp.experimentName,
                            "average": avg,
                            "min": minVal,
                            "max": maxVal,
                        }

                        print(
                            f"\nEl experimento {exp.experimentName} tiene los siguientes resultados: \n"
                            f"Promedio: {avg:.2f} \n"
                            f"Mínimo: {minVal} \n"
                            f"Máximo: {maxVal}"
                        )
                        isFound = True
                        break

                if not isFound:
                    print(
                        f"\n ⚠️ No se encontró un experimento con el ID {experimentInput}. Por favor, inténtelo de nuevo."
                    )
                    i -= 1

            # Conclusiones de la comparación
            if experimentResults:
                tableResults = PrettyTable()
                tableResults.field_names = [
                    "Experimento",
                    "Promedio",
                    "Mínimo",
                    "Máximo",
                ]

                for exp in experimentResults.values():
                    tableResults.add_row(
                        [exp["name"], exp["average"], exp["min"], exp["max"]]
                    )

                print("\nConclusiones de la comparación:\n")
                print(tableResults)
                """ 
                bestAverage = max(
                    experimentResults.items(), key=lambda x: x[1]["average"]
                )
                print(
                    f"\nEl experimento con el mejor promedio es {bestAverage[1]['name']} "
                    f"con un promedio de {bestAverage[1]['average']:.2f}."
                )

                minResult = min(experimentResults.items(), key=lambda x: x[1]["min"])
                print(
                    f"\nEl experimento con el menor resultado es {minResult[1]['name']} con {minResult[1]['min']} "
                )

                maxResult = max(experimentResults.items(), key=lambda x: x[1]["max"])
                print(
                    f"\nEl experimento con el mayor resultado es {maxResult[1]['name']} con {maxResult[1]['max']} "
                ) """
                break
