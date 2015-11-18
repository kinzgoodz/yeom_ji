from pico2d import *

import game_framework
import main_state
from character import character
from enemy import Enemy

name = "main_state"

player = None
grass = None
font = None
enemy1 = None
mop = None

class Grass:
    def __init__(self):
        self.image = load_image('resource/grass.png')
        self.background = load_image('resource/stage1.png')

    def draw(self):
        self.image.draw(400, 30)
        self.background.draw(400,400)
def enter():
   global player,grass
   global enemy1,mop
   player = character()
   grass = Grass()
   enemy1 = Enemy()
   mop = [Enemy() for i in range(10)]
def exit():
    global player,grass,enemy1
    del(player)
    del(grass)
    del(enemy1)
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
            game_framework.change_state(main_state)
        else :
            player.handle_event(event)

def update():
    global  mop1
    player.update()
    enemy1.update()
    # mop.update()
    for mop1 in mop:
        mop1.update()

    delay(0.05)
def draw():
    global  mop1
    clear_canvas()
    grass.draw()
    enemy1.draw()
    for mop1 in mop:
          mop1.draw()
    player.draw()
    update_canvas()



