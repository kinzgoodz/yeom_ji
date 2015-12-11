import random
from pico2d import *
import character
import math

__author__ = 'user'

class PowerAttack1:
   image = None
   global XDir
   global YDir
   global Time
   def __init__(self,x,y):
        self.frameSize = 20
        self.frame = 0
        self.x = x
        self.y = y
        self.XDir = 5
        self.YDir = 3
        self.Time = 0
        PowerAttack1.image = load_image("resource/PowerAttack/필살기 비행기.png")

   def update(self):
        self.y += self.YDir

        if(self.y >= 200):
            if(self.Time == 50):
                self.YDir = 15
            else:
                self.YDir = 0
                self.Time += 1
        # self.frame = (self.frame+1) % self.frameSize
        # self.y = self.y + 40

   def Delete(self):
        if(self.y >= 750):
            return True
        else:
            return False

   def get_bb(self):
        return self.x - 200, self.y - 30, self.x + 200, self.y - 0


   def get_bb2(self):
        return self.x - 100, self.y + 0, self.x + 100, self.y + 100




   def draw(self):
        self.image.draw(self.x,self.y )
        #draw_rectangle(*self.get_bb())
        #draw_rectangle(*self.get_bb2())

