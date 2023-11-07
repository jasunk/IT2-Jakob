import pygame as py
from pygame.locals import *
import classes, settings
py.init()

clock=py.time.Clock()
mann = classes.mann
enemy1 = classes.pikk
gameSurf = py.display.set_mode((settings.WW,settings.WH))


while True:
    gameSurf.fill(settings.colors["BG"])
    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            exit()
        if e.type == KEYDOWN:
            if e.unicode == "s":
                mann.takeDamage(5,0,2)
            if e.unicode == "w":
                enemy1.takeDamage(5,0,2)
            match e.unicode:
                case "1":
                    mann.useAbility(0)
                case "2":
                    mann.useAbility(1)
                case "3":
                    mann.useAbility(2)
                case "4":
                    mann.useAbility(3)
    mann.update(gameSurf)
    enemy1.update(gameSurf)
    py.display.update()
    clock.tick(30)
