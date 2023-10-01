import pygame as py
import camera

class Thing(py.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type

    def draw(self, surf,camera):
        self.image = py.image.load("sprites/blomst.png")
        surf.blit(self.image, (300+camera.getPos()[0],300+camera.getPos()[1]))
    def interract(self):
        mixer = py.mixer
        mixer.init()
        mixer.Channel(1).play(py.mixer.Sound("sounds/house/Can_clink_4.wav"))
        print("interracted with blomst")

class Level():
    def __init__(self):
        self.things = [Thing(1) for x in range(5)]
    def draw(self,plane, camera):
        for thing in self.things:
            thing.draw(plane, camera)