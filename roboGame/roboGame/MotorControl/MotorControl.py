__author__ = 'Mathias'



import os, sys, pygame
from pygame.locals import *

class MotorControl:


    def __init__(self):
        self.speed = 1
        self.turn = 1

        self.signalValueLeftWheel = 0
        self.signalValueRightWheel = 0

        #constants
        self.speedIncrement = 1

    def update_motor(self, speed, turn):
        #speed: 0 - decrease
        #       1 - do nothing
        #       2 - increase
        #turn:
        #       0 - more left
        #       1 - do nothing
        #       2 - more right

        if speed==0:
            self.signalValueLeftWheel = self.signalValueLeftWheel - self.speedIncrement
            self.signalValueRightWheel = self.signalValueRightWheel - self.speedIncrement
        elif speed==2:
            self.signalValueLeftWheel = self.signalValueLeftWheel + self.speedIncrement
            self.signalValueRightWheel = self.signalValueRightWheel + self.speedIncrement

