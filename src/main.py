import os
from pathlib import Path
import JsonDBlib as l
clear = lambda: os.system('cls')

def main():
    while True:
        clear()
        choise = input("Choose one of the options:\n\n(1) Create DB\n(2) Use DB\n(3) Connect to a DB\n(0) Exit\n\n> ")
        if choise == "1":
            clear()
            l.create_db()
        elif choise == "2":
            clear()
            choise = input("Choose a DB name:\n\n> ")
            message = l.use_db(choise)
            if not message[0]:
                print(message[1])
        elif choise=="0":
            break
        


if __name__ == '__main__':
    main()