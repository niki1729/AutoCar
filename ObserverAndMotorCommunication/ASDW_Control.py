from nanpy import (ArduinoApi, SerialManager)
from time import sleep

forward_d = 8
back_d = 9
r_turn = 7
l_turn = 2


class MotorController:
    """
    Controller of the motors through arduino and probably through H-Bridge
    Used from different parts of the programme. It only gets the command to start or stop some mouvements
    """
    def __init__(self):
        """
        Creation of connection to the arduino through nanpy and initialisation of the used Pins
        """

        try:
            connection = SerialManager()
            self.asdw_m = ArduinoApi(connection=connection)
            print("failed to upload")

        except:
            print("didn't worked")

        self.asdw_m.pinMode(l_turn, self.asdw_m.OUTPUT)
        self.asdw_m.pinMode(back_d, self.asdw_m.OUTPUT)
        self.asdw_m.pinMode(r_turn, self.asdw_m.OUTPUT)
        self.asdw_m.pinMode(forward_d, self.asdw_m.OUTPUT)

    def drive_forward(self):
        self.asdw_m.digitalWrite(forward_d, self.asdw_m.HIGH)

    def drive_back(self):
        self.asdw_m.digitalWrite(back_d, self.asdw_m.HIGH)

    def turn_right(self):
        self.asdw_m.digitalWrite(r_turn, self.asdw_m.HIGH)

    def turn_left(self):
        self.asdw_m.digitalWrite(l_turn, self.asdw_m.HIGH)

    # part to stop the mouvement or the turn
    def stop_drive(self):
        self.asdw_m.digitalWrite(back_d, self.asdw_m.LOW)
        self.asdw_m.digitalWrite(forward_d, self.asdw_m.LOW)

    def stop_turn(self):
        self.asdw_m.digitalWrite(l_turn, self.asdw_m.LOW)
        self.asdw_m.digitalWrite(r_turn, self.asdw_m.LOW)

    def d_motor_off(self):
        pass

    def w_motor_off(self):
        pass

