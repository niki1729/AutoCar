# import RPi.GPIO as GPIO
import os


class Drive:
    """
    This class works or with arduino or with the motors directly through relays and drive right or left
    """

    def __init__(self):
        print('Init from drive.py in MotorsWork')
        IN1 = 6  # IN1
        IN2 = 13  # IN2
        IN3 = 19  # IN3
        IN4 = 26  # IN4

    def Forward(self):
        print("forward")

    def Back(self):
        print("bacwards")
