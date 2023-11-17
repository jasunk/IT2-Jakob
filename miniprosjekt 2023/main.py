import pygame as py
from pygame.locals import *
import classes, settings, random, cProfile, random_gen, saves
py.init()

clock=py.time.Clock()
player = random_gen.createRandom(True)
enemy = random_gen.createRandom()
player.refreshTarget(enemy)
enemy.refreshTarget(player)

newCharTimer = 10
has_updated_timer = False
def newChars(victor):
    global player, enemy, newCharTimer, has_updated_timer
    newCharTimer-=0.1
    if newCharTimer<=0:

        saves.save_1["enemy"]["lvl"]+= random.randint(1,2)
        saves.save_1["player"]["lvl"]+= random.randint(1,3)
        if victor:
            player = random_gen.semiRandom(player, True)
            enemy = random_gen.createRandom()
        else:
            enemy = random_gen.semiRandom(enemy, False)
            player = random_gen.createRandom(True)
        player.refreshTarget(enemy)
        enemy.refreshTarget(player)
        print("New characters made")
        has_updated_timer=False

flags = DOUBLEBUF | py.HWSURFACE | FULLSCREEN
py.event.set_allowed([QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEMOTION])

gameSurf = py.display.set_mode((settings.WW,settings.WH), flags, 16 )

enemy.yourTurn=False


bakgrunn = classes.Background()
b1 = classes.Button("Heisann", [200, 200], [200, 50])
gameplay = True
settingsPage = False

def gameLoop():
    while gameplay and not settingsPage:
        global newCharTimer, has_updated_timer
        player.refreshTarget(enemy)
        enemy.refreshTarget(player)
        print(player.name)


        if not settings.background: gameSurf.fill(settings.colors["BG"])

        for e in py.event.get():
            if e.type == QUIT:
                py.quit()
                exit()
            if e.type == MOUSEMOTION and settings.respondToMouse:
                if settings.background: bakgrunn.movePic(py.mouse.get_pos())


        if player.currentHealth<=0:
            print("Du tapte mann")
            if not has_updated_timer:
                newCharTimer=10
                has_updated_timer=True
            newChars(False)
        if enemy.currentHealth<=0:
            print("EZ DUB")
            if not has_updated_timer:
                newCharTimer=10
                has_updated_timer=True
            newChars(True)
        print(newCharTimer)


        if settings.background: bakgrunn.update(gameSurf)
        player.update(gameSurf, py.mouse.get_pos())
        enemy.update(gameSurf, py.mouse.get_pos())
        py.display.update()
        clock.tick(settings.FPS)
        print(saves.save_1["player"]["lvl"])
    while settingsPage:


        #b1.update(gameSurf, py.mouse.get_pos())
        py.display.update()
        clock.tick(settings.FPS)



cProfile.run("gameLoop()")
