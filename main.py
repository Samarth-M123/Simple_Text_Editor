import cmdClass
import re

mainObject = cmdClass()
while True:
    try:
        command = str(input(f"${mainObject.getAccount()}: "))
    except FileNotFoundError as e:
        print(f"{e}: Your parameter (file-name) was invalid")
        mainObject.exit()
    except ValueError as e:
        print(f"{e}: You gave input of wrong datatype")
    
    