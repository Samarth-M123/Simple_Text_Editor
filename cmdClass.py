import os

class Cmd:
    def __init__(self):
        self.account = input("Account Name: ")
    def create(self, fileName):
        file = open(f"{self.account}_{fileName}", 'x')
    def exitProgram(self):
        exit()
    def kill(self, fileName):
        os.remove(fileName)
    def open(self, fileName):
        pass