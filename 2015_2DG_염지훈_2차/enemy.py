import random
from pico2d import *

__author__ = 'user'


class Enemy:
   image = None
   frameSize = 5
   jump = True
   dir
   LEFT_IDLE, RIGHT_IDLE, LEFT_RUN, RIGHT_RUN,LEFT_HIT,RIGHT_HIT,LEFT_DIE,RIGHT_DIE =7,6,5,4,3,2,1,0

   def __init__(self):
        self.x, self.y = random.randint(0,500), random.randint(800,1500)
        self.startx = self.x
        self.frame = random.randint(0, 5)
        self.state = self.LEFT_RUN
        self.dir = -1
        self.randNum = random.randint(10,150)
   def update(self):
        self.frame = (self.frame+1) % self.frameSize
        self.y += (self.dir * 5)
        # if(self.x > self.startx + self.randNum):
        #     self.dir = -1
        # elif(self.x < self.startx - self.randNum):
        #     self.dir = 1
        if(self.x < 0 ):
            self.x = 810

        Enemy.image = load_image("resource/enemy/enemy1.png")
   def draw(self):
        self.image.draw(self.x,self.y)




