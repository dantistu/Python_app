from abc import abstractmethod
import os
import time
from colorama import Fore

MAIN_DESCRIPTION = "Press W, E keys to change menu options. Enter to select an option and Esc to close the programm."
ENDL = "\n"
SPACE = " "

class MainMenu: 
    @abstractmethod
    def map():
        while True:
            os.system("cls||clear")
            print(ENDL + SPACE + Fore.LIGHTRED_EX + MAIN_DESCRIPTION + "\n\n")
            print(SPACE + Fore.YELLOW + 'Element 1')
            print(SPACE + Fore.YELLOW + 'Element 2')
            print(SPACE + Fore.LIGHTYELLOW_EX + '\033[4m' + '_Element 3' + '\033[0m')
            print(SPACE + Fore.YELLOW + 'Element 4')
            print(SPACE + Fore.YELLOW + 'Element 5')
            element_desc = "That's doing something for anything..."
            print(ENDL + ENDL + SPACE + Fore.YELLOW + 'Option\'s description: ' + element_desc)
            time.sleep(1)
            
    
