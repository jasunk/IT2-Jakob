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




subMachinegun = Gun(p, 2, 1.2,0, [1, 0.5], game)
pistol =        Gun(p, 18, 10,10, [0.75, 0.75], game)
AR =            Gun(p, 15, 15,5, [1.5,1.5], game)
sniper =        Gun(p, 50, 40,15, [3, 1.5], game)
BOOM =          Gun(p, 100, 140,15, [6, 3], game)




gun = AR
bgImg = py.image.load("sprites/topdown_shooter_assets/sMap.png").convert_alpha()
bgImg = py.transform.scale(bgImg, (1155,1155))
py.mouse.set_cursor(py.SYSTEM_CURSOR_CROSSHAIR)

while 1:



    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            exit()
        if e.type == KEYDOWN:
            match e.unicode:
                case "1": gun=subMachinegun
                case "2": gun=pistol
                case "3": gun=AR
                case "4": gun=sniper
                case "5": gun=BOOM


    game.draw_level(surf)








    game.update(surf)
    p.update(surf, py.mouse.get_pos())

    gun.update(surf, py.mouse.get_pos())



    py.display.update()
    py.time.Clock().tick(30)