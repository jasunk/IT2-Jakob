import random
import pygame as py
from pygame.locals import *
from classes import *
import cProfile
from settings import *


py.init()
flags = DOUBLEBUF | HWSURFACE | FULLSCREEN | SCALED
surf = py.display.set_mode((WW, WH),flags, 16)


game = Game()
game.load_level()
game.playerRef = Player([500,500], 10, 1000, game)




c = Crosshair()




bgImg = py.image.load("sprites/topdown_shooter_assets/sMap.png").convert_alpha()
bgImg = py.transform.scale(bgImg, (1155,1155))
py.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))



while 1:



    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            exit()

    match game.state:
        case "game": gameLoop(surf, game, py.mouse.get_pos())
        case "intro": introScreen(surf, game, py.mouse.get_pos())
        case "gameOver": gameOverScreen(surf, game, py.mouse.get_pos())

    c.update(surf, py.mouse.get_pos())
    py.display.update()
    py.time.Clock().tick(FPS)
