import pygame as py
from pygame.locals import *
import classes, settings, random, cProfile, random_gen, saves, saves_V2
py.init()

#definerer noen startverdier
clock = py.time.Clock()
player = random_gen.createRandom(True)
enemy = random_gen.createRandom()
player.refreshTarget(enemy)
enemy.refreshTarget(player)

py.mixer.music.load("trackTest.mp3")

py.mixer.music.play(-1)
py.mixer.music.set_volume(0.75)




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
            settings.currentSave["enemy"]["currentXP"]+=random.randint(10,40)
            settings.currentSave["player"]["currentXP"]+=random.randint(50,150)

        #samme men motsatt
        else:
            enemy = random_gen.semiRandom(enemy, False)
            player = random_gen.createRandom(True)
            settings.currentSave["player"]["currentXP"]+=random.randint(10,40)
            settings.currentSave["enemy"]["currentXP"]+=random.randint(50,150)

        saves_V2.updateSave()

        #sjekker om spiller eller fiendes XP er mer enn det som kreves for å levle opp, ez dubs
        if int(saves_V2.loadSave()["player"]["currentXP"])>int(saves_V2.loadSave()["player"]["XPtoLevelUp"]):
            settings.currentSave["player"]["lvl"]+= 1
            settings.currentSave["player"]["XPtoLevelUp"]+=100 + settings.currentSave["player"]["lvl"]*25

        if int(saves_V2.loadSave()["enemy"]["currentXP"])>int(saves_V2.loadSave()["enemy"]["XPtoLevelUp"]):
            settings.currentSave["enemy"]["lvl"]+= 1
            settings.currentSave["enemy"]["XPtoLevelUp"]+=100 + settings.currentSave["enemy"]["lvl"]*25

        saves_V2.updateSave()

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
startButton = classes.Button("START", [settings.WW/2, settings.WH/2], 55, 10, "start")
b1 = classes.Button("FPS up", [settings.WW/2, settings.WH/2-100], 20,4, "FPSup")
b2 = classes.Button("FPS down", [settings.WW/2, settings.WH/2-50], 20,4, "FPSdown")
b3 = classes.Button("TOGGLE PARALAXING", [settings.WW/2, settings.WH/2], 20,4, "mousemove")
b4 = classes.Button("TOGGLE BACKGROUND", [settings.WW/2, settings.WH/2+50], 20,4, "bg")
wipe = classes.Button("WIPE SAVE", [settings.WW/2, settings.WH/2+250], 20,4, "wipe")

#toggleSettingsButtons
b5 = classes.Button("BACK", [settings.WW/2, settings.WH/2+150], 20,4, "back")
b6 = classes.Button("Settings", [settings.WW/2, settings.WH/2-350], 20,4, "back")

l1 = classes.Label("GAME SETTINGS", [settings.WW/2, settings.WH/20], 30)
l2 = classes.Label(f"Current FPS:",[settings.WW/2, settings.WH/2-175],20)
l3 = classes.Label(f"(CLOSES GAME, RESTART MANUALLY)",[settings.WW/2, settings.WH/2+300],20)
liveFPS = classes.Label(f"{settings.FPS}",[settings.WW/2, settings.WH/2-150],30)

settingsButtons = [b1, b2, b3, b4, b5, wipe]
settingsLabels = [l1, l2, l3]
gameplay = True
settingsPage = False
introPage = True

shouldDrawBG = 1
FPS = settings.FPS

def gameLoop():
    while gameplay:
        global newCharTimer, has_updated_timer, settingsPage, shouldDrawBG, FPS, introPage

        if introPage:
            gameSurf.blit(py.image.load("sprites/nice.png"),[-45,0])
            startButton.update(gameSurf, py.mouse.get_pos())
            if startButton.inputHandler(py.mouse.get_pos()):
                introPage=False

        if not settingsPage and not introPage:

            player.refreshTarget(enemy)
            enemy.refreshTarget(player)



            if  shouldDrawBG==-1: gameSurf.fill(settings.colors["BG"])


            if shouldDrawBG: bakgrunn.movePic(py.mouse.get_pos())


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



            if shouldDrawBG==1: bakgrunn.update(gameSurf)
            player.update(gameSurf, py.mouse.get_pos())
            enemy.update(gameSurf, py.mouse.get_pos())
            b6.update(gameSurf,py.mouse.get_pos())
            if b6.inputHandler(py.mouse.get_pos()):
                settingsPage = True


        if settingsPage:
            gameSurf.fill((50,50,50))
            liveFPS = classes.Label(f"{FPS}",[settings.WW/2, settings.WH/2-150],30)
            for b in settingsButtons:
                b.update(gameSurf,py.mouse.get_pos())

            for l in settingsLabels:
                l.draw(gameSurf)

            liveFPS.draw(gameSurf)

            if b5.inputHandler(py.mouse.get_pos()):
                settingsPage = False
            if b1.inputHandler(py.mouse.get_pos()):
                FPS+=1
            if b2.inputHandler(py.mouse.get_pos()):
                FPS-=1
            if wipe.inputHandler(py.mouse.get_pos()):
                saves_V2.delete_json_file("save_data.json")
                py.quit()
                exit()


            py.display.update()
            clock.tick(settings.FPS)

        for e in py.event.get():
            if e.type == QUIT:
                py.quit()
                exit()


        py.display.update()
        clock.tick(FPS)
        shouldDrawBG = settings.background
        print(shouldDrawBG, settings.background)








cProfile.run("gameLoop()")
