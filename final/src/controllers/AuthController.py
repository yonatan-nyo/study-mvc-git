# src/controllers/AuthController.py

from src.models import User
from src.views import AuthView


def Register():
    username, password = AuthView.getUserInput()

    res = User.insertOne(username, password)

    AuthView.showResult(res)
