import pygame as py
import gameObjects
from pygame.locals import *
import sys
py.init()

gameSurf = py.display.set_mode((1200, 800))

clock = py.time.Clock()

running = True

player1 = gameObjects.Paddle(1,12,10,gameSurf)
player2 = gameObjects.Paddle(2,12,10,gameSurf)
ball = gameObjects.Ball(600, 400, 10, 5,5)

while running:
    gameSurf.fill((0,0,0))

    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            sys.exit()

    ball.update(gameSurf.get_width(), gameSurf.get_height(), [player1, player2])


    ball.draw(gameSurf)
    player1.update()
    player2.update()
    py.display.update()
    clock.tick(60)