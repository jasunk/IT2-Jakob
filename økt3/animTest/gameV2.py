import pygame as py
import time, sys, random

import pygame.sprite
from pygame.locals import *

py.init()


window_width=900
window_height = 500

FPS = 32
animChange=True
FramePerSec = py.time.Clock()

gameSurf = py.display.set_mode((window_width,window_height))

spriteNumsPlayer = [10, 10, 10, 3, 9,8, 7, 8, 8]
currentSpriteIndex = 0
playerState = ["crouch_idle",0]

cam_x = 0
cam_y = 0

touching_ground = True

player_x = 150
player_y = 150
playerFlip = False
floatiness=0.05
walkSpeed = 5
runAdded=0
runSpeed = 10
jumpSpeed = 50
friction = 2
rolling=False

playerScale = 100
gravity = 9.81 * playerScale/80

hsp=0
vsp=0






class Player(py.sprite.Sprite):

    def __init__(self):
        super().__init__()

        spriteString = ""

        if currentSpriteIndex <10:
            spriteString = "0"+str(currentSpriteIndex)+".png"
        else:
            spriteString=str(currentSpriteIndex)+".png"

        original_image = py.image.load("anims/" + playerState[0] + "/tile0" + spriteString)
        flipped_image = py.transform.flip(original_image, playerFlip, False)
        scaled_image = py.transform.scale(flipped_image, (playerScale, playerScale))

        self.image = scaled_image
        self.rect = self.image.get_rect()
        self.rect.center = (player_x, player_y)

    def move(self,x,y):
        global player_x, player_y
        player_x+=x
        player_y+=y

    def animator(self,state,stateIndex):
        global playerState, currentSpriteIndex, spriteNumsPlayer
        playerState=[state,stateIndex]
        if currentSpriteIndex > spriteNumsPlayer[stateIndex]-1:
            currentSpriteIndex=0


    def update(self):
        global gravity, touching_ground, playerFlip, walkSpeed, runSpeed, jumpSpeed, floatiness, hsp, vsp, friction, runAdded, rolling, playerScale
        playerScale=100
        if rolling and currentSpriteIndex==6:
            rolling=False

        user_input = py.key.get_pressed()
        if not touching_ground:
            gravity+=floatiness
            vsp+=gravity
        else:
            gravity=9.81*playerScale/80

        if user_input[K_RSHIFT]:
            rolling=True
            if playerFlip:
                hsp=-12
            else:
                hsp=12
            self.animator("roll",6)
        elif user_input[K_z]:
            self.animator("punch",5)


        elif user_input[K_LEFT] and not user_input[K_DOWN] and not user_input[K_LSHIFT] and not rolling:
            hsp=-walkSpeed
            self.animator("walk", 8)
            playerFlip=True

        elif user_input[K_LEFT] and user_input[K_DOWN] and not rolling:
            hsp=-runSpeed/3
            self.animator("crouch_walk", 1)
            playerFlip=True

        elif user_input[K_LEFT] and not user_input[K_DOWN] and  user_input[K_LSHIFT] and not rolling:
            if runAdded<5:
                runAdded+=0.1
            hsp=-runSpeed-runAdded
            self.animator("run", 7)
            playerFlip=True

        elif user_input[K_RIGHT] and not user_input[K_DOWN] and not user_input[K_LSHIFT] and not rolling:
            hsp=walkSpeed
            self.animator("walk", 8)
            playerFlip=False

        elif user_input[K_RIGHT] and user_input[K_DOWN] and not rolling:
            hsp=runSpeed/3
            self.animator("crouch_walk", 1)
            playerFlip=False

        elif user_input[K_RIGHT] and not user_input[K_DOWN] and  user_input[K_LSHIFT] and not rolling:
            if runAdded<5:
                runAdded+=0.1
            hsp=runSpeed+runAdded
            self.animator("run", 6)
            playerFlip=False




        elif user_input[K_DOWN] and touching_ground:
            self.animator("crouch_idle",0)
            hsp=0

        elif not rolling and touching_ground:

            if hsp<0:
                hsp+=friction
            if hsp>0:
                hsp-=friction
            if hsp <2 and hsp > -2:
                hsp=0


            self.animator("idle",2)


        if user_input[K_SPACE] and touching_ground:
            vsp-=jumpSpeed
            self.animator("jump",3)
            touching_ground=False

        self.move(hsp,vsp)


    def draw(self):
        gameSurf.blit(self.image, self.rect.center)



while True:
    p = Player()
    p.update()


    if currentSpriteIndex >=(spriteNumsPlayer[playerState[1]]-1):
        currentSpriteIndex=0

    gameSurf.fill((0, 0, 0))


    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()

    FramePerSec.tick(FPS)
    p.draw()
    py.display.update()
    if animChange:
        animChange=False
        currentSpriteIndex += 1
    else:
        animChange=True