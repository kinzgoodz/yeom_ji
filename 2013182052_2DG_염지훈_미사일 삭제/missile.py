import random
from pico2d import *
import character

__author__ = 'user'

class Missile1:
   image = None
   def __init__(self,x,y):
        self.frameSize = 20
        self.frame = 0
        self.x = x
        self.y = y




   def update(self):
        Missile1.image = load_image("resource/missile/missile1.png")
        self.frame = (self.frame+1) % self.frameSize
        self.y = self.y + 40



   def Delete(self):
       if(self.y > 600):
           return True
       else:
           return False



   def draw(self):

        self.image.draw(self.x,self.y )


class Missile2:
   image = None
   def __init__(self,x,y):
        self.frameSize = 20
        self.frame = 0
        self.x = x
        self.y = y

   def update(self):
        Missile2.image = load_image("resource/missile/missile2.png")
        self.frame = (self.frame+1) % self.frameSize
        self.y = self.y+ 40
   def draw(self):
        self.image.draw(self.x,self.y )



   def Delete(self):
       if(self.y > 600):
           return True
       else:
           return False


class Missile3:
   image = None
   def __init__(self,x,y):
        self.frameSize = 20
        self.frame = 0
        self.x = x
        self.y = y

   def update(self):
        Missile3.image = load_image("resource/missile/missile3.png")
        self.frame = (self.frame+1) % self.frameSize
        self.y = self.y+ 40


   def draw(self):

        self.image.draw(self.x,self.y )


   def Delete(self):
       if(self.y > 600):
           return True
       else:
           return False