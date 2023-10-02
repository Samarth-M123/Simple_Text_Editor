import cmdClass
import re

mainObject = cmdClass()
while True:
    try:
        command = str(input(f"${mainObject.getAccount()}: "))
        if re.search('', command) != True:
            raise ValueError
    except FileNotFoundError as e:
        mainObject.exit(f"{e}: Your parameter (file-name) was invalid")
    except ValueError as e:
        mainObject.exit(f"{e}: Your input was invalid")
    
    
    