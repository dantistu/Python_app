from abc import abstractmethod
import os
import time
from colorama import Fore

DESCRIPTION = "Press W, E keys to change menu options. Enter to select option and Esc for close the programm."
ENDL = "\n"
SPACE = " "

class MainMenu: 
    @abstractmethod
    def map():
        while True:
            os.system("cls||clear")
            print(ENDL + SPACE + Fore.LIGHTRED_EX + DESCRIPTION + "\n\n")
            print(SPACE + Fore.YELLOW + 'Element 1')
            print(SPACE + Fore.YELLOW + 'Element 2')
            print(SPACE + Fore.LIGHTYELLOW_EX + '\033[4m' + '_Element 3' + '\033[0m')
            print(SPACE + Fore.YELLOW + 'Element 4')
            print(SPACE + Fore.YELLOW + 'Element 5')
            time.sleep(1)
            
    
