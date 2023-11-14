import pygame as py
from pygame.locals import *
import classes, settings, random, cProfile
py.init()

clock=py.time.Clock()
mann = classes.mann
enemy1 = classes.pikk

flags = DOUBLEBUF | py.HWSURFACE | FULLSCREEN
py.event.set_allowed([QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEMOTION])

gameSurf = py.display.set_mode((settings.WW,settings.WH), flags, 16 )

enemy1.yourTurn=False


bakgrunn = classes.Background()
b1 = classes.Button("Heisann", [200, 200], [200, 50])
gameplay = True
settingsPage = False
def gameLoop():
    while gameplay and not settingsPage:

        if not settings.background: gameSurf.fill(settings.colors["BG"])

        for e in py.event.get():
            if e.type == QUIT:
                py.quit()
                exit()
            if e.type == MOUSEMOTION and settings.respondToMouse:
                if settings.background: bakgrunn.movePic(py.mouse.get_pos())




            if e.type == KEYDOWN:
                if e.unicode == "s":
                    mann.takeDamage(5,0,2)
                if e.unicode == "w":
                    enemy1.takeDamage(5,0,2)
                if e.unicode=="z":
                    mann.spriteHandler = classes.SpriteHandler(1, True)
                if e.unicode=="x":
                    mann.spriteHandler = classes.SpriteHandler(2, True)
                if e.unicode=="c":
                    mann.spriteHandler = classes.SpriteHandler(3, True)
                if e.unicode=="v":
                    enemy1.spriteHandler = classes.SpriteHandler(1)
                if e.unicode=="b":
                    enemy1.spriteHandler = classes.SpriteHandler(2)
                if e.unicode=="n":
                    enemy1.spriteHandler = classes.SpriteHandler(3)

                match e.unicode:
                    case "1":
                        mann.useAbility(0)
                    case "2":
                        mann.useAbility(1)
                    case "3":
                        mann.useAbility(2)
                    case "4":
                        mann.useAbility(3)

        if settings.background: bakgrunn.update(gameSurf)
        mann.update(gameSurf, py.mouse.get_pos())
        enemy1.update(gameSurf, py.mouse.get_pos())
        py.display.update()
        clock.tick(settings.FPS)
    while settingsPage:


        #b1.update(gameSurf, py.mouse.get_pos())
        py.display.update()
        clock.tick(settings.FPS)


cProfile.run("gameLoop()")
