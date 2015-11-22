import random
from pico2d import *
import character
import math

__author__ = 'user'

class Missile1:
   image = None
   def __init__(self,x,y):
        self.frameSize = 20
        self.frame = 0
        self.x = x
        self.y = y




   def update(self):

        self.frame = (self.frame+1) % self.frameSize
        self.y = self.y + 40



   def Delete(self):
       if(self.y > 600):
           return True
       else:
           return False

   def get_bb(self):
        return self.x - 15, self.y - 30, self.x + 15, self.y + 60

   def draw(self):
        Missile1.image = load_image("resource/missile/정조준일격.png")
        self.image.draw(self.x,self.y )
        draw_rectangle(*self.get_bb())


class Missile2:
   image = None
   def __init__(self,x,y):
        self.frameSize = 20
        self.frame = 0
        self.x = x
        self.y = y


   def get_bb(self):
        return self.x - 7, self.y - 7, self.x + 7, self.y + 7



   def MonDelete(self):
       if(self.y < 50):
           return True
       else:
           return False

   def update(self):
        self.frame = (self.frame+1) % self.frameSize
        self.y = self.y - 10
   def draw(self):
        Missile2.image = load_image("resource/missile/미사일.jpg")
        self.image.draw(self.x,self.y )
        draw_rectangle(*self.get_bb())





class Missile3:
   global Angle
   global PI
   image = None
   def __init__(self,x,y):
        self.frameSize = 20
        self.frame = 0
        self.x = x
        self.y = y
        self.Angle = 0
        self.PI = 3.141592

   def update(self, Angle):
        self.frame = (self.frame+1) % self.frameSize
        self.y = self.y - math.sin(Angle *self.PI/180) * 15
        self.x = self.x + math.cos(Angle *self.PI/180) * 15



        if(self.Angle >= 360):
            self.Angle = 0
    # m_tInfo.fX += cosf(m_fAngle * PI / 180.f) * m_fSpeed;
	# m_tInfo.fY -= sinf(m_fAngle * PI / 180.f) * m_fSpeed;

   def draw(self):
        Missile3.image = load_image("resource/missile/보스미사일.jpg")
        self.image.draw(self.x,self.y )


   def Delete(self):
       if(self.y > 600):
           return True

       elif(self.y < 50):
           return True

       elif(self.x < 20):
           return True

       elif(self.x > 480):
           return True
       else:
           return False