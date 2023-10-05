import pygame as py
from pygame.locals import *
import settings


spriteSheetImage = py.image.load("sprites/characterSprites.png")
spriteImageScale = [320, 448]
horiz = 5
vert = 7
def splitSheet(sheet, imgSize, split, index, flip = 0):
    xSize = imgSize[0]/split[0]
    ySize = imgSize[1]/split[1]
    img = py.Surface((xSize,ySize))
    img.blit(sheet, (0,0), (xSize*(index[0]), ySize*(index[1]),xSize*(index[0]+1), ySize*(index[1]+1)))
    img = py.transform.scale(img,(xSize*3,ySize*3))
    img = py.transform.flip(img,flip,0)
    return img

playerAnims = {
    "idleDown":[splitSheet(spriteSheetImage,[320,448],[5,7],[i,0]) for i in range(0,5)],
    "walkDown":[splitSheet(spriteSheetImage,[320,448],[5,7],[i,1]) for i in range(0,5)],
    "idleUp":[splitSheet(spriteSheetImage,[320,448],[5,7],[i,2]) for i in range(0,5)],
    "walkUp":[splitSheet(spriteSheetImage,[320,448],[5,7],[i,3]) for i in range(0,5)],
    "idleLeft":[splitSheet(spriteSheetImage,[320,448],[5,7],[i,4],1) for i in range(0,5)],
    "walkLeft":[splitSheet(spriteSheetImage,[320,448],[5,7],[i,5],1) for i in range(0,5)],
    "idleRight":[splitSheet(spriteSheetImage,[320,448],[5,7],[i,4]) for i in range(0,5)],
    "walkRight":[splitSheet(spriteSheetImage,[320,448],[5,7],[i,5]) for i in range(0,5)],
}
py.init()
winWidth, winHeigth = settings.get_window()

clock=py.time.Clock()
gameSurf = py.display.set_mode((winWidth,winHeigth))
frame = 0
while True:
    if frame<4:
        frame+=1
    else:
        frame=0
    gameSurf.blit(playerAnims["idleDown"][frame],(200,200))
    py.display.update()
    clock.tick(8)



class Player(py.sprite.Sprite):
    def __init__(self, cam, plane, speed, playerNr, equipment):
        super().__init__()
        self.cam = cam
        self.plane = plane
        self.image = py.image.load("sprites/test.png")
        self.speed = speed
        self.nr = playerNr
        self.equipment = equipment
        self.runCooldown=3


    def animate(self):
        pass

    def controls(self):
        pressedKeys = py.key.get_pressed()

        if pressedKeys[K_LSHIFT]:
            self.runCooldown-=0.01
            if self.runCooldown>0:
                speedToUse = self.speed*2
            else:
                speedToUse = self.speed
        else:
            speedToUse = self.speed
            self.runCooldown = 3
        if pressedKeys[K_a]:
            self.cam.updatePos(speedToUse, 0)
        if pressedKeys[K_d]:
            self.cam.updatePos(-speedToUse, 0)
        if pressedKeys[K_w]:
            self.cam.updatePos(0, speedToUse)
        if pressedKeys[K_s]:
            self.cam.updatePos(0, -speedToUse)


    def draw(self):
        self.plane.blit(self.image, (settings.get_window()[0]/2-50, settings.get_window()[1]/2-50))

    def update(self):
        self.controls()
        self.animate()
        self.draw()