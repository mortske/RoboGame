__author__ = 'psk'
import Main
import pygame
import sys
from GameComponents import Button
from pygame.locals import *

class Inputs(object):
    #def __init__(self):

    def initialize(self):
        #Array/collection of buttons
        self.Buttons={}
        self.Buttons["stopStartB"] = Button.Button((0,200,40, 40))
        self.Buttons["stopStartB"].color=(0,0,0,0)
        self.Buttons["stopStartB"].iconFg= pygame.image.load("icons/pause.png")

        self.Buttons["stopB"] = Button.Button((0,250,40, 40))
        self.Buttons["stopB"].color=(0,0,0,0)
        self.Buttons["stopB"].iconFg= pygame.image.load("icons/stop.png")
        self.Buttons["stopB"].callback = sys.exit


    def update(self,screen):
        for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if(event.type is MOUSEBUTTONDOWN):
                    pos = pygame.mouse.get_pos()

                    for button in self.Buttons:
                        self.Buttons[button].selected(pos)

    def draw(self, screen):
        for button in self.Buttons:
            self.Buttons[button].draw(screen)
        return screen

  #  def _startStop(self):
