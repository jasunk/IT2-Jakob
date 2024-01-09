import pygame as py
from pygame.locals import *
from classes import *
py.init()

from settings import *

surf = py.display.set_mode((WW, WH))

p = Player([500,500], 10, 100)
gun = Gun(p, 10, 10)


while 1:
    surf.fill("gray")


    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            exit()


    p.update(surf, py.mouse.get_pos())
    gun.update(surf, py.mouse.get_pos())
    py.display.update()
    py.time.Clock().tick(30)