from pico2d import *

import game_framework
import title_state

from enemy import Enemy
from enemy import Enemy2
from enemy import middleboss
from character import character
from missile import Missile1
from missile import Missile2
from missile import Missile3
from missile import Missile4
from missile import Missile5
from missile import UpMissile
from missile import UpMissile2
from Upgrade import Upgrade1
from Upgrade import Upgrade2
from PowerAttack import PowerAttack1

import start_state
name = "main_state"

stage = None
mop = None
Time = 1
Type = 1
Count = 0
NUM = 0
iTime = 0
Num2 = 0
BossHp = 0
middleHp = 0
middlenum = 0
MTime = 0
MissileType = 1
Check = 1
Kim = 1
minus = 2
AAA = 1
PPP = 1
PP = 1
P = 0


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
    global midbullet
    global Bossbullet
    global Bossbullet2
    global Bossbullet3
    global boss
    global middle
    global upbullet
    global Upgrade
    global Chance
    global bgm
    global missilesound,explosionsound,itemsound
    global Attack

    missilesound = None
    explosionsound = None
    itemsound = None
    bullet = []
    upbullet = []
    Monbullet = []
    midbullet = []
    Bossbullet = []
    Bossbullet2 = []
    Bossbullet3 = []
    Attack = []
    player = character()


    #enemy1 = Enemy()
    # bgm = load_music("resource/stage.mp3")
    # #start_state.bgm.resume()
    # bgm.set_volume(64)
    # bgm.repeat_play()


    mop = [Enemy(100+(75*i), 700) for i in range(6)]
    boss = [Enemy2(250, 1000) for j in range(1)]
    middle = [middleboss(150 + (200 * k),800) for k in range(2)]
    Chance = [Upgrade2(75 - (l * 50),20)for l in range(2)]
    bgm = load_music('resource/stage.mp3')
    Upgrade = [Upgrade1(100+(j * 100), 100+(j * 100)) for j in range(2)]
    bgm.set_volume(64)
    bgm.repeat_play()

    if missilesound ==  None:
        missilesound = load_wav('resource/missile.wav')
        missilesound.set_volume(50)

    if itemsound ==  None:
        itemsound = load_wav('resource/missile up.wav')
        itemsound.set_volume(50)

    if explosionsound ==  None:
        explosionsound = load_wav('resource/explo.wav')
        explosionsound.set_volume(50)



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
   global MissileType
   global missilesound
   global Check
   global Kim
   global minus
   global AAA


   for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN  and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else :
            player.handle_event(event)

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            missilesound.play()
            if(MissileType == 1):
                bullet.append(Missile1(player.x,player.y))
            elif(MissileType == 2):
                bullet.append(UpMissile(player.x, player.y))
            elif(MissileType == 3):
                bullet.append(UpMissile2(player.x, player.y))

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_s):
            # missilesound.play()
            if(Kim == 1):
                if(minus > 0):
                    Attack.append(PowerAttack1(250, 0))
                    Check = 0
                    Kim = 0
                    minus -= 1
                    AAA = 0
            #mop = [Enemy(100+(75*i), 700) for i in range(6)]
            # elif(MissileType == 2):
            #     bullet.append(UpMissile(player.x, player.y))




def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if(left_a > right_b):return False
    if(right_a < left_b):return False
    if(top_a < bottom_b):return False
    if(bottom_a > top_b):return False

    return True



def collide2(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb2()

    if(left_a > right_b):return False
    if(right_a < left_b):return False
    if(top_a < bottom_b):return False
    if(bottom_a > top_b):return False

    return True


def update():
    global mop1, Count, Time, Type, NUM, Num2, BossHp, mop2, mop3,middleHp, middlenum, MTime, MissileType, Check, Kim, Chance, minus, PPP, PP, P
    global bgm, AAA
    player.update()
    stage.update()

    if(Type == 3):
        P += 1
        if(P >= 200):
            P = 0
            if(PPP == 1):
                PPP = 2
            elif(PPP == 2):
                PPP = 3


    Num2 += 3

    if(Num2 >= 360):
        Num2 = 0


    # Count += 1
    #
    # if(Count == 100):
    #     MissileType = 2
    #     Count = 0

    for Up in Upgrade:
        Up.update()
        if(collide(player,Up)):
             Upgrade.remove(Up)
             if(MissileType == 1):
                 MissileType = 2
                 itemsound.play()
             elif(MissileType == 2):
                 MissileType = 3
                 itemsound.play()


    for Chance1 in Chance:
        Chance1.update()
        if(AAA == 0):
            AAA = 1
            Chance.remove(Chance1)

    for Attack1 in Attack:
        Attack1.update()
        if(Attack1.Delete()):
            Attack.remove(Attack1)
            Kim = 1
            #Check = 1

    for bull1 in bullet:
        bull1.update()


    for bull2 in Monbullet:
        bull2.update()
        if(collide(bull2, player)):
            Monbullet.remove(bull2)
            player.Die()




    for bull3 in Bossbullet:
        bull3.update((0+Num2))
        if(collide(bull3, player)):
            Bossbullet.remove(bull3)
            player.Die()

    for bull4 in Bossbullet2:
        bull4.update((120+Num2))
        if(collide(bull4, player)):
            Bossbullet2.remove(bull4)
            player.Die()

    for bull5 in Bossbullet3:
        bull5.update((240+Num2))
        if(collide(bull5, player)):
            Bossbullet3.remove(bull5)
            player.Die()


    # for bull10 in upbullet:
    #     bull10.update()







    for member in bullet :
        overmap = member.Delete()
        if overmap == True :
             bullet.remove(member)



    for member1 in Monbullet :
        overmap1 = member1.MonDelete()
        if overmap1 == True :
             Monbullet.remove(member1)


    for member2 in Bossbullet :
        overmap2 = member2.Delete()
        if overmap2 == True :
             Bossbullet.remove(member2)
        for Attack1 in Attack:
            if(collide2(member2, Attack1)):
                Bossbullet.remove(member2)
                break
            elif(collide(member2, Attack1)):
                if(member2 == None):
                    break
                else:
                    Bossbullet.remove(member2)






    for member3 in Bossbullet2 :
        overmap3 = member3.Delete()
        if overmap3 == True :
             Bossbullet2.remove(member3)
        for Attack1 in Attack:
            if(collide2(member3, Attack1)):
                Bossbullet2.remove(member3)
                break
            elif(collide(member3, Attack1)):
                if(member3 == None):
                    break
                else:
                    Bossbullet2.remove(member3)



    for member4 in Bossbullet3 :
        overmap4 = member4.Delete()
        if overmap4 == True :
             Bossbullet3.remove(member4)
        for Attack1 in Attack:
            if(collide2(member4, Attack1)):
                Bossbullet3.remove(member4)
                break
            if(collide(member4, Attack1)):
                Bossbullet3.remove(member4)
                break


    for member5 in midbullet :
        overmap5 = member5.Delete()
        if overmap5 == True :
             midbullet.remove(member5)


    for mid in midbullet :
        for pla in bullet:
            if(collide(mid, pla)):
                midbullet.remove(mid)
                bullet.remove(pla)


    if(Check == 0):
        Check = 1
        if(Type == 1):
            for mop1 in mop:
                mop1.Power()
                if(mop1.Variable()):
                    print("카운트 시작")
                    MTime += 1
                    if(MTime >= 6):
                        mop.remove(mop1)
                        MTime = 0
                        NUM += 1
                        if(NUM == 6):
                            Type = 2
        elif(Type == 2):
            for mop3 in middle:
                mop3.Power()
                if(mop3.Variable()):
                    MTime += 1
                    if(MTime >= 10):
                        MTime = 0
                        middle.remove(mop3)
        elif(Type == 3):
            for mop2 in boss:
                mop2.Power()
                if(mop2.Variable()):
                    MTime += 1
                    if(MTime >= 50):
                        MTime = 0
                        boss.remove(mop2)


    if(Type == 2):
        for mop3 in middle:
            mop3.update()
            if(mop3.Variable()):
                print("카운트 시작")
                MTime += 1
                if(MTime >= 10):
                    middle.remove(mop3)
                    MTime = 0
                    middlenum += 1
                    if(middlenum == 2):
                        Type = 3
            Time += 1
            if(Time >= 30):
                 print("미사일발사")
                 midbullet.append(Missile4(mop3.x,mop3.y- 50))
                 Time = 1
            for bull4 in bullet:
                if(mop3.Variable() == False):
                    if(collide(mop3,bull4)):
                        explosionsound.play()
                        if(MissileType == 1):
                            if(mop3.Hp()):
                                mop3.Variable()
                        elif(MissileType == 2):
                            mop3.Hp()
                            if(mop3.Hp()):
                                mop3.Variable()
                        elif(MissileType == 3):
                            mop3.Hp()
                            mop3.Hp()
                            if(mop3.Hp()):
                                mop3.Variable()
                        bullet.remove(bull4)
                        print("collision")

    elif(Type == 3):
        print("보스생성")
        for mop2 in boss:
            mop2.update()
            if(mop2.Variable()):
                MTime += 1
                if(MTime >= 7):
                    boss.remove(mop2)
            Time += 1
            if(Time >= 10):
                 print("미사일발사")
                 if(PPP == 1):
                    Bossbullet.append(Missile3(mop2.x,mop2.y- 50))
                    Bossbullet2.append(Missile3(mop2.x,mop2.y- 50))
                    Bossbullet3.append(Missile3(mop2.x,mop2.y- 50))

                 elif(PPP == 2):
                     if(PP == 1):
                        PP = 2
                        Bossbullet.append(Missile5(mop2.x,mop2.y-50))
                        Bossbullet2.append(Missile5(mop2.x+200,mop2.y- 50))
                        Bossbullet3.append(Missile5(mop2.x-200,mop2.y- 50))
                     elif(PP == 2):
                        PP = 1
                        Bossbullet.append(Missile5(mop2.x-100,mop2.y-50))
                        Bossbullet2.append(Missile5(mop2.x+100,mop2.y- 50))
                        #Bossbullet3.append(Missile5(mop2.x-200,mop2.y- 50))
                 elif(PPP == 3):
                     midbullet.append(Missile4(mop2.x,mop2.y- 50))
                     midbullet.append(Missile4(mop2.x-50,mop2.y- 50))
                     midbullet.append(Missile4(mop2.x+50,mop2.y- 50))
                     midbullet.append(Missile4(mop2.x+100,mop2.y- 50))
                     midbullet.append(Missile4(mop2.x-100,mop2.y- 50))
                     midbullet.append(Missile4(mop2.x-150,mop2.y- 50))
                     midbullet.append(Missile4(mop2.x+150,mop2.y- 50))
                     midbullet.append(Missile4(mop2.x-200,mop2.y- 50))
                     midbullet.append(Missile4(mop2.x+200,mop2.y- 50))
                     if(P >= 30):
                         P = 0
                         PPP = 1
                 Time = 1
        for bull3 in bullet:
                if(mop2.Variable() == False):
                    if(collide(mop2,bull3)):
                        explosionsound.play()
                        bullet.remove(bull3)
                        if(MissileType == 1):
                            if(mop2.Hp()):
                                mop2.Variable()
                        elif(MissileType==2):
                             mop2.Hp()
                             if(mop2.Hp()):
                                mop2.Variable()
                        elif(MissileType==3):
                             mop2.Hp()
                             mop2.Hp()
                             if(mop2.Hp()):
                                mop2.Variable()




    elif(Type == 1):
        for mop1 in mop:
            mop1.update()
            if(mop1.Variable()):
                print("카운트 시작")
                MTime += 1
                if(MTime >= 5):
                    mop.remove(mop1)
                    MTime = 0
                    NUM += 1
                    if(NUM == 6):
                        Type = 2
            Time += 1
            if(Time == 50):
                 Monbullet.append(Missile2(mop1.x,mop1.y- 50))
                 Time = 1
            for bull2 in bullet:
                if(mop1.Variable() == False):
                    if(collide(mop1,bull2)):
                        explosionsound.play()
                        if(MissileType == 1):
                            if(mop1.Hp()):
                                mop1.Variable()
                        elif(MissileType == 2):
                            mop1.Hp()
                            if(mop1.Hp()):
                                mop1.Variable()
                        elif(MissileType == 3):
                            mop1.Hp()
                            mop1.Hp()
                            if(mop1.Hp()):
                                mop1.Variable()
                        bullet.remove(bull2)
                        print("collision")


    for bull6 in midbullet:
        bull6.update(player.x, player.y)
        if(collide(bull6, player)):
            midbullet.remove(bull6)
            player.Die()
        for Attack1 in Attack:
            if(collide(bull6, Attack1)):
                midbullet.remove(bull6)
                break
            if(collide2(bull6, Attack1)):
                midbullet.remove(bull6)
                break

    for bull15 in Monbullet:
        for Attack1 in Attack:
            if(collide(bull15, Attack1)):
                Monbullet.remove(bull15)
                break
            if(collide2(bull15, Attack1)):
                Monbullet.remove(bull15)
                break

    delay(0.02)

def draw():
    global  mop1
    clear_canvas()
    stage.draw()
    # grass.draw()

    for Chance1 in Chance:
        Chance1.draw()

    for Attack1 in Attack:
        Attack1.draw()

    for mop1 in mop:
          mop1.draw()

    for mop2 in boss:
          mop2.draw()

    for mop3 in middle:
          mop3.draw()

    for bull1 in bullet:
          bull1.draw()

    # for bull10 in upbullet:
    #       bull10.draw()

    for bull2 in Monbullet:
          bull2.draw()


    for bull3 in Bossbullet:
          bull3.draw()

    for bull4 in Bossbullet2:
          bull4.draw()

    for bull5 in Bossbullet3:
          bull5.draw()



    for bull6 in midbullet:
          bull6.draw()


    for Up in Upgrade:
        Up.draw()
    player.draw()

    update_canvas()



