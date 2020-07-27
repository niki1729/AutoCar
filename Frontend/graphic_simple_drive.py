from tkinter import *
from MotorsWork import drive
from MotorsWork import turn

driv = drive.Drive()
turns = turn.Turn()


class SimpleControl:
    def __init__(self):
        self.simple_window = Tk()
        self.simple_window.geometry("250x100")
        self.two_buttons = Canvas(self.simple_window)
        self.two_buttons.grid()

        self.drive_forward = Button(self.two_buttons, text="forward", command=driv.Forward)
        self.drive_forward.grid(row=0, column=1)

        self.drive_back = Button(self.two_buttons, text="back", command=driv.Back)
        self.drive_back.grid(row=2, column=1)

        self.drive_left = Button(self.two_buttons, text="left", command=turns.turn_left)
        self.drive_left.grid(row=1, column=0)

        self.drive_right = Button(self.two_buttons, text="right", command=turns.turn_right)
        self.drive_right.grid(row=1, column=2)

s=SimpleControl()

mainloop()
