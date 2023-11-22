import pygame as py
from pygame.locals import *
import classes, settings, random, cProfile, random_gen, saves
py.init()

#definerer noen startverdier
clock=py.time.Clock()
player = random_gen.createRandom(True)
enemy = random_gen.createRandom()
player.refreshTarget(enemy)
enemy.refreshTarget(player)

#logikk for å lage nye tilfeldige karakterer
newCharTimer = 5
has_updated_timer = False
def newChars(victor):
    global player, enemy, newCharTimer, has_updated_timer
    newCharTimer-=0.1
    if newCharTimer<=0:


        #om spiller vinner, la spiller bare være semi-tilfeldig, forklart i random_gen.py
        #gir også spiller mer xp om den vinner
        if victor:
            player = random_gen.semiRandom(player, True)
            enemy = random_gen.createRandom()
            saves.save_1["enemy"]["currentXP"]+=random.randint(10,40)
            saves.save_1["player"]["currentXP"]+=random.randint(50,150)

        #samme men motsatt
        else:
            enemy = random_gen.semiRandom(enemy, False)
            player = random_gen.createRandom(True)
            saves.save_1["player"]["currentXP"]+=random.randint(10,40)
            saves.save_1["enemy"]["currentXP"]+=random.randint(50,150)


        #sjekker om spiller eller fiendes XP er mer enn det som kreves for å levle opp, ez dubs
        if saves.save_1["player"]["currentXP"]>saves.save_1["player"]["XPtoLevelUp"]:
            saves.save_1["player"]["lvl"]+= 1
            saves.save_1["player"]["XPtoLevelUp"]+=100 + saves.save_1["player"]["lvl"]*25

        if saves.save_1["enemy"]["currentXP"]>saves.save_1["enemy"]["XPtoLevelUp"]:
            saves.save_1["enemy"]["lvl"]+= 1
            saves.save_1["enemy"]["XPtoLevelUp"]+=100 + saves.save_1["enemy"]["lvl"]*25

        #oppdaterer abilities
        player.refreshTarget(enemy)
        enemy.refreshTarget(player)
        print("New characters made")
        has_updated_timer=False

#velger flags for bedre kjøring av program
flags = DOUBLEBUF | py.HWSURFACE | FULLSCREEN
py.event.set_allowed([QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEMOTION])

gameSurf = py.display.set_mode((settings.WW,settings.WH), flags, 16 )

enemy.yourTurn=False


bakgrunn = classes.Background()
#b1 = classes.Button("Heisann", [200, 200], [200, 50])
gameplay = True
settingsPage = False

def gameLoop():
    while gameplay and not settingsPage:
        global newCharTimer, has_updated_timer
        player.refreshTarget(enemy)
        enemy.refreshTarget(player)



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



        if settings.background: bakgrunn.update(gameSurf)
        player.update(gameSurf, py.mouse.get_pos())
        enemy.update(gameSurf, py.mouse.get_pos())
        py.display.update()
        clock.tick(settings.FPS)

    while settingsPage:


        #b1.update(gameSurf, py.mouse.get_pos())
        py.display.update()
        clock.tick(settings.FPS)



cProfile.run("gameLoop()")
