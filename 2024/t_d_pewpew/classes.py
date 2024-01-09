import pygame as py
from pygame.locals import *
import math
from settings import *




class AnimationSet():

    def splitSheet(self, sheet, imgSize, split, index, flip = 0):
        xSize = imgSize[0]/split[0]
        ySize = imgSize[1]/split[1]
        img = py.Surface((xSize,ySize), py.SRCALPHA)

        sheet = py.image.load(sheet)
        img.blit(sheet, (0,0), (xSize*(index[0]), ySize*(index[1]),xSize*(index[0]+1), ySize*(index[1]+1)))

        img = py.transform.scale(img,(xSize*1.5,ySize*1.5))
        img = py.transform.flip(img, flip, 0)
        return img
    def returnSingleSprite(self, img, size=None):
        image = py.image.load(img)
        if size:
            image = py.transform.scale(image,[size])
        return image

    def returnArr(self, img, imgSize, split, flip = 0):
        return [self.splitSheet(img,imgSize, [split, 1], [i,0], flip) for i in range(0,split-1)]



class KinematicBody():
    def __init__(self, pos, speed, health, friction = 1, canBeHit=True,):
        self.spriteList = [py.image.load("sprites/topdown_shooter_assets/sBullet.png")]
        self.frameForFrameShift = 0
        self.frame = 0
        self.pos = pos
        self.vel = [0,0]
        self.speed = speed
        self.friction = friction
        self.hp = health


    def addVelocity(self,velArray):
        self.vel[0] += velArray[0]
        self.vel[1] += velArray[1]

    def setVelocity(self,velArray):
        self.vel[0], self.vel[1] = velArray[0], velArray[1]

    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.vel[0] *= self.friction
        self.vel[1] *= self.friction



    def draw(self, surf):
        self.move()
        if self.frame>len(self.spriteList)-1:
            self.frame=0
        surf.blit(self.spriteList[self.frame], (self.pos[0], self.pos[1]))
        if self.frameForFrameShift>=1:
            self.frameForFrameShift=0
            if self.frame < len(self.spriteList)-1:
                self.frame+=1
            else:
                self.frame=0
        else:
            self.frameForFrameShift+=1

class Player(KinematicBody):

    def __init__(self, pos, speed, health):
        animSet = AnimationSet()

        self.animations = {
            "idleRight":animSet.returnArr("sprites/topdown_shooter_assets/sPlayerIdle_strip4.png",[160,40], 4),
            "idleLeft":animSet.returnArr("sprites/topdown_shooter_assets/sPlayerIdle_strip4.png",[160,40], 4, 1),
            "runRight":animSet.returnArr("sprites/topdown_shooter_assets/sPlayerRun_strip7.png",[280,40], 7),
            "runLeft":animSet.returnArr("sprites/topdown_shooter_assets/sPlayerRun_strip7.png",[280,40], 7, 1)
        }

        super().__init__(pos, speed, health, 0.7)
        self.dir = "Right"
        self.spriteList = self.animations["run"+self.dir]



    def input(self, mousePos):
        keystrokes = py.key.get_pressed()

        diagonalSpeed = math.sqrt((self.speed**2 + self.speed**2)/2)

        if keystrokes[K_w]:
            super().setVelocity([0,-self.speed])
        if keystrokes[K_s]:
            super().setVelocity([0,self.speed])
        if keystrokes[K_a]:
            super().setVelocity([-self.speed,0])
        if keystrokes[K_d]:
            super().setVelocity([self.speed,0])

        if keystrokes[K_w] and keystrokes[K_d]:
            super().setVelocity([diagonalSpeed,-diagonalSpeed])
        if keystrokes[K_w] and keystrokes[K_a]:
            super().setVelocity([-diagonalSpeed,-diagonalSpeed])
        if keystrokes[K_s] and keystrokes[K_a]:
            super().setVelocity([-diagonalSpeed,diagonalSpeed])
        if keystrokes[K_s] and keystrokes[K_d]:
            super().setVelocity([diagonalSpeed,diagonalSpeed])

        if not (keystrokes[K_w] or keystrokes[K_s] or keystrokes[K_a] or keystrokes[K_d]):
            moving = False
        else:
            moving = True

        if mousePos[0]<self.pos[0]:
            self.dir="Left"
        elif mousePos[0]>self.pos[0]:
            self.dir="Right"

        if moving:
            self.spriteList = self.animations["run"+self.dir]
        else:
            self.spriteList = self.animations["idle" + self.dir]

    def update(self, surf, mousePos):
        self.input(mousePos)
        super().draw(surf)

class Gun:
    def __init__(self, parent, damage, recoil):
        self.img = py.image.load("sprites/topdown_shooter_assets/sGun.png")
        self.dmg = damage
        self.recoil = recoil
        self.parent = parent
        self.offset = [50, 25]
        self.smoothing_factor = [0.5,0.5]
        self.currentPos = [self.parent.pos[0], self.parent.pos[1]]
        self.rotation = 0
        self.dy=10
        self.bullets = []

    def positionSelf(self):
        target_pos = [0, 0]

        if self.parent.dir == "Left":
            target_pos[0] = self.parent.pos[0] - self.offset[0]+40
        elif self.parent.dir == "Right":
            target_pos[0] = self.parent.pos[0] + self.offset[0]+10


        target_pos[1] = self.parent.pos[1] + self.offset[1] + self.dy/10

        # Smoothly update the gun position
        self.currentPos[0] += (target_pos[0] - self.currentPos[0]) * self.smoothing_factor[0]
        self.currentPos[1] += (target_pos[1] - self.currentPos[1]) * self.smoothing_factor[1]

    def update_rotation(self, mouse_pos):
        self.dx = mouse_pos[0] - self.currentPos[0]
        self.dy = mouse_pos[1] - self.currentPos[1]

        self.rotation = math.degrees(math.atan2(self.dy, self.dx))+180

    def draw(self, surf):
        rotated_img = py.transform.rotate(self.img, -self.rotation)
        rect = rotated_img.get_rect(center=(self.currentPos[0], self.currentPos[1]))

        surf.blit(rotated_img, rect.topleft)


    def shoot(self, mouse_pos):
        vector = [mouse_pos[0]-self.currentPos[0], mouse_pos[1]-self.currentPos[1]]
        if py.mouse.get_pressed()[0]:
            lengdeDia = math.sqrt((vector[0]**2 + vector[1]**2)/2)

            self.bullets.append(Bullet(self.currentPos,[vector[0]/(lengdeDia/4), vector[1]/(lengdeDia/4)],self.dmg ))

    def update(self, surf, mouse_pos):
        self.shoot(mouse_pos)
        self.positionSelf()
        self.update_rotation(mouse_pos)
        self.draw(surf)

        for bullet in self.bullets:

            bullet.updateBullet(surf)




class Bullet:
    def __init__(self, pos, vel, dmg):
        self.pos = pos
        self.vel = vel
        self.dmg = dmg