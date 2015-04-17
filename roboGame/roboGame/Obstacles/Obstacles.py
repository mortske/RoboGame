__author__ = 'Mathias'


import os, sys, pygame
from pygame.locals import *

class Obstacles:
#Perhaps add function to define area of interest, i.e. horizon


    def __init__(self):
        self.horizion = 200
        self.thresh = 140
        self.shrink_factor = 10

    def find_obstacles(self, picture):
        self.pic = picture
        self.crect = pygame.Rect(375,450,50,50)
        self.ccolor = pygame.transform.average_color(self.pic, self.crect)
        self.thresholded = pygame.Surface((800,600))
        pygame.transform.threshold(self.thresholded,self.pic,self.ccolor,(self.thresh,self.thresh,self.thresh),(0,0,255),2)
        #return self.thresholded

        self.trans = pygame.transform.smoothscale(self.thresholded, (800/self.shrink_factor,600/self.shrink_factor))
        self.trans2 = pygame.transform.scale(self.trans, (800,600))

        self.mask = pygame.mask.from_threshold(self.trans2, (0,0,255), (30,30,30))
        #self.reduced_mask = self.mask.connected_component()

        self.rects = self.mask.get_bounding_rects()
        return self.rects


