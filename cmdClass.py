import os

class Cmd:
    def __init__(self):
        self.account = input("Account Name: ")
    def create(self, fileName):
        file = open(f"{self.account}_{fileName}", 'x')
    def programExit(self, exitMessage):
        exit(exitMessage)
    def kill(self, fileName):
        os.remove(fileName)
    def fileOpen(self, fileName):
        pass
    def getAccount(self):
        return self.account