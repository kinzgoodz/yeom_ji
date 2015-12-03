import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image,bgm

    open_canvas(500,700)
    image = load_image('resource/Game_logo.png')
    bgm = load_music('resource/logo.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    global image,bgm
    del(image)

    close_canvas()


def update():
   global logo_time,bgm
   if(logo_time > 1.0):
       logo_time = 0
       # bgm.stop()
       game_framework.push_state(title_state)

   delay(0.01)
   logo_time +=0.01



def draw():
    global image
    clear_canvas()
    image.draw(250,350)
    update_canvas()



def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




