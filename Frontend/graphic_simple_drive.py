from tkinter import *
from time import *
from MotorsWork import drive
from MotorsWork import turn

driv = drive.Drive()
turns = turn.Turn()


class SimpleControl:
    """
    Little class to control the car with back, forward, left and right
    """

    def __init__(self):
        self.simple_window = Tk()
        self.simple_window.geometry("250x100")
        self.two_buttons = Canvas(self.simple_window)
        self.two_buttons.grid()

        self.drive_forward = Button(self.two_buttons, text="forward",
                                    command=lambda: [driv.Forward(), self.block_the_button(1)])
        self.drive_forward.grid(row=0, column=1)

        self.drive_back = Button(self.two_buttons, text="back", command=lambda: [driv.Back(), self.block_the_button(2)])
        self.drive_back.grid(row=2, column=1)

        self.turn_left = Button(self.two_buttons, text="left",
                                command=lambda: [turns.turn_left(), self.block_the_button(3)])
        self.turn_left.grid(row=1, column=0)

        self.turn_right = Button(self.two_buttons, text="right",
                                 command=lambda: [turns.turn_right(), self.block_the_button(4)])
        self.turn_right.grid(row=1, column=2)

        self.stop = Button(self.two_buttons, text="stops", command=lambda: self.block_the_button(0))
        self.stop.grid(row=1, column=1)

    def block_the_button(self, button):
        if int(button) == 1:
            self.drive_forward.config(state=DISABLED)

            self.drive_back.config(state=NORMAL)
            self.turn_left.config(state=NORMAL)
            self.turn_right.config(state=NORMAL)

        if int(button) == 2:
            self.drive_back.config(state=DISABLED)

            self.drive_forward.config(state=NORMAL)
            self.turn_left.config(state=NORMAL)
            self.turn_right.config(state=NORMAL)

        if int(button) == 3:
            self.turn_left.config(state=DISABLED)

            self.drive_forward.config(state=NORMAL)
            self.drive_back.config(state=NORMAL)
            self.turn_right.config(state=NORMAL)

        if int(button) == 4:
            self.turn_right.config(state=DISABLED)

            self.drive_forward.config(state=NORMAL)
            self.drive_back.config(state=NORMAL)
            self.turn_left.config(state=NORMAL)

        if int(button) == 0:
            self.drive_forward.config(state=NORMAL)
            self.drive_back.config(state=NORMAL)
            self.turn_left.config(state=NORMAL)
            self.turn_right.config(state=NORMAL)

    def update_each_second(self):
        time = localtime()



s = SimpleControl()

mainloop()
