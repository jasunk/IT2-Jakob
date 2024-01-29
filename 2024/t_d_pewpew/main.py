import random
import pygame as py
from pygame.locals import *
from classes import *
import cProfile
from settings import *

py.init()
flags = DOUBLEBUF| HWACCEL  | HWSURFACE | FULLSCREEN | SCALED
surf = py.display.set_mode((WW, WH),flags, 16)

game = Game()

c = Crosshair()

py.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

while 1:



    game.update(surf, py.mouse.get_pos(), py.event.get())

    c.update(surf, py.mouse.get_pos())
    py.display.update()
    py.time.Clock().tick(FPS)
