import random
from pico2d import *

import main_state
__author__ = 'user'


iCount = 1


class Enemy:
   global Type
   global iCount
   global NHp
   global Time

   def __init__(self,x,y):
        self.x = x
        self.y = y
        #self.x, self.y = random.randint(0,500), random.randint(800,1500)
        self.startx = self.x
        self.frame = random.randint(0, 5)
        self.dir = -1
        self.randNum = random.randint(10,150)
        Enemy.image = load_image("resource/enemy/enemy1.png")
        self.Type = 1
        self.NHp = 2
        self.Time = 0

   def Variable(self):
        if(self.Type == 2):
            self.image = load_image("resource/enemy/비행기 폭발 모션.png")
            print("이미지변환 조건 실행")
            return True

        else:
            return False

   def AAA(self):
        self.Time += 1

        if(self.Time == 50):
            self.Time = 0
            return True
   def Power(self):
       self.NHp -=2
       self.Type = 2
       return True

   def Hp(self):

        self.NHp -= 1
        print("HP함수 실행 현재 HP : %d", self.NHp)
        if(self.NHp == 0):
            print("비행기 격파")
            #self.NHp = 3
            self.Type = 2
            return True
        else:
            return False



   def update(self):
        if(self.Type == 1):
            if(self.y >= 600):
                self.y += (self.dir * 5)
            else:
                self.x += (self.dir * 5)
                if(self.x <= 0):
                    self.dir *= -1

                elif(self.x >= 500):
                    self.dir *= -1

        elif(self.Type == 2):
            print("파괴실행")



#        if(self.Type == 2):
 #            Enemy.image = load_image("resource/enemy/비행기 폭발 모션.png")



   def get_bb(self):
        return self.x - 35, self.y - 40, self.x + 35, self.y + 40

   def draw(self):
        self.image.draw(self.x,self.y)
        #draw_rectangle(*self.get_bb())

class Enemy2:
   global Type
   global iCount
   global BHp

   def __init__(self,x, y):
        self.x = x
        self.y = y
        #self.x, self.y = random.randint(0,500), random.randint(800,1500)
        self.startx = self.x
        self.frame = random.randint(0, 5)
        self.dir = -1
        self.randNum = random.randint(10,150)
        Enemy2.image = load_image("resource/enemy/boss.png")
        self.Type = 1
        self.BHp = 100

   def Variable(self):
        if(self.Type == 2):
            self.image = load_image("resource/enemy/비행기 폭발 모션.png")
            print("이미지변환 조건 실행")
            return True

        else:
            return False

   def Power(self):
       self.BHp -= 10
       print("HP함수 실행 현재 HP : %d", self.BHp)
       if(self.BHp <= 0):
            print("비행기 격파")
            self.Type = 2

   def Hp(self):
        self.BHp -= 1
        print("HP함수 실행 현재 HP : %d", self.BHp)
        if(self.BHp == 0):
            print("비행기 격파")
            self.Type = 2
            return True
        else:
            return False


   def update(self):
            if(self.y >= 600):
                self.y += (self.dir * 10)
            else:
                self.y = 599
                #self.x += (self.dir * 1)
                # if(self.x < 245):
                #     self.dir *= -1
                # elif(self.x > 255):
                #     self.dir *= -1











#        if(self.Type == 2):
 #            Enemy.image = load_image("resource/enemy/비행기 폭발 모션.png")



   def get_bb(self):
        return self.x - 35, self.y - 40, self.x + 35, self.y + 40

   def draw(self):
        self.image.draw(self.x,self.y)
        #draw_rectangle(*self.get_bb())




class middleboss:
   global Type
   global iCount
   global MBHp

   def __init__(self,x, y):
        self.x = x
        self.y = y
        #self.x, self.y = random.randint(0,500), random.randint(800,1500)
        self.startx = self.x
        self.frame = random.randint(0, 5)
        self.dir = -1
        self.randNum = random.randint(10,150)
        middleboss.image = load_image("resource/enemy/중간보스.png")
        self.Type = 1
        self.MBHp = 30

   def Variable(self):
        if(self.Type == 2):
            self.image = load_image("resource/enemy/비행기 폭발 모션.png")
            print("이미지변환 조건 실행")
            return True

        else:
            return False

   def Hp(self):
        self.MBHp -= 1
        print("HP함수 실행 현재 HP : %d", self.MBHp)
        if(self.MBHp <= 0):
            print("비행기 격파")
            self.Type = 2
            return True
        else:
            return False

   def Power(self):
       self.MBHp -= 10
       print("HP함수 실행 현재 HP : %d", self.MBHp)
       if(self.MBHp <= 0):
            print("비행기 격파")
            self.Type = 2




   def update(self):
            if(self.y >= 600):
                self.y += (self.dir * 3)
            else:
                self.y = 599
                #self.x += (self.dir * 1)
                # if(self.x < 245):
                #     self.dir *= -1
                # elif(self.x > 255):
                #     self.dir *= -1











#        if(self.Type == 2):
 #            Enemy.image = load_image("resource/enemy/비행기 폭발 모션.png")



   def get_bb(self):
        return self.x - 35, self.y - 40, self.x + 35, self.y + 40

   def draw(self):
        self.image.draw(self.x,self.y)
        #draw_rectangle(*self.get_bb())






