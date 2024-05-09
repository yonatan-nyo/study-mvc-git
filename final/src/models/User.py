# src/models/User.py

from src.helpers import FileManager
from typing import List, Optional

FILENAME = "user.txt"
HEADER = "id;username;password"
data = []


def parseDataString(DataString: str) -> List[dict]:
    users = []
    lines = DataString.split("\n")
    lines = lines[1:]  # Skip the header line
    for line in lines:
        el = line.split(";")
        user = {'id': int(el[0]), 'username': el[1],
                'password': el[2]}
        users.append(user)
    return users


def getDataFromFile() -> List[dict]:
    CSVString = FileManager.readFile(FILENAME)
    return parseDataString(CSVString)


def load() -> None:
    global data
    data = getDataFromFile()


def toString(user: dict) -> str:
    return f"\n{user['id']};{user['username']};{user['password']}"


def toStringAll(users: List[dict]) -> str:
    DataString = ""
    for user in users:
        DataString += toString(user)
    return DataString


def save() -> None:
    global data
    FileManager.rewriteFile(FILENAME, HEADER)
    FileManager.appendFile(FILENAME, toStringAll(data))


def getNextId() -> int:
    global data
    if not data:
        return 1
    return int(data[-1]['id']) + 1


def findOneByUsername(username: str) -> Optional[dict]:
    global data
    for existingUser in data:
        if existingUser['username'] == username:
            return existingUser
    return None


def insertOne(username: str, password: str) -> str:
    global data
    if findOneByUsername(username):
        return "USER EXISTS"
    inputUser = {'id': getNextId(), 'username': username,
                 'password': password}
    data.append(inputUser)
    return "SUCCESS"


def updateOneById(id: int, newUsername: str) -> str:
    global data
    for existingUser in data:
        if existingUser['id'] == id:
            existingUser["username"] = newUsername
            return "SUCCESS"
    return "USER DOESN'T EXISTS"


def deleteOneById(id: int) -> str:
    global data
    newData = []
    for existingUser in data:
        if existingUser['id'] != id:
            newData.append(existingUser)
    data = newData
    return "SUCCESS"
