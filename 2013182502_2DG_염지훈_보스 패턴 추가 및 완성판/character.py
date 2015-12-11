import random
from pico2d import *



__author__ = 'user'

from missile import Missile1
from missile import Missile2
from missile import Missile3
import main_state

class character:
   global missile1,missile2,missile3
   image = None

   global bullet1,bullet2,bullet3

   #bullet1 = []
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
   missile2 = Missile1(0,0)
   missile2 = Missile2(0,0)
   missile3 = Missile3(0,0)

   def __init__(self):

        self.x, self.y = 250,50

        self.missilex = self.x

        character.image = load_image("resource/character/character.png")


   def handle_event(self, event):
        global mis
        global left,right,up,down
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):

                left = True
        if(event.type, event.key) == (SDL_KEYDOWN,SDLK_RIGHT):

                right = True
        if(event.type, event.key) == (SDL_KEYDOWN,SDLK_UP):

                up = True
        if(event.type, event.key) == (SDL_KEYDOWN,SDLK_DOWN):

                down = True
        if(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
                left = False
        if(event.type, event.key) == (SDL_KEYUP,SDLK_RIGHT):

                right = False
        if(event.type, event.key) == (SDL_KEYUP,SDLK_UP):

                up = False
        if(event.type, event.key) == (SDL_KEYUP,SDLK_DOWN):

                down = False

   def get_bb(self):
        return self.x - 35, self.y - 25, self.x + 35, self.y + 25

   def update(self):
       global left,right,up,down

       if(left == True):
           self.x -=10
           if(self.x <= 10):
               self.x = 10
       if(right == True):
           self.x +=10
           if(self.x >= 490):
               self.x = 490
       if(up == True):
           self.y +=10
           if(self.y >= 690):
               self.x = 690
       if(down == True):
           self.y -=10
           if(self.y <= 10):
               self.y = 10


   def draw(self):
        self.image.draw(self.x,self.y)
        #draw_rectangle(*self.get_bb())