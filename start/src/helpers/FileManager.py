# src/helpers/FileManager.py
import os


def createFile(fileName: str):
    filePath: str = "data/" + fileName
    os.makedirs(os.path.dirname(filePath), exist_ok=True)
    with open(filePath, "x"):
        pass


def rewriteFile(fileName: str, strData: str):
    filePath: str = "data/" + fileName
    os.makedirs(os.path.dirname(filePath), exist_ok=True)
    if not os.path.exists(filePath):
        createFile(fileName)
    with open(filePath, "w") as f:
        f.write(strData)


def appendFile(fileName: str, strData: str):
    filePath: str = "data/" + fileName
    os.makedirs(os.path.dirname(filePath), exist_ok=True)
    if not os.path.exists(filePath):
        createFile(fileName)
    with open(filePath, "a") as f:
        f.write(strData)


def readFile(fileName: str) -> str:
    filePath: str = "data/" + fileName
    os.makedirs(os.path.dirname(filePath), exist_ok=True)
    if not os.path.exists(filePath):
        createFile(fileName)
    with open(filePath) as f:
        return f.read()
