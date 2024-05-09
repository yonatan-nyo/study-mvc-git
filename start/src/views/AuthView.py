
def getInputRegister():
    username = input("username : ")
    password = input("password : ")

    return (username, password)


def showResultRegister(res: str):
    if (res == "SUCCESS"):
        print("success register")
        return
    else:
        print("failed", res)
