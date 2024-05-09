# src/controllers/AuthController.py

from src.models import User
from src.views import AuthView


def Register():
    username, password = AuthView.getInputRegister()

    res = User.insertOne(username, password)

    AuthView.showResultRegister(res)
