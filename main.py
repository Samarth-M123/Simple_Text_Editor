import cmdClass
import re

mainObject = cmdClass()
while True:
    try:
        userInput = str(input(f"${mainObject.getAccount()}: "))
        matches = re.search(r'^^(create|open|kill|exit)(?:\s+([^\s]+))?$', userInput)
        if matches != True:
            raise ValueError
        else:
            command = matches.group(1)
            if matches.group(2) != None:
                parameter = matches.group(2)
    except FileNotFoundError as e:
        mainObject.exit(f"{e}: Your parameter (file-name) was invalid")
    except ValueError as e:
        mainObject.exit(f"{e}: Your input was invalid")
    except TypeError as e:
        mainObject.exit(f"{e}: You passed unwanted arguments")
    
    if command == "create":
        mainObject.create(parameter)
    elif command == "kill"
        mainObject.kill(parameter)
    elif command == "open"
        mainObject.fileOpen(parameter)
    elif command == "exit":
        mainObject.programExit()
    
    
    