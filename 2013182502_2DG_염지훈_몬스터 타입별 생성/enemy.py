import random
from pico2d import *

__author__ = 'user'


class Enemy:

   global Type

   Type = True

   def __init__(self,x,y):
        self.x = x
        self.y = y
        self.startx = self.x
        self.frame = random.randint(0, 5)
        self.dir = -1
        self.randNum = random.randint(10,150)

   def update(self):
        if(self.y >= 600):
            self.y += (self.dir * 5)
        else:
            self.x += (self.dir * 5)
            if(self.x <= 20):
                self.dir *= -1

            elif(self.x >= 480):
                self.dir *= -1


        if(self.y < 0 ):
            self.y = 810

        if(Type == True):
            Enemy.image = load_image("resource/enemy/enemy1.png")

        elif(Type == False):
            Enemy.image = load_image("resource/enemy/비행기 폭발 모션.png")

   def get_bb(self):
        return self.x - 35, self.y - 40, self.x + 35, self.y + 40

   def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())



