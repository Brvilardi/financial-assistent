
import csv
import os

def getVariableData(filePath, target):
    try: 
        return os.environ[target]
    except:
        with open(filePath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for key, value in csv_reader:
                if key == target:
                    return value
                pass
        return "Not Found"
