import random
from pico2d import *
import character
import math

__author__ = 'user'

class Upgrade1:
   image = None
   global XDir
   global YDir
   def __init__(self,x,y):
        self.frameSize = 20
        self.frame = 0
        self.x = x
        self.y = y
        self.XDir = 5
        self.YDir = 7
        Upgrade1.image = load_image("resource/Upgrade/총알업그래이드.png")

   def update(self):
        self.y += self.YDir
        self.x += self.XDir

        if(self.x <= 10):
            self.XDir *= -1
        elif(self.x >= 490):
            self.XDir *= -1

        if(self.y <= 10):
            self.YDir *= -1
        elif(self.y >= 690):
            self.YDir *= -1
        # self.frame = (self.frame+1) % self.frameSize
        # self.y = self.y + 40

   def Delete(self):
        self.y = 1000
        self.x = 1000
        self.XDir = 0
        self.YDir = 0

   def get_bb(self):
        return self.x - 12, self.y - 5, self.x + 12, self.y + 10

   def draw(self):
        self.image.draw(self.x,self.y )
        #draw_rectangle(*self.get_bb())

class Upgrade2:
   image = None
   global XDir
   global YDir
   def __init__(self,x,y):
        self.frameSize = 20
        self.frame = 0
        self.x = x
        self.y = y
        self.XDir = 0
        self.YDir = 0
        Upgrade2.image = load_image("resource/Upgrade/필살기 아이템.png")

   def update(self):
        self.y += self.YDir
        self.x += self.XDir

        if(self.x <= 10):
            self.XDir *= -1
        elif(self.x >= 490):
            self.XDir *= -1

        if(self.y <= 10):
            self.YDir *= -1
        elif(self.y >= 690):
            self.YDir *= -1
        # self.frame = (self.frame+1) % self.frameSize
        # self.y = self.y + 40

   def Delete(self):
        self.y = 1000
        self.x = 1000
        self.XDir = 0
        self.YDir = 0

   def get_bb(self):
        return self.x - 12, self.y - 5, self.x + 12, self.y + 10

   def draw(self):
        self.image.draw(self.x,self.y )
        #draw_rectangle(*self.get_bb())
