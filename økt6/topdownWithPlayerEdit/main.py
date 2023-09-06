import pygame as py
from pygame.locals import *
import sys, time, random

py.init()

FPS = 24
shouldChangeSprite = 0
changeCap =3

FramePerSec = py.time.Clock()
dir = "down"
WINWIDTH = 500
WINHEIGHT = 500
active_costume=0
totalCost = 2
currentSprite=0
player_x=150
player_y=150
cam_x = 0
cam_y=0
win = py.display.set_mode((WINWIDTH,WINHEIGHT))


animDir = {
    "down":["00","01", "02", "03"],
    "left":["04", "05", "06", "07"],
    "right":["08","09","10","11"],
    "up":["12","13","14","15"]

}

class BG(py.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = py.transform.scale(py.image.load("sprites/ph.jpeg"),(1100,800))
        self.rect = self.image.get_rect()

    def draw(self, win):
        win.blit(self.image,(-200+cam_x,-200+cam_y))
class Object():
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.heigth=height
        self.color = color
        self.rect = (x+cam_x,y+cam_y,width,height)
    def draw(self,win):
        py.draw.rect(win, self.color, self.rect)
class Player(py.sprite.Sprite):
    def __init__(self, hp, speed):

        super().__init__()
        self.image = py.image.load(f"sprites/var{active_costume}/tile0{animDir[dir][currentSprite]}.png")
        self.rect = self.image.get_rect()
        self.hp = hp
        self.speed = speed

        self.pos = (player_x,player_y)


    def draw(self):

        win.blit(self.image,(240,240))

    def move(self):
        global dir, active_costume, cam_x, cam_y, shouldChangeSprite, changeCap
        pressedKeys = py.key.get_pressed()

        if pressedKeys[K_LSHIFT]:
            self.speed=10
            changeCap=2
        else:
            self.speed=5
            changeCap=3
        if pressedKeys[K_UP]:
            dir = "up"
            cam_y+=self.speed

        if pressedKeys[K_DOWN]:
            dir = "down"
            cam_y-=self.speed



        if pressedKeys[K_LEFT]:
            dir = "left"
            cam_x+=self.speed
        if pressedKeys[K_RIGHT]:
            dir = "right"
            cam_x-=self.speed
        if not (pressedKeys[K_UP] or pressedKeys[K_DOWN] or pressedKeys[K_LEFT] or pressedKeys[K_RIGHT]):
            shouldChangeSprite=0

class Button():
    def __init__(self, x, y, width, height, color, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.value = value

    def draw(self, win):

        py.draw.rect(win, self.color, self.rect)

running=True
inGame=True
while running:
    while not inGame:
        pass

    else:
        obj1 = Object(150,200,20,20,(255,0,0))
        bDown = Button(450,350,25,25,(155,0,0),-1)
        bUp = Button(450,300,25,25,(0,155,0),1)
        buttons = [bDown,bUp]
        objects = [obj1]

        bg=BG()

        player = Player(50,6)
        mouse = py.mouse.get_pos()


        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                for button in buttons:

                    if button.x<mouse[0]<button.x+button.width and button.y<mouse[1]<button.y+button.height:
                        if totalCost-totalCost<=(active_costume+button.value)<=totalCost-1:
                            active_costume += button.value




        win.fill((0,0,0))
        bg.draw(win)

        obj1.draw(win)
        player.move()
        player.draw()
        #for object in objects:
        #   if cam_x + object.x < 0 < (cam_x + object.width) and cam_y < player_y < (cam_y + object.heigth):
        #       print("Ye")

        bDown.draw(win)
        bUp.draw(win)

        py.display.update()
        FramePerSec.tick(FPS)

        if shouldChangeSprite==changeCap:
            shouldChangeSprite=0
            if currentSprite<3:
                currentSprite+=1
            else:
                currentSprite=0
        else:
            shouldChangeSprite+=1