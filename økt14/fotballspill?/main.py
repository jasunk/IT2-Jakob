import pygame as py
from pygame.locals import *
import players, ball
import sys, random, time

py.init()

FPS = 60
clock = py.time.Clock()

WW = 800
WH = 400

gameSurf = py.display.set_mode((WW,WH))

#(team,active,number,pace,shotpower,accuracy,tackles,x,y,hasPosession)
p1 = players.Player(1, True, 12, 80, 80, 40, 40, 200, 200, True)
ball1 = ball.Ball(300,200,0.9)
activePVel = [0,0]
while True:

    gameSurf.fill("green")
    clock.tick(FPS)

    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            sys.exit()
        if e.type == KEYDOWN:

            if e.unicode == "a":
                activePVel[0] = -1
            if e.unicode == "d":
                activePVel[0] = 1
            if e.unicode == "w":
                activePVel[1] = -1
            if e.unicode == "s":
                activePVel[1] = 1
            if e.unicode =="e":
                ball1.giveVelocity(1,1)
        if e.type == KEYUP:
            if e.unicode == "a" and activePVel[0] !=1:
                activePVel[0] = 0
            if e.unicode == "d" and activePVel[0] !=-1:
                activePVel[0] = 0
            if e.unicode == "w" and activePVel[1] !=1:
                activePVel[1] = 0
            if e.unicode == "s" and activePVel[1] !=-1:
                activePVel[1] = 0


    ball1.slide()
    ball1.draw(gameSurf)
    p1.control(activePVel[0],activePVel[1])
    p1.draw(gameSurf)
    py.display.update()