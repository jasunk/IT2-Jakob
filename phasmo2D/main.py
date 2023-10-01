import pygame as py
from pygame.locals import *
import time, random, sys
import settings, player, ghost, level, camera

mixer = py.mixer
mixer.init()
py.mixer.set_num_channels(10)
mixer.Channel(0).play(py.mixer.Sound("sounds/ambient/Rain_Medium_2.wav"))

py.init()

clock=py.time.Clock()

winWidth, winHeigth = settings.get_window()

gameSurf = py.display.set_mode((winWidth,winHeigth))

currentGhost = ghost.Ghost(
    10,
    [1,2,3],
    50,
    level.Level(),
    "heii",
    [400,300]
)
cam = camera.Camera([0,0])
currentGhost.newRoamPos()
while True:
    gameSurf.fill("gray")
    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            sys.exit()
        if e.type == KEYDOWN:
            if e.unicode =="w":
                cam.updatePos(0,10)
            if e.unicode=="s":
                cam.updatePos(0,-10)

    currentGhost.room.draw(gameSurf,cam)
    currentGhost.goToNewPos()
    currentGhost.draw(gameSurf,cam)

    py.display.update()
    clock.tick(60)