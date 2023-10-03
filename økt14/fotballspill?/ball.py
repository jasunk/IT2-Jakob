import pygame as py
import math

class Ball(py.sprite.Sprite):
    def __init__(self, initX,initY,Friction):
        super().__init__()
        self.pos = [initX, initY]
        self.speedVector = [0,0]
        self.friction = 1-Friction

    def slide(self):

        if self.speedVector[0]>0:
            self.speedVector[0]-=self.friction
        if self.speedVector[0]<0:
            self.speedVector[0]+=self.friction
        if self.speedVector[1]>0:
            self.speedVector[1]-=self.friction
        if self.speedVector[1]<0:
            self.speedVector[1]+=self.friction

    def giveVelocity(self,x,y):
        self.speedVector[0] += x
        self.speedVector[1] += y
        self.pos += self.speedVector


    def draw(self,plane):

        image = py.image.load("sprites/red.png")
        plane.blit(image,(self.pos[0]+self.speedVector[0],self.pos[1]))

