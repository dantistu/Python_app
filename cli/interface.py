from abc import abstractmethod
import os
import time
from colorama import Fore


class MainMenu: 
    @abstractmethod
    def map():
        while True:
            print(Fore.BLUE + 'Синий текст')
            time.sleep(1)
            os.system("cls||clear")
    
