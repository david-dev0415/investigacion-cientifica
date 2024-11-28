from datetime import datetime
from collections.abc import Collection
import os
from pathlib import Path
from prettytable import PrettyTable
from colorama import Fore, Back, Style


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
    def deleteExperiment(cls):
        if not cls.isExperimentRegistered():
            return
        print("Estos son los experimentos registrados:")

        table = PrettyTable()
        table.field_names = ["Id", "Nombre"]

        for exp in cls.listExperimentalData:
            table.add_row([exp.experimentId, exp.experimentName])

        print(table)

        while True:
            experimentId = int(input("\nPor favor, ingrese el ID del experimento: "))
            for exp in cls.listExperimentalData:
                if exp.experimentId == experimentId:
                    cls.listExperimentalData.remove(exp)
                    print(f"\nEl experimento {exp.experimentName} ha sido eliminado.")
                    return
                print(f"⛔ No se encontró un experimento con el Id {experimentId}.")

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

        table = PrettyTable()
        table.field_names = ["Id", "Nombre"]

        for exp in cls.listExperimentalData:
            table.add_row([exp.experimentId, exp.experimentName])

        print(table)

        isFound = False  # Verifica si el ID existe en la lista
        while not isFound:
            experimentInput = int(input("\nPor favor, ingrese el ID del experimento: "))

            for exp in cls.listExperimentalData:
                if exp.experimentId == experimentInput:
                    print(
                        f"\nEl experimento {exp.experimentName} tiene los siguientes resultados: \n"
                        f"Promedio: {cls.calculateAverageResults(experimentInput):.2f} \n"
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
                avg = sum(exp.resultsObtained) / len(exp.resultsObtained)
                return float(avg)

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
        avaliableExperiments = cls.availableExperiments()

        if avaliableExperiments < 2:
            print(
                "⚠️  No hay suficientes experimentos para comparar, como mínimo debes tener dos."
            )
            return

        print("Estos son los experimentos disponibles:\n")

        table = PrettyTable()
        table.field_names = ["Id", "Nombre"]

        for exp in cls.listExperimentalData:
            table.add_row([exp.experimentId, exp.experimentName])

        print(table)

        while True:
            quantityExperiments = int(
                input("\n¿Cuántos experimentos desea comparar?: ")
            )
            print(f"------------------------------------------")
            print(
                f"👉 Te confirmo que vas a comparar {quantityExperiments} experimentos"
            )
            print(f"------------------------------------------\n")

            if quantityExperiments > avaliableExperiments:
                print(
                    f"\n⚠️ Sólo hay {avaliableExperiments} experimentos disponibles para comparar."
                )
                continue
            elif quantityExperiments < 2:
                print(
                    "\n ⚠️ No son suficientes experimentos, para comparar como mínimo debes ingresar dos."
                )
                continue

            experimentIds = []
            i = 1
            while i <= quantityExperiments:
                experimentInput = int(input(f"🔘 Ingrese el ID del experimento {i}: "))
                # Si es ingresado el mismo ID, se repite el bucle.
                if experimentInput in experimentIds:
                    print(
                        f"\n ⚠️ El ID {experimentInput} ya ha sido ingresado. Por favor, ingrese uno diferente."
                    )
                    continue
                # Si el ID no existe en la lista, se repite el bucle.
                if not any(
                    exp.experimentId == experimentInput
                    for exp in cls.listExperimentalData
                ):
                    print(
                        f"\n⚠️ No se encontró un experimento con el ID {experimentInput}. Por favor, ingrese correctamente el ID.\n"
                    )
                    continue

                experimentIds.append(experimentInput)
                i += 1

            # Esto nos llama a la función comparativeResults con los Ids recogidos.
            cls.comparativeResults(experimentIds)
            break

    @classmethod
    def comparativeResults(cls, experimentIds=None):
        isFound = False
        experimentResults = {}  # Diccionario para almacenar los resultados

        if experimentIds is None:
            experimentIds = [exp.experimentId for exp in cls.listExperimentalData]

        for experimentInput in experimentIds:
            for exp in cls.listExperimentalData:
                if exp.experimentId == experimentInput:
                    avg = float(cls.calculateAverageResults(experimentInput))
                    minVal = cls.calculateMin(experimentInput)
                    maxVal = cls.calculateMax(experimentInput)

                    experimentResults[exp.experimentId] = {
                        "experimentId": exp.experimentId,
                        "name": exp.experimentName,
                        "average": avg,
                        "min": minVal,
                        "max": maxVal,
                    }
                    print(
                        f"\nEl experimento {exp.experimentName} tiene los siguientes resultados:\n"
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

        if experimentResults:
            tableResults = PrettyTable()
            tableResults.field_names = [
                "Id",
                "Experimento",
                "Promedio",
                "Mínimo",
                "Máximo",
            ]

            # sorted_experimentResults = sorted(
            #     experimentResults.values(), key=lambda exp: exp["experimentId"]
            # )

            for exp in experimentResults.values():
                tableResults.add_row(
                    [
                        exp["experimentId"],
                        exp["name"],
                        f"{exp["average"]:.2f}",
                        exp["min"],
                        exp["max"],
                    ]
                )

            print("\n------------------------------------------")
            print("Detalles de la comparación:")
            print("------------------------------------------")
            print(tableResults)

            print("\n------------------------------------------")
            print("Conclusiones de la comparación:")
            print("------------------------------------------")
            bestAverage = max(experimentResults.items(), key=lambda x: x[1]["average"])
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
            )

    @classmethod
    def availableExperiments(cls):
        return len(cls.listExperimentalData)
