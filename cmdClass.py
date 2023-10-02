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
        with open(fileName, 'a+') as file:
            for i in file.readlines():
                print i
            lineNum = 0
            while True:
                lineNum += 1
                line = input(f"{lineNum} ")
                if line != "q\?":
                    file.write(line)
                else:
                    break
    def getAccount(self):
        return self.account