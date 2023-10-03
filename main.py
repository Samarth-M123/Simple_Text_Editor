from cmdClass import *
import re
import os

mainObject = Cmd()
while True:
    try:
        userInput = str(input(f"${mainObject.getAccount()}: "))
        matches = re.search(r'^^(create|open|kill|exit) -(?:\s+([^\s]+))?$', userInput)
        if matches is None:
            raise ValueError
        else:
            command = matches.group(1)
            if matches.group(2) != None:
                parameter = matches.group(2)
    except FileNotFoundError:
        mainObject.programExit(f"Your parameter (file-name) was invalid")
    except ValueError:
        mainObject.programExit(f"Your input was invalid")
    except TypeError:
        mainObject.programExit(f"You passed unwanted arguments")
    
    if command == "create":
        try:
            mainObject.create(parameter)
        except NameError:
            mainObject.programExit("No argument was passed")
    elif command == "kill":
        try:
            mainObject.kill(parameter)
        except NameError:
            mainObject.programExit("No argument was passed")
    elif command == "open":
        try:
            mainObject.fileOpen(parameter)
        except NameError:
            mainObject.programExit("No argument was passed")
    elif command == "exit":
        mainObject.programExit()