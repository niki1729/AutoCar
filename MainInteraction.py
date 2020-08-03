from tkinter import *
from State_driving import state
from time import sleep
from DifferentDrivingCommands import ASDWDiriving



control_window_width = 500
control_window_height = 500

asdw = ASDWDiriving.ASDWDriving()



class Display:
    """
    This class display a window with what you can control the car in different possibilities
    """

    def __init__(self):
        """Creation of the window it self with the basic keys"""
        control_window = Tk()
        control_window.geometry(str(control_window_width) + 'x' + str(control_window_height))
        control_window.title("AutoCar")

        # stands for control window Cnavas
        self.control_w_c = Canvas(control_window, width=control_window_width, height=control_window_height)
        self.control_w_c.place(x=0, y=0)

        self.label = Label(self.control_w_c, text="Control Panel of the Car \n choose how you want to control it",
                           font=("Ariel", 15))
        self.label.place(x=control_window_width / 2, y=10, anchor=N)

        self.button_asdw_drive = Button(self.control_w_c, text="drive with 'ASWD'", font=("Ariel", 10),
                                        command=self.ASDW_driving_command)
        self.button_asdw_drive.place(x=10, y=control_window_height / 5, anchor=W)

    def ASDW_driving_command(self):
        if state != state.ASDW:
            self.button_asdw_drive.configure(fg="green")
            asdw.asdw_window_f()
            asdw.asdw_window.protocol("WM_DELETE_WINDOW", lambda: [self.all_keys_black(), asdw.destroy_asdw_w("")])
            asdw.asdw_window.bind('<KeyPress-q>', lambda event: [self.all_keys_black(), asdw.destroy_asdw_w("")])

    def all_keys_black(self):
        self.button_asdw_drive.configure(fg="black")


display = Display()
mainloop()
