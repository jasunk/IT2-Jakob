import random
import pygame as py
from pygame.locals import *
from classes import *
py.init()

from settings import *
from maps import *

flags = DOUBLEBUF | py.HWSURFACE | FULLSCREEN | SCALED
surf = py.display.set_mode((WW, WH),flags, 16)


game = Game()
game.load_level()
p = Player([500,500], 10, 100, game)










bgImg = py.image.load("sprites/topdown_shooter_assets/sMap.png").convert_alpha()
bgImg = py.transform.scale(bgImg, (1155,1155))
py.mouse.set_cursor(py.SYSTEM_CURSOR_CROSSHAIR)

while 1:



    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            exit()



    game.draw_level(surf)








    game.update(surf)
    p.update(surf, py.mouse.get_pos())




    py.display.update()
    py.time.Clock().tick(30)