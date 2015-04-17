__author__ = 'Mathias'

# import os, sys, pygame
# from pygame.locals import *

#import clr
#clr.AddReference("SMAPi")
#import Smapi


class MotorControl:
    def __init__(self):
        self.speed = 1
        self.turn = 1

        # Range: 0->20480, 0x0000->0x5000
        self.signalValueLeftWheel = 0
        self.signalValueRightWheel = 0

        # Constants
        self.speedIncrement = 20

        # Connect to COO8


        # Check if COO8 is connected!

    def update_motor(self, speed, turn):
        # speed:
        #       0 - decrease
        #       1 - do nothing
        #       2 - increase
        # turn:
        #       0 - more left
        #       1 - do nothing
        #       2 - more right

        if speed == 0:
            self.signalValueLeftWheel = self.signalValueLeftWheel - self.speedIncrement
            self.signalValueRightWheel = self.signalValueRightWheel - self.speedIncrement
        elif speed == 2:
            self.signalValueLeftWheel = self.signalValueLeftWheel + self.speedIncrement
            self.signalValueRightWheel = self.signalValueRightWheel + self.speedIncrement

        leftHighByte = (self.signalValueLeftWheel & 0xff00) >> 8
        leftLowByte  = (self.signalValueLeftWheel & 0x00ff)

        rightHighByte = (self.signalValueRightWheel & 0xff00) >> 8
        rigthLowByte  = (self.signalValueRightWheel & 0x00ff)

        #status, response = self.coo8.GeneralRequest([0x2F, 0xF0, 0x52, 0x06, leftHighByte, leftLowByte], None)
        #status, response = self.coo8.GeneralRequest([0x2F, 0xF0, 0x51, 0x06, rightHighByte, rigthLowByte], None)