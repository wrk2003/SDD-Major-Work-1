from random import randint
from subprocess import run
from os import sys, chdir, path

def GenerateFileName (existingFileNames):
    randomInt = GenerateRandomInteger()
    fileName = ConvertToHexadecimalString(randomInt)

    while IsFileNameUsed(fileName, existingFileNames):
        randomInt = GenerateRandomInteger()
        fileName = ConvertToHexadecimalString(randomInt)

    return fileName

def GenerateRandomInteger ():
    return randint(int(16**7), int(16**8)-1) 

def ConvertToHexadecimalString (integer):
    return str(int(integer, 16))

def IsFileNameUsed (fileName, existingFileNames):
    for file in existingFileNames:
        if file == fileName:
            return True
    return False

def CreatePythonFile (fileName, inputText):
    path = sys.path[0]
    chdir(path)
    f = open(path + "/problems/python_files/" + fileName + ".py", "w")
    f.write(inputText)
    f.close()

def ExecutePythonFile (fileName, inputData):
    path = sys.path[0]
    chdir(path)

    programOutput = []

    for data in inputData:
        programOutput.append(run(f"py python_files/{fileName}.py {str(data)}", capture_output=True).stdout.strip().decode("UTF-8"))

    return programOutput

print(ExecutePythonFile("helloName", ["1 2", "2 3"]))