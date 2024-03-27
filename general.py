import requests

class Subject():
    def __init__(self, name, quiz, mats, chaps, tips):
        self.name = name
        self.quiz = quiz
        self.mats = mats
        self.chaps = chaps
        self.tips = tips

    def __str__(self):
        return f"The subject {self.name}"

