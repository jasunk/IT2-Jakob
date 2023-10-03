import pygame as py
import random
class Player(py.sprite.Sprite):
    def __init__(self, team, active, number, pace, shotpower, accuracy, tackles, x,y, hasPosession):
        super().__init__()
        self.team = team
        self.active = active
        self.number = number
        self.pace = pace
        self.shotpower = shotpower
        self.accuracy = accuracy
        self.tackles = tackles
        self.pos = [x,y]
        self.hasPosession = hasPosession


    def runRandom(self):
        pass

    def control(self,moveX, moveY):
        if self.active:
            self.pos[0]+=moveX*(self.pace/75)
            self.pos[1]+=moveY*(self.pace/75)

    def getShot(self, initVelocity):
        power = shotpower + random.randint(0,10)*random.randint(-1,1)

    def tackle(self):
        if (random.randint(0,100)+self.tackles) >50:
            self.hasPosession = True
            return True
        self.hasPosession = False
        return False

    def draw(self, plane):
        if self.team == 1:
            image = py.image.load("sprites/red.png")
        if self.team == 2:
            image = py.image.load("sprites/blue.png")
        plane.blit(image, (self.pos[0], self.pos[1]))
