# src/controllers/MainController.py

from src.models import User


def Load():
    User.load()


def Save():
    User.save()
