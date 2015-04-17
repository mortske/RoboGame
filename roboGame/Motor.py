__author__ = 'psk'

import pygame
import MotorControl

class Motor(object):
    def __init__(self):
        self.timer = 0
        self.adjustment = 0.01
        #self.motor= MotorControl.MotorControl()

#    def Initialize(self):

    def update(self,screen,forwardbackward, sideways):
        speed=1
        if self.timer > 1:
            self.timer = 0
            #update motor forward with 2
            speed=2


        if self.timer < -1:
            self.timer = 0;
            #update motor backward with 0
            speed=0

        if forwardbackward == 1:
            self.timer = self.timer + self.adjustment

        if forwardbackward == -1:
            self.timer = self.timer - self.adjustment

        if forwardbackward == 0:
            if self.timer != 0:
                self.timer = 0
        #self.motor.update_motor(speed,1)
        return screen

    def draw(self, screen):
        myfont = pygame.font.SysFont("Arial", 40)
        label = myfont.render(str(self.timer), 1, (255,255,255))
        screen.blit(label, (700,200))
