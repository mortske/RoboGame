__author__ = 'psk'
import os, sys, pygame
from pygame.locals import *
from VideoCapture import Device
import pygame.camera
from MotorControl.MotorControl import MotorControl
import Inputs
from GameComponents import Button
from GameComponents import Icon
import Main

class GameLoop(object):
    def __init__(self, width, height, camid):
        print "Init pygame..."
        self.width = width
        self.height = height
        self.camId=camid
        self._main=Main.Main()
        self.motor= MotorControl()
        self.inputs=Inputs.Inputs()



    def run(self):
        #Init and set up variables...
        pygame.init()
        pygame.camera.init()

        self.screen = pygame.display.set_mode((self.width+20,self.height+20))

        self._main.initialize()

        self.size=(self.width, self.height)
        self.cam = pygame.camera.Camera(self.camId,self.size,"RGB",0)
        self.cam.start()
        #self.screen = pygame.display.set_mode((self.width+20,self.heigth+20),0 )



        #Set surface to handle a frame from camera
        snapshot = pygame.surface.Surface((self.width+20,self.height+20), 0, self.screen)


        black = 0, 0, 0
        #Init gamestate
        stopped = False
        running=True
        while not stopped:


            self.screen= self._main.update(self.screen)
            snapshot = self.cam.get_image(snapshot)
            black=0,0,0
            self.screen.fill(black)
            self.screen.blit(snapshot, (0,0))
            self._main.draw(self.screen)
            pygame.display.flip()



#Testcode to run module. Standard Python way of testing modules.
#OBS !! comment out   line 47: "C:\Python27\Lib\site-packages\pygame\_camera_vidcapture.py":
#       #self.dev.setresolution(width, height) on row 49 in:
#
if __name__ == "__main__":
    #Set to webcam ID, std is 0. Networkedcam is probably 1
    camid=0
    #Set to resolution of your webcam
    width= 640
    height=480

    gl=GameLoop(width,height, camid)
    gl.run()