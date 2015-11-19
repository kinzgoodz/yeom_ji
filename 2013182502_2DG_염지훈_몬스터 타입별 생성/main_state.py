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
        global Count
        Count = 1
        self.stageBackground = load_image('resource/stagebackground.png')

        #bullet = [player.bullet1]
    def draw(self):
        self.stageBackground.draw(250,350)


def enter():
    global stage,mop
    stage = Stage()
    global player
    global enemy1
    global bullet

    bullet = []
    player = character()

    mop = [Enemy(250, 700) for i in range(2)]


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

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            if player.state in (player.RIGHT_IDLE,):
                player.state = player.RIGHT_ATTACK
                player.frameSize = 2
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
    global  mop1
    player.update()

    for bull1 in bullet:
        bull1.update()

    for member in bullet :
        overmap = member.Delete()
        if overmap == True :
             bullet.remove(member)



    for mop1 in mop:
        mop1.update()
        for bull2 in bullet:
            if collide(mop1,bull2):
                mop.remove(mop1)
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

    for mop1 in mop:
          mop1.draw()
    player.draw()
    update_canvas()



