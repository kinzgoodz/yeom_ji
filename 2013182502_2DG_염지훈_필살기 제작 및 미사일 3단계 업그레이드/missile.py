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
       if(self.y > 700):
           return True
       else:
           return False

   def get_bb(self):
        return self.x - 12, self.y - 5, self.x + 12, self.y + 10

   def draw(self):
        Missile1.image = load_image("resource/missile/정조준일격.png")
        self.image.draw(self.x,self.y )
        draw_rectangle(*self.get_bb())

class UpMissile:
   image = None
   def __init__(self,x,y):
        self.frameSize = 20
        self.frame = 0
        self.x = x
        self.y = y
        UpMissile.image = load_image("resource/missile/플레이어미사일2.png")

   def update(self):

        self.frame = (self.frame+1) % self.frameSize
        self.y = self.y + 40

   def Delete(self):
       if(self.y > 700):
           return True
       else:
           return False

   def get_bb(self):
        return self.x - 12, self.y - 5, self.x + 12, self.y + 10

   def draw(self):
        self.image.draw(self.x,self.y )
        draw_rectangle(*self.get_bb())

class UpMissile2:
   image = None
   def __init__(self,x,y):
        self.frameSize = 20
        self.frame = 0
        self.x = x
        self.y = y
        UpMissile2.image = load_image("resource/missile/최종미사일.png")

   def update(self):

        self.frame = (self.frame+1) % self.frameSize
        self.y = self.y + 40

   def Delete(self):
       if(self.y > 700):
           return True
       else:
           return False

   def get_bb(self):
        return self.x - 12, self.y - 5, self.x + 12, self.y + 10

   def draw(self):
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
       if(self.y <= 0):
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
        self.Angle = 0.0
        self.PI = 3.141592
        #Missile3.image = load_image("resource/missile/보스미사일.jpg")


   def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

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
        draw_rectangle(*self.get_bb())


   def Delete(self):
       if(self.y > 700):
           return True

       elif(self.y < 0):
           return True

       elif(self.x < 0):
           return True

       elif(self.x > 500):
           return True
       else:
           return False



class Missile4:
   global Angle
   global PI
   global Width
   global Height
   global Distance
   image = None
   def __init__(self,x,y):
        self.frameSize = 20
        self.frame = 0
        self.x = x
        self.y = y
        self.Angle = 0.0
        self.PI = 3.141592
        self.Width = 0.0
        self.Height = 0.0
        self.Distance = 0.0
        Missile4.image = load_image("resource/missile/중보스미사일.jpg")


   def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15

   def update(self, playerx, playery):
        self.frame = (self.frame+1) % self.frameSize

        if(playery <= self.y):
            self.Height = self.y - playery
        elif(playery >= self.y):
            self.Height =  playery - self.y
        self.Width = playerx - self.x
        self.Distance = math.sqrt(self.Width * self.Width) + (self.Height + self.Height)
        self.Angle = math.acos(self.Width / self.Distance)


        if(playery >= self.y):
            self.Angle = 2 * self.PI - self.Angle

        self.y = self.y - math.sin(self.Angle) * 5
        self.x = self.x + math.cos(self.Angle) * 5

	# if(m_pPlayer->GetInfo().fY > m_tInfo.fY)
	# {
	# 	m_fAngle = 2 * PI - m_fAngle;
	# }

        # if(self.Angle >= 360):
        #     self.Angle = 0
    # m_tInfo.fX += cosf(m_fAngle * PI / 180.f) * m_fSpeed;
	# m_tInfo.fY -= sinf(m_fAngle * PI / 180.f) * m_fSpeed;

   def draw(self):
        #Missile4.image = load_image("resource/missile/중보스미사일.jpg")
        self.image.draw(self.x,self.y )
        draw_rectangle(*self.get_bb())


   def Delete(self):
       # if(self.y > 600):
       #     return True

       if(self.y < 50):
           return True

       elif(self.x < 0):
           return True

       elif(self.x > 500):
           return True
       else:
           return False