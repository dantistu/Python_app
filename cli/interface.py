from abc import abstractmethod
import os
import time
from colorama import Fore


class MainMenu: 
    @abstractmethod
    def map():
        while True:
            print(Fore.YELLOW + 'Element 1')
            print(Fore.YELLOW + 'Element 2')
            print(Fore.YELLOW + 'Element 3')
            print(Fore.YELLOW + 'Element 4')
            print(Fore.YELLOW + 'Element 5')
            time.sleep(1)
            os.system("cls||clear")
    
