import os


class Turn:
    """
    This class works or with arduino or with the motors directly through relays and turn right or left
    """

    def __init__(self):
        self.IN1 = 6  # IN1
        self.IN2 = 13  # IN2
        self.IN3 = 19  # IN3
        self.IN4 = 26  # IN4

    def turn_right(self):
        print('turn_right')

    def turn_left(self):
        print('turn_left')
