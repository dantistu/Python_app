import msvcrt

class WASDController:
    def __init__(self):
        self.running = True

    async def run(self):
        while self.running:
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'w':
                self.move_up()
            elif key == 'a':
                self.move_left()
            elif key == 's':
                self.move_down()
            elif key == 'd':
                self.move_right()
            elif key == '\r':
                self.enter()
            elif key == '\x1b':
                self.esc()

    def move_up(self):
        print('Moving up')
        

    def move_left(self):
        print('Moving left')

    def move_down(self):
        print('Moving down')

    def move_right(self):
        print('Moving right')

    def enter(self):
        print('Enter pressed')

    def esc(self):
        print('Esc pressed')
        self.running = False

controller = WASDController()
controller.run()