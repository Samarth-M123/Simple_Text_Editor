import os

class Cmd:
    def __init__(self):
        self.account = input("Account Name: ")
    def create(self, fileName):
        file = open(f"{self.account}_{fileName}", 'x')
    def programExit(self, exitMessage=None):
        exit(exitMessage)
    def kill(self, fileName):
        os.remove(fileName)
    def fileOpen(self, fileName):
        with open(fileName, 'a+') as file:
            lineNum = 0
            for i in file.readlines():
                lineNum += 1
                print(f"{lineNum} {i}")
            while True:
                lineNum += 1
                line = input(f"{lineNum} ")
                if line != "q\?":
                    file.write(f"{line}\n")
                else:
                    break
    def getAccount(self):
        return self.account