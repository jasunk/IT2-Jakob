import pygame as py
from pygame.locals import *
import random


class Pung():
    def siHei(self):
        print("Hallais")


class Pikk(Pung):

    def __init__(self):
        super().siHei()

pikk = Pikk()


class Paddle(py.rect.Rect):

    def __init__(self, player, speed, bounceEffect, plane):

        self.player = player
        self.speed = speed
        self.bounceEffect = bounceEffect
        self.plane = plane

        if self.player == 1:
            self.pos = [30,325]
        else:
            self.pos = [1150,325]
        self.rect = py.Rect(self.pos[0], self.pos[1], 20, 150)

    def draw(self):
            if self.pos[1]<-130:
                self.pos[1]=930
            if self.pos[1]>930:
                self.pos[1]=-130

            self.rect = py.Rect(self.pos[0], self.pos[1], 20, 150)

            py.draw.rect(self.plane, "white", self.rect)

    def move(self):
        keystrokes = py.key.get_pressed()
        if self.player == 1:
            if keystrokes[K_w]:
                self.pos[1] -= self.speed
            if keystrokes[K_s]:
                self.pos[1] += self.speed
        if self.player == 2:
            if keystrokes[K_UP]:
                self.pos[1] -= self.speed
            if keystrokes[K_DOWN]:
                self.pos[1] += self.speed


    def update(self):
        self.move()
        self.draw()




class Ball:
    def __init__(self, x, y, radius, velx, vely):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocityX = velx
        self.velocityY = vely

    def move(self):
        self.x += self.velocityX
        self.y += self.velocityY

    def check_collision(self, width, height, paddles):
        if self.x - self.radius <= 0:
            print("Poeng til spiller 2")
            self.x = width / 2 - self.radius / 2
            self.y = height / 2 - self.radius / 2
            self.velocityX = random.randint(4, 7)
            self.velocityY = random.randint(2, 8)
        if self.x + self.radius >= width:
            print("Poeng til spiller 1")
            self.x = width / 2 - self.radius / 2
            self.y = height / 2 - self.radius / 2
            self.velocityX = -random.randint(4, 7)
            self.velocityY = random.randint(2, 8)

        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.velocityY *= -1

        for paddle in paddles:
            if self.y + self.radius >= paddle.rect.top and self.y - self.radius <= paddle.rect.bottom:
                if self.x + self.radius >= paddle.rect.left and self.x - self.radius <= paddle.rect.right:
                    self.velocityX = -self.velocityX  # Reverse x velocity on collision with a paddle

    def update(self, width, height, paddles):
        self.move()
        self.check_collision(width, height, paddles)
        self.velocityX *= 1.0005
        self.velocityY *= 1.0005

    def draw(self, surface):
        py.draw.circle(surface, (255, 255, 255), (self.x, self.y), self.radius)
