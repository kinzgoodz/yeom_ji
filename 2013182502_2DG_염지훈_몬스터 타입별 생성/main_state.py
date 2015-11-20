from pico2d import *

import game_framework
import title_state

from enemy import Enemy
from character import character
from missile import Missile1
from missile import Missile2
from missile import Missile3


name = "main_state"

stage = None
mop = None
Time = 1
Type = 1
Count = 1
NUM = 0

class Stage:
    def __init__(self):
        self.x = 250
        self.y = 700
        self.stageBackground = load_image('resource/map.png')
        self.stageBackground2 = load_image('resource/map.png')
        self.stageBackground3 = load_image('resource/map.png')
        self.stageBackground4 = load_image('resource/map.png')

    def update(self):
        self.y -= 5

        if(self.y < 0):
            self.y = 700

        #bullet = [player.bullet1]
    def draw(self):
        self.stageBackground.draw(self.x,self.y)
        self.stageBackground.draw(self.x,self.y+700)
        self.stageBackground.draw(self.x,self.y-700)
        self.stageBackground.draw(self.x,self.y+1400)



def enter():
    global stage,mop,State
    stage = Stage()
    global player
    global enemy1
    global bullet
    global Monbullet

    bullet = []
    Monbullet = []
    player = character()
    enemy1 = Enemy()


    mop = [Enemy() for i in range(4)]


def exit():
    global player
    del(player)

def pause():
    pass

def resume():
    pass





def handle_events():
   events = get_events()
   global player
   for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN  and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else :
            player.handle_event(event)

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            bullet.append(Missile1(player.x,player.y))



def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if(left_a > right_b):return False
    if(right_a < left_b):return False
    if(top_a < bottom_b):return False
    if(bottom_a > top_b):return False

    return True

def update():
    global mop1, Count, Time, Type, NUM
    player.update()
    stage.update()

    for bull1 in bullet:
        bull1.update()

    for bull2 in Monbullet:
        bull2.update()

    for member in bullet :
        overmap = member.Delete()
        if overmap == True :
             bullet.remove(member)



    for member1 in Monbullet :
        overmap1 = member1.MonDelete()
        if overmap1 == True :
             Monbullet.remove(member1)

    if(Type == 2):
            print("중보스 생성")



    elif(Type == 1):
        for mop1 in mop:
            mop1.update()
            Time += 1
            if(Time == 50):
                 print("미사일발사")
                 Monbullet.append(Missile2(mop1.x,mop1.y- 50))
                 Time = 1
            # if(mop1.Variable() == True):
            #     Time += 1
            #     print("타임어택")
            #     if(Time == 10):
            #         mop.remove(mop1)
            #         Type = 1
            for bull2 in bullet:
                if collide(mop1,bull2):
                    Count += 1
                    if(Count == 3):
                        mop1.Variable()
                        NUM += 1
                        #draw()
                        mop.remove(mop1)
                        #Type = 2a
                        Count = 1
                        if(NUM == 4):
                            Type = 2
                        #Type = 2
                    # if(Type == 2):
                    #     mop.remove(mop1)
                    #     Type = 1
                    bullet.remove(bull2)
                    print("collision")


    delay(0.03)
def draw():
    global  mop1
    clear_canvas()
    stage.draw()
    # grass.draw()

    for bull1 in bullet:
          bull1.draw()

    for bull2 in Monbullet:
          bull2.draw()

    for mop1 in mop:
          mop1.draw()
    player.draw()
    update_canvas()



