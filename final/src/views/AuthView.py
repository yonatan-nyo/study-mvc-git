# src/views/AuthView.py

def getUserInput():
    username = input("username : ")
    password = input("password : ")

    return (username, password)


def showResult(res: str):
    if (res == "SUCCESS"):
        print("success register")
        return
    else:
        print("failed", res)
