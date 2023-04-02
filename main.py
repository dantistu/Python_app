import os
import platform

os_name = platform.system()
print(f'Current OS: {os_name}')

match os_name:
    case "Windows":
        os.system('mode con: cols=100 lines=25')
    case "Linux":
        os.system('resize -s 25 100')
    case _:
        pass

from cli.interface import MainMenu


if __name__ == "__main__":
    MainMenu.map()
    

