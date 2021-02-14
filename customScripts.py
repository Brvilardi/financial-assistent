
import csv

def getVariableData(filePath, target):
    with open(filePath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for key, value in csv_reader:
            if key == target:
                return value
            pass
        return "Not Found"
