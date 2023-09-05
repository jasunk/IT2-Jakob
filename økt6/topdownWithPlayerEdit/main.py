import pygame as py
from pygame.locals import *
import sys, time, random

py.init()

FPS = 8

FramePerSec = py.time.Clock()
dir = "down"
WINWIDTH = 500
WINHEIGHT = 500
active_costume=0
currentSprite=0
win = py.display.set_mode((WINWIDTH,WINHEIGHT))

animDir = {
    "down":["00","01", "02", "03"],
    "left":["04", "05", "06", "07"],
    "right":["08","09","10","11"],
    "up":["12","13","14","15"]

}

class Player(py.sprite.Sprite):
    def __init__(self, x, y, hp, speed):

        super().__init__()
        self.image = py.image.load(f"sprites/var{active_costume}/tile0{animDir[dir][currentSprite]}.png")
        self.rect = self.image.get_rect()
        self.hp = hp
        self.speed = speed
        self.pos = (x,y)

    def draw(self):
        win.blit(self.image,self.pos)
    def move(self):
        global dir
        pressedKeys = py.key.get_pressed()

        if pressedKeys[K_UP]:
            dir = "up"
        if pressedKeys[K_DOWN]:
            dir = "down"
        if pressedKeys[K_LEFT]:
            dir = "left"
        if pressedKeys[K_RIGHT]:
            dir = "right"
        if pressedKeys[K_SPACE]:
            active_costume+=1



running=True

while running:
    player = Player(250,250,50,3)
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()

    win.fill((0,0,0))
    player.move()
    player.draw()
    py.display.update()
    FramePerSec.tick(FPS)
    if currentSprite<3:
        currentSprite+=1
    else:
        currentSprite=0