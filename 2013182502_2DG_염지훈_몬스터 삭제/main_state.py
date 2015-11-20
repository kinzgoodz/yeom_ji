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

class Stage:
    def __init__(self):
        self.stageBackground = load_image('resource/stagebackground.png')
    def draw(self):
        self.stageBackground.draw(250,350)


def enter():
    global stage,mop
    stage = Stage()
    global player
    global enemy1
    global bullet
    player = character()
    enemy1 = Enemy()
    mop = [Enemy() for i in range(10)]
    bullet = Missile1(0,0)
def exit():
    pass
    # global player,grass,enemy1
    del(player)
    # del(grass)
    # del(enemy1)
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



def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if(left_a > right_b):return False
    if(right_a < left_b):return False
    if(top_a < bottom_b):return False
    if(bottom_a > top_b):return False

    return True

def update():
    global  mop1
    player.update()
    enemy1.update()
    bullet.update()
    for mop1 in mop:
        mop1.update()
        if collide(mop1,player):
            mop.remove(mop1)
            print("collision")

    delay(0.03)
def draw():
    global  mop1
    clear_canvas()
    stage.draw()
    # grass.draw()
    enemy1.draw()
    for mop1 in mop:
          mop1.draw()
    player.draw()
    update_canvas()



