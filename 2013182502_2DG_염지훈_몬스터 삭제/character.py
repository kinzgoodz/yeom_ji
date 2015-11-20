import random
from pico2d import *



__author__ = 'user'

from missile import Missile1
from missile import Missile2
from missile import Missile3

class character:
   global missile1,missile2,missile3
   image = None
   hpbar = None
   frameSize =9
   jump = True
   gravity = -30
   jumpMove = 0
   UP,DOWN,LEFT_RUN,RIGHT_IDLE,RIGHT_RUN,RIGHT_ATTACK =5,4,3,2,1,0
   global bullet1,bullet2,bullet3
   bullet1 = []
   bullet2 = []
   bullet3 = []

   global left
   global right
   global  up
   global down

   left = False
   right = False
   up = False
   down = False
   missile1 = Missile1(0,0)
   missile2 = Missile2(0,0)
   missile3 = Missile3(0,0)

   def __init__(self):

        self.x, self.y = 50,300
        self.frame = random.randint(0, 1) # 셀프가 뭔지
        self.state = self.RIGHT_IDLE
        self.gravity = 10 # 그래비티는 뭔지
        self.missilex = self.x
        # character.image = load_image("resource/character/idle/Kyo Kusanagi_%d.png"%self.frame)


   def handle_event(self, event):
        global mis
        global left,right,up,down
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                # self.state = self.LEFT_RUN
                left = True
        if(event.type, event.key) == (SDL_KEYDOWN,SDLK_RIGHT):
                # self.state = self.RIGHT_RUN
                right = True
        if(event.type, event.key) == (SDL_KEYDOWN,SDLK_UP):
                # self.state = self.UP
                up = True
        if(event.type, event.key) == (SDL_KEYDOWN,SDLK_DOWN):
                 # self.state = self.DOWN
                down = True
        if(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                # self.state = self.LEFT_RUN
                left = False
        if(event.type, event.key) == (SDL_KEYUP,SDLK_RIGHT):
                # self.state = self.RIGHT_RUN
                right = False
        if(event.type, event.key) == (SDL_KEYUP,SDLK_UP):
                # self.state = self.UP
                up = False
        if(event.type, event.key) == (SDL_KEYUP,SDLK_DOWN):
                 # self.state = self.DOWN
                down = False

        #
        # elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
        #     if self.state in (self.LEFT_RUN,self.RIGHT_RUN,):
        #         self.state = self.RIGHT_IDLE
        # elif(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
        #     if self.state in (self.LEFT_RUN,self.RIGHT_RUN):
        #         self.state = self.RIGHT_IDLE
        # elif(event.type, event.key) == (SDL_KEYUP, SDLK_UP):
        #     if self.state in (self.LEFT_RUN,self.RIGHT_RUN,self.UP):
        #         self.state = self.RIGHT_IDLE
        # elif(event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
        #     if self.state in (self.LEFT_RUN,self.RIGHT_RUN,self.DOWN):
        #         self.state = self.RIGHT_IDLE






         # 공격
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            if self.state in (self.RIGHT_IDLE,):
                self.state = self.RIGHT_ATTACK
                self.frameSize = 2
            bullet1.append(Missile1(self.x,self.y+25))
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_a):
            if self.state in (self.RIGHT_ATTACK,):
                self.state = self.RIGHT_IDLE

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            if self.state in (self.RIGHT_IDLE,):
                self.state = self.RIGHT_ATTACK
                self.frameSize = 2
            bullet2.append(Missile2(self.x,self.y+25))
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_z):
            if self.state in (self.RIGHT_ATTACK,):
                self.state = self.RIGHT_IDLE

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            if self.state in (self.RIGHT_IDLE,):
                self.state = self.RIGHT_ATTACK
                self.frameSize = 2
            bullet3.append(Missile3(self.x,self.y+25))
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_x):
            if self.state in (self.RIGHT_ATTACK,):
                self.state = self.RIGHT_IDLE

   def get_bb(self):
        return self.x - 35, self.y - 25, self.x + 35, self.y + 25

   def update(self):
       global left,right,up,down
       global bullet1,bullet2,bullet3
       for bull1 in bullet1:
            bull1.update()
       for bull2 in bullet2:
            bull2.update()
       for bull3 in bullet3:
            bull3.update()
       self.frame = (self.frame+1) % self.frameSize
       missile1.update()
       missile2.update()
       missile3.update()
       self.missilex = self.missilex+3

       if(left == True):
           self.x -=10
       if(right == True):
           self.x +=10
       if(up == True):
           self.y +=10
       if(down == True):
           self.y -=10
       for member in bullet1 :
           overmap = member.Delete()
           if overmap == True :
                bullet1.remove(member)

       for member2 in bullet2 :
           overmap2 = member2.Delete()
           if overmap2 == True :
                bullet2.remove(member2)


       for member3 in bullet3 :
           overmap3 = member3.Delete()
           if overmap3 == True :
                bullet3.remove(member3)




       if self.state == self.RIGHT_RUN:
             self.x = min(800,self.x+5)
       if self.state == self.LEFT_RUN:
              self.frameSize = 9
              self.x = max(0,self.x-5)
       if self.state == self.RIGHT_IDLE:
              self.frameSize = 10
       if self.state == self.UP:
              self.y = self.y+10
       if self.state == self.DOWN:
              self.y = self.y-10

        # 공격
       elif self.state == self.RIGHT_ATTACK:
            self.frameSize = 2
       if self.state == self.RIGHT_IDLE:
             character.image = load_image("resource/character/character.png")
       elif self.state == self.RIGHT_RUN:
              character.image = load_image("resource/character/character.png")
       elif self.state == self.RIGHT_ATTACK:
              character.image = load_image("resource/character/character.png")


   def draw(self):
        global bull1,bull2,bull3
        self.image.draw(self.x,self.y)
        # missile1.draw()
        for bull1 in bullet1:
            bull1.draw()
        for bull2 in bullet2:
            bull2.draw()
        for bull3 in bullet3:
            bull3.draw()

        draw_rectangle(*self.get_bb())