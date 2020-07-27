from MotorsWork import drive
from MotorsWork import turn
from time import *

from State_driving import State
from Frontend import graphic_simple_drive



driv = drive.Drive()
turns = turn.Turn()


class Main:
    def __init__(self):
        self.state = State.STOP
        self.simple_drive_controll()

    def simple_drive_controll(self):
        simple_drive = graphic_simple_drive.SimpleControl()
        # simple_drive.simple_window.mainloop()
        print('hi')
        self.state = simple_drive.state
        print(self.state)
        while self.state == State.SIMPLEDRIVE:
            print('while Schlaufe')
            state = str(simple_drive.drive_forward['state'])
            if state == 'disabled':
                driv.Forward()

            elif str(simple_drive.drive_back['state'] == 'normal'):
                driv.Back()



