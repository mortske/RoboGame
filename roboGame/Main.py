__author__ = 'psk'

import Motor
import Inputs
class Main(object):
    def __init__(self):
        self._motor=Motor.Motor()
        self._inputs=Inputs.Inputs()

    def initialize(self):
        print "Main init..."
        self._inputs.initialize()

    def update(self,screen):
        self._inputs.update(screen)
        self._motor.update(screen,self._inputs.GetForwardBackward(), 1)
        return screen

    def draw(self, screen):
        black = 0, 0, 0
        self._inputs.draw(screen)
        self._motor.draw(screen)
        return screen
