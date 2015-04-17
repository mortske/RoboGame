__author__ = 'psk'
import Main
import pygame
import sys
from GameComponents import Button
from pygame.locals import *

class Inputs(object):
    def __init__(self):
        self.forward = 1

    def initialize(self):
        #Array/collection of buttons
        self.Buttons={}
        self.Buttons["stopStartB"] = Button.Button((700,200,40, 40))
        self.Buttons["stopStartB"].color=(0,0,0,0)
        self.Buttons["stopStartB"].iconFg= pygame.image.load("icons/Frame_Up.png")
        self.Buttons["stopStartB"].iconFg.convert_alpha()
        self.Buttons["stopStartB"].iconFgPressed = pygame.image.load("icons/Frame_Down.png")

        self.Buttons["stopB"] = Button.Button((0,250,40, 40))
        self.Buttons["stopB"].color=(0,0,0,0)
        self.Buttons["stopB"].iconFg= pygame.image.load("icons/stop.png")
        self.Buttons["stopB"].callback = sys.exit

    def update(self,screen):
        for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                self.forward = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.forward = 1
                    if event.key == pygame.K_DOWN:
                        self.forward = -1

                if(event.type is MOUSEBUTTONDOWN):
                    pos = pygame.mouse.get_pos()

                    for button in self.Buttons:
                        self.Buttons[button].selectedImage = self.Buttons[button].iconFgPressed

                if(event.type is MOUSEBUTTONUP):
                    for button in self.Buttons:
                        self.Buttons[button].selectedImage = self.Buttons[button].iconFg


    def draw(self, screen):
        for button in self.Buttons:
            self.Buttons[button].draw(screen)
        return screen

    def GetForwardBackward(self):
        return self.forward;
   # def _startStop(self):

