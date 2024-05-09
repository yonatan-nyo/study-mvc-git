# src/models/User.py

from src.helpers import FileManager
from typing import List, Optional

FILENAME = "user.csv"
HEADER = "id;username;password"
data = []


def parseCSVString(CSVStringLine: str) -> dict:
    CSVStringData = CSVStringLine.split(";")
    return {
        "id": int(CSVStringData[0]),
        "username": CSVStringData[1],
        "password": CSVStringData[2]
    }


def parseCSVStringAll(CSVString: List[str]) -> List[dict]:
    userData = []
    for line in CSVString:
        userData.append(parseCSVString(line))
    return userData


def load():
    CSVString = FileManager.readFile(FILENAME).split("\n")[1:]
    global data
    data = parseCSVStringAll(CSVString)


def getCSVString(user: dict) -> str:
    return f'\n{user["id"]};{user["username"]};{user["password"]}'


def getCSVStringAll():
    global data
    CSVStringAll = ""
    for user in data:
        CSVStringAll += getCSVString(user)
    return CSVStringAll


def save():
    FileManager.rewriteFile(FILENAME, HEADER)
    FileManager.appendFile(FILENAME, getCSVStringAll())


def findAll():
    global data
    return data


def getNextId():
    global data
    if (len(data) <= 0):
        return 1
    return data[-1]["id"] + 1


def findOneByUsername(username: str) -> Optional[dict]:
    global data
    for user in data:
        if (user["username"] == username):
            return user
    return None


def insertOne(username: str, password: str) -> str:
    id = getNextId()
    global data
    if (findOneByUsername(username)):
        return "USER EXISTS"
    data.append({"id": id, "username": username, "password": password})
    return "SUCCESS"
