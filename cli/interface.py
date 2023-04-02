from abc import abstractmethod
import os
import time


class MainMenu: 
    @abstractmethod
    def map():
        while True:
            print("menu")
            time.sleep(1)
            os.system("cls||clear")
    
