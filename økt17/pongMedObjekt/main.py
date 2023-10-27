import pygame as py
import gameObjects
from pygame.locals import *
import sys, settings



#initialiserer prosjektet og mækker vindu
py.init()
py.display.set_caption('Long Dong Pong')
gameSurf = py.display.set_mode((settings.window["x"], settings.window["y"]))
clock = py.time.Clock()
running = True


#mækker objekter
player1 = gameObjects.Paddle(1,12,10,gameSurf)
player2 = gameObjects.Paddle(2,12,10,gameSurf)
ball = gameObjects.Ball(600, 400, 10, 5,5)


font = py.font.Font('Dosis/static/Dosis-Bold.ttf', 50)

def drawUI():
    UIlines = [gameObjects.UILines(595, i*80+20, gameSurf) for i in range(80)]
    for line in UIlines:
        line.draw()
    scoreP1 = font.render(str(settings.score["player1"]), True, settings.colors["UI"])
    scoreP2 = font.render(str(settings.score["player2"]), True, settings.colors["UI"])
    p1Rect = scoreP1.get_rect()
    p2Rect = scoreP2.get_rect()
    p1Rect.center = (settings.window["x"] // 2-300, settings.window["y"] // 2)
    p2Rect.center = (settings.window["x"] // 2+300, settings.window["y"] // 2)
    gameSurf.blit(scoreP1, p1Rect)
    gameSurf.blit(scoreP2, p2Rect)

while running:
    gameSurf.fill(settings.colors["background"])



    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            sys.exit()


    ball.update(gameSurf.get_width(), gameSurf.get_height(), [player1, player2])
    drawUI()
    ball.draw(gameSurf)
    player1.update()
    player2.update()
    py.display.update()
    clock.tick(60)