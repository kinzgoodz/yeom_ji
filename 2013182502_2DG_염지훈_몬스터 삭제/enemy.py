import random
from pico2d import *

__author__ = 'user'


class Enemy:

   def __init__(self):
        self.x, self.y = random.randint(0,500), random.randint(800,1500)
        self.startx = self.x
        self.frame = random.randint(0, 5)
        self.dir = -1
        self.randNum = random.randint(10,150)

   def update(self):
        self.y += (self.dir * 5)
        if(self.y < 0 ):
            self.y = 810
        Enemy.image = load_image("resource/enemy/enemy1.png")

   def get_bb(self):
        return self.x - 35, self.y - 40, self.x + 35, self.y + 40

   def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())



