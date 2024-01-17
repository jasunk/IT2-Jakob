import random

import pygame as py
from pygame.locals import *
import math
from settings import *
from maps import *



class AnimationSet():

    def splitSheet(self, sheet, imgSize, split, index, flip = 0):
        xSize = imgSize[0]/split[0]
        ySize = imgSize[1]/split[1]
        img = py.Surface((xSize,ySize), py.SRCALPHA)

        sheet = py.image.load(sheet)
        img.blit(sheet, (0,0), (xSize*(index[0]), ySize*(index[1]),xSize*(index[0]+1), ySize*(index[1]+1)))


        img = py.transform.flip(img, flip, 0)
        return img
    def returnSingleSprite(self, img, size=None):
        image = py.image.load(img)
        if size:
            image = py.transform.scale(image,[size])
        return image

    def returnArr(self, img, imgSize, split, flip = 0):
        return [self.splitSheet(img,imgSize, [split, 1], [i,0], flip) for i in range(0,split-1)]



class KinematicBody(py.sprite.Sprite):
    def __init__(self, pos, speed, health, game, friction = 1, canBeHit=True, size=1.5):
        super().__init__()
        self.spriteList = [py.image.load("sprites/topdown_shooter_assets/sBullet.png")]
        self.frameForFrameShift = 0
        self.frame = 0
        self.pos = pos
        self.vel = [0,0]
        self.size = size
        self.targetSize = size
        self.hitSize = size*1.3
        self.speed = speed
        self.friction = friction
        self.hp = health
        self.particles = []
        self.bullets = []
        self.alive = True
        self.deathImg = py.image.load("sprites/topdown_shooter_assets/sEnemyDead.png")
        self.deathImg = py.transform.scale(self.deathImg, (self.deathImg.get_rect().width*self.size, self.deathImg.get_rect().height*self.size))
        self.rect = py.rect.Rect(pos[0], pos[1], self.deathImg.get_size()[0], self.deathImg.get_size()[0])
        self.game = game

    def check_collision(self, direction):

        if direction == "x":

            hits = py.sprite.spritecollide(self, self.game.collisionTiles, False)

            if hits:

                if self.vel[0]>0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.vel[0]<0:
                    self.rect.x = hits[0].rect.right



                if isinstance(self, Enemy):
                    self.vel[0]*=-1
                    self.vel[1]*=-1

        if direction == "y":

            hits = py.sprite.spritecollide(self, self.game.collisionTiles, False)
            if hits:
                if self.vel[1]>0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.vel[1]<0:
                    self.rect.y = hits[0].rect.bottom


                if isinstance(self, Enemy):
                    self.vel[0]*=-1
                    self.vel[1]*=-1

    def checkIfExit(self):
        hits = py.sprite.spritecollide(self, self.game.exits, False)

        if hits:

            nextRoom(self.game.currentRoomIndex+1, self)
            self.game.currentRoomIndex+=1
            self.game.load_level()
            self.game.spawnEnemies(self, (2+self.game.currentRoomIndex),[3,7], [15,30], 20, 15 )


        #hits = py.sprite.spritecollide(self, self.game.entrances, False)

        #if hits:
            #nextRoom(self.game.currentRoomIndex-1, self)
            #self.game.currentRoomIndex-=1
            #self.game.load_level()

    def addVelocity(self,velArray):
        self.vel[0] += velArray[0]

        self.vel[1] += velArray[1]


    def setVelocity(self,velArray):
        if abs(self.vel[0])<abs(velArray[0]):
            self.vel[0] = velArray[0]

        if abs(self.vel[1]) < abs(velArray[1]):
            self.vel[1] = velArray[1]


    def move(self):
        self.rect.x += self.vel[0]

        self.check_collision("x")
        self.rect.y += self.vel[1]
        self.check_collision("y")

        if isinstance(self, Player):  self.checkIfExit()
        self.vel[0] *= self.friction
        self.vel[1] *= self.friction

    def particleHandling(self, surf):
        self.particles = [p for p in self.particles if p.lifetime >= 0]
        self.bullets = [p for p in self.bullets if p.lifetime >= 0]
        for p in self.particles:
            p.update(surf)
        for b in self.bullets:
            b.update(surf)

    def hitScaling(self):
        self.size = self.hitSize
        self.vel[0]*=-1
        self.vel[1]*=-1


    def draw(self, surf):
        if self.alive:
            self.move()
        if self.hp <=0:
            self.alive = False


        if self.size > self.targetSize:
            self.size-=0.25

        self.particleHandling(surf)

        if self.frame>len(self.spriteList)-1:
            self.frame=0

        if not self.alive:
            surf.blit(self.deathImg, (self.rect.x, self.rect.y))
        else:
            scaledSprite = py.transform.scale(self.spriteList[self.frame],(self.spriteList[self.frame].get_size()[0]*self.size,self.spriteList[self.frame].get_size()[1]*self.size))
            surf.blit(scaledSprite, (self.rect.x, self.rect.y))



        if self.frameForFrameShift>=int(self.size):
            self.frameForFrameShift=0
            if self.frame < len(self.spriteList)-1:
                self.frame+=1
            else:
                self.frame=0
        else:
            self.frameForFrameShift+=1


class Enemy(KinematicBody):
    def __init__(self, pos, speed, health, damage, seekArea, player,game, size=1.5 ):
        animSet = AnimationSet()

        self.animations = {

            "runRight":animSet.returnArr("sprites/topdown_shooter_assets/sEnemy_strip7.png",[280,40], 7),
            "runLeft":animSet.returnArr("sprites/topdown_shooter_assets/sEnemy_strip7.png",[280,40], 7, 1),
            "dead":animSet.returnArr("sprites/topdown_shooter_assets/sEnemyDead.png", [40,40], 1)
        }
        super().__init__(pos,speed,health,game, 0.8,True,size)
        self.state = "seek"
        self.dmg = damage
        self.circle_radius = seekArea
        self.player = player
        self.dir = "Right"
        self.spriteList = self.animations["run"+self.dir]
        self.changeDir = 10
        self.despawnTimer = 150

    def chaseState(self):
        vector = [self.player.pos[0]-self.pos[0], self.player.pos[1]-self.pos[1]]
        lengdeDia = math.sqrt((vector[0]**2 + vector[1]**2)/2)
        if lengdeDia==0:lengdeDia=1
        self.vel[0] = vector[0]/(lengdeDia/5)
        self.vel[1] = vector[1]/(lengdeDia/5)
    def is_point_inside_circle(self):
        distance = math.sqrt((self.player.rect.x - (self.rect.x+30))**2 + (self.player.rect.y - (self.rect.y+30))**2)
        return distance < self.circle_radius
    def seekState(self):
        if self.changeDir<0:
            self.changeDir=10
            self.vel[0] += random.randint(int(-self.speed*1.5), int(self.speed*1.5))
            self.vel[1] += random.randint(int(-self.speed*1.5), int(self.speed*1.5))
        else:
            self.changeDir-=1

        if self.is_point_inside_circle():
            self.chaseState()
        if (self.vel[0] and self.vel[1]) == 0:
            self.frame=0


    def die(self):
        pass

    def input(self):
        pass
    def update(self, surf):

        if self.alive:self.seekState()
        self.draw(surf)
        if self.vel[0]<0:
            self.dir = "Left"
        else:
            self.dir = "Right"

        if not self.alive:
            self.spriteList = self.animations["dead"]
            self.alive= False
            self.despawnTimer-=1
        self.spriteList = self.animations["run"+self.dir]
        for b in self.player.bullets:
            if (self.rect.x< b.rect.x< self.rect.x+60) and (self.rect.y< b.rect.y< self.rect.y+60) and self.alive:
                self.hitScaling()
                self.hp-=b.dmg
                if b.dmg >=50:
                    b.dmg *= 0.5
                else: b.lifetime=-1
                for i in range(10):
                    size = random.randint(3,8)
                    self.particles.append(Particle([size,size],[self.rect.x+30, self.rect.y+30], [random.randint(-6,6),random.randint(-6,6)],"red",random.randint(10,20) ))



class Player(KinematicBody):

    def __init__(self, pos, speed, health, game):
        animSet = AnimationSet()

        self.animations = {
            "idleRight":animSet.returnArr("sprites/topdown_shooter_assets/sPlayerIdle_strip4.png",[160,40], 4),
            "idleLeft":animSet.returnArr("sprites/topdown_shooter_assets/sPlayerIdle_strip4.png",[160,40], 4, 1),
            "runRight":animSet.returnArr("sprites/topdown_shooter_assets/sPlayerRun_strip7.png",[280,40], 7),
            "runLeft":animSet.returnArr("sprites/topdown_shooter_assets/sPlayerRun_strip7.png",[280,40], 7, 1)
        }

        super().__init__(pos, speed, health, game, 0.7)


        self.dir = "Right"

        self.spriteList = self.animations["run"+self.dir]
        self.dashCooldown = 20
        self.game.spawnEnemies(self, (2+self.game.currentRoomIndex),[3,7], [15,30], 20, 15 )




    def input(self, mousePos):
        keystrokes = py.key.get_pressed()
        usedSpeed = self.speed
        diagonalSpeed = math.sqrt((self.speed**2 + self.speed**2)/2)
        self.dashCooldown-=1
        if keystrokes[K_LSHIFT] and self.dashCooldown<0:
            for i in range(10):
                self.particles.append(Particle([5,5], [self.rect.x, self.rect.y],[random.randrange(-10,10), random.randrange(-10,10)], "gray", 15, 0.7))
            self.dashCooldown=20
            diagonalSpeed *=5
            usedSpeed*=5


        if keystrokes[K_w]:
            super().setVelocity([0,-usedSpeed])
        if keystrokes[K_s]:
            super().setVelocity([0,usedSpeed])
        if keystrokes[K_a]:
            super().setVelocity([-usedSpeed,0])
        if keystrokes[K_d]:
            super().setVelocity([usedSpeed,0])

        if keystrokes[K_w] and keystrokes[K_d]:

            super().setVelocity([diagonalSpeed,-diagonalSpeed])
        if keystrokes[K_w] and keystrokes[K_a]:

            super().setVelocity([-diagonalSpeed,-diagonalSpeed])
        if keystrokes[K_s] and keystrokes[K_a]:

            super().setVelocity([-diagonalSpeed,diagonalSpeed])
        if keystrokes[K_s] and keystrokes[K_d]:

            super().setVelocity([diagonalSpeed,diagonalSpeed])

        if not (keystrokes[K_w] or keystrokes[K_s] or keystrokes[K_a] or keystrokes[K_d]):
            moving = False
        else:
            moving = True

        if mousePos[0]<self.pos[0]:
            self.dir="Left"
        elif mousePos[0]>self.pos[0]:
            self.dir="Right"

        if moving:
            self.spriteList = self.animations["run"+self.dir]
        else:
            self.spriteList = self.animations["idle" + self.dir]

    def playerUI(self, surf):
        headerFont = py.font.Font("sprites/Pixelify_Sans/static/PixelifySans-Bold.ttf")
        _ = py.rect.Rect(1000,0,400,1000)
        py.draw.rect(surf,"pink", _)

    def update(self, surf, mousePos):
        self.input(mousePos)
        self.playerUI(surf)
        super().draw(surf)

class Gun:
    def __init__(self, parent, damage, recoil, cooldownSTD, size, game, knockBack=True):
        self.img = py.image.load("sprites/topdown_shooter_assets/sGun.png")
        self.imgRect = self.img.get_rect()
        self.sizeArr = [size[0], size[1]]
        self.img = py.transform.scale(self.img, (self.imgRect.width*size[0], self.imgRect.height*size[1]))
        self.knockBack = knockBack
        self.size=size[1]
        self.dmg = damage
        self.recoil = recoil
        self.parent = parent
        self.offset = [50, 25]
        self.smoothing_factor = [0.5,0.5]
        self.currentPos = [self.parent.pos[0], self.parent.pos[1]]
        self.rotation = 0
        self.dy=10
        self.bullets = []
        self.cooldown = cooldownSTD
        self.cooldownSTD = cooldownSTD
        self.active= True
        self.game = game

    def positionSelf(self):
        target_pos = [0, 0]

        if self.parent.dir == "Left":
            target_pos[0] = self.parent.rect.x - self.offset[0]+40 +self.size*5
        elif self.parent.dir == "Right":
            target_pos[0] = self.parent.rect.x + self.offset[0]+15+self.size*5


        target_pos[1] = self.parent.rect.y + self.offset[1] + self.dy/10

        # Smoothly update the gun position
        self.currentPos[0] += (target_pos[0] - self.currentPos[0]) * self.smoothing_factor[0]
        self.currentPos[1] += (target_pos[1] - self.currentPos[1]) * self.smoothing_factor[1]

    def update_rotation(self, mouse_pos):
        self.dx = mouse_pos[0] - self.currentPos[0]
        self.dy = mouse_pos[1] - self.currentPos[1]

        self.rotation = math.degrees(math.atan2(self.dy, self.dx))+180

    def draw(self, surf):
        rotated_img = py.transform.rotate(self.img, -self.rotation)
        rect = rotated_img.get_rect(center=(self.currentPos[0], self.currentPos[1]))

        surf.blit(rotated_img, rect.topleft)


    def shoot(self, mouse_pos):
        vector = [mouse_pos[0]-self.currentPos[0], mouse_pos[1]-self.currentPos[1]]
        if (py.key.get_pressed()[K_SPACE] or py.mouse.get_pressed()[0]) and self.cooldown<0:
            self.cooldown=self.cooldownSTD
            lengdeDia = math.sqrt((vector[0]**2 + vector[1]**2)/2)

            self.parent.bullets.append(Bullet(self.currentPos,[vector[0]/(lengdeDia/15), vector[1]/(lengdeDia/15)],self.dmg, self.size, self.game ))
            self.currentPos[0] += vector[0]/(lengdeDia/self.recoil)
            self.currentPos[1] += vector[1]/(lengdeDia/self.recoil)
            if self.knockBack:
                self.parent.addVelocity([(vector[0]*self.recoil/5)/(-lengdeDia/5),(vector[1]*self.recoil/5)/(-lengdeDia/5)])
            for i in range(random.randint(5,14)):
                self.parent.particles.append(Particle([5*self.size,5*self.size],self.currentPos,[(vector[0]/(lengdeDia/10)+random.randint(-7,7)), (vector[1]/(lengdeDia/5))+random.randint(-7,7)], "yellow", 7, 0.65))
                self.parent.particles.append(Particle([4*self.size,4*self.size],self.currentPos,[(vector[0]/(lengdeDia/5)+random.randint(-3,3)), (vector[1]/(lengdeDia/5))+random.randint(-3,3)], "red", 5, 0.8))
                self.parent.particles.append(Particle([5*self.size,5*self.size],self.currentPos,[(vector[0]/(lengdeDia/3)+random.randint(-3,3)), (vector[1]/(lengdeDia/3))+random.randint(-3,3)], "black", 5, 0.8))




    def update(self, surf, mouse_pos):
        if self.active:
            self.shoot(mouse_pos)
            self.positionSelf()
            self.update_rotation(mouse_pos)
            self.draw(surf)
            self.cooldown-=1



class Particle:
    def __init__(self, size, pos, vel, color, lifetime, damping=0.8, img=False):
        self.size = [size[0], size[1]]
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.damping = damping
        self.color = color
        self.lifetime = lifetime
        self.img = img

    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.vel[0] *= self.damping
        self.vel[1] *= self.damping

    def draw(self, surf):
        py.draw.rect(surf, self.color, py.rect.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]))
    def update(self, surf):
        self.move()
        self.draw(surf)
        self.lifetime-=1

class Bullet(py.sprite.Sprite):
    def __init__(self, pos, vel, dmg, size, game):
        super().__init__()
        self.vel = [vel[0], vel[1]]
        self.dmg = dmg
        self.lifetime = 50
        self.img = py.image.load("sprites/topdown_shooter_assets/sBullet.png").convert_alpha()
        self.imgRect = self.img.get_rect()
        self.rect = py.rect.Rect(pos[0], pos[1],self.imgRect.width*size, self.imgRect.height*size, center=pos)
        self.img = py.transform.scale(self.img, (self.imgRect.width*size, self.imgRect.height*size))
        self.game = game

    def wallBounce(self, dir):

        hits = py.sprite.spritecollide(self, self.game.collisionTiles, False)
        if hits:
            self.lifetime=-1
            normal = py.math.Vector2(hits[0].rect.center) - self.rect.center
            normal.normalize_ip()

            # Make sure self.vel is a Vector2
            self.vel = py.math.Vector2(self.vel)

            # Reflect the velocity of the bullet
            self.vel.reflect_ip(normal)



    def update(self, surf):
        self.lifetime-=1

        self.rect.x += self.vel[0]
        self.wallBounce("x")
        self.rect.y += self.vel[1]
        self.wallBounce("y")
        surf.blit(self.img,(self.rect.x, self.rect.y))


class Tiler(py.sprite.Sprite):
    def __init__(self, img, pos):
        super().__init__()
        self.sprite = py.image.load(img).convert()
        self.sprite = py.transform.scale(self.sprite, (WH/10, WH/10))
        self.pos = pos
        self.rect = py.rect.Rect(pos[0]*self.sprite.get_size()[0]-self.sprite.get_size()[0], pos[1]*self.sprite.get_size()[0]-self.sprite.get_size()[0], self.sprite.get_size()[0], self.sprite.get_size()[1])


    def draw(self, surf):
        surf.blit(self.sprite, (self.rect.x, self.rect.y))




class Game:
    def __init__(self):
        self.tiles = []
        self.collisionTiles = py.sprite.LayeredUpdates()
        self.exits = py.sprite.LayeredUpdates()
        self.entrances = py.sprite.LayeredUpdates()
        self.currentRoomIndex = 1
        self.enemies = []


    def load_level(self):
        self.tiles = []
        self.collisionTiles = py.sprite.LayeredUpdates()
        self.exits = py.sprite.LayeredUpdates()
        self.entrances = py.sprite.LayeredUpdates()
        for i in range(0, len(rooms[self.currentRoomIndex]["map"])):
            for j in range(0, len(rooms[self.currentRoomIndex]["map"])):
                if rooms[self.currentRoomIndex]["map"][i][j]==0:
                    self.tiles.append(Tiler("sprites/grass.png",[(j),i]))
                if rooms[self.currentRoomIndex]["map"][i][j]==1:
                    _ = Tiler("sprites/rasse.jpg",[(j),i])
                    self.collisionTiles.add(_)
                    self.tiles.append(_)
                if rooms[self.currentRoomIndex]["map"][i][j]==2:
                    _ = Tiler("sprites/grass.png",[(j),i])
                    self.exits.add(_)
                    self.tiles.append(_)
                if rooms[self.currentRoomIndex]["map"][i][j]==3:
                    _ = Tiler("sprites/grass.png",[(j),i])
                    self.entrances.add(_)
                    self.tiles.append(_)

        print(self.collisionTiles)

    def spawnEnemies(self, p, amount, speedRange, healthRange, damage, bigSpawnChance):
        for i in range(amount):
            if random.randrange(0,100) > bigSpawnChance:
                self.enemies.append(Enemy(
                    [random.randint(100,WH-150),random.randint(100,WH-150)],
                    random.randrange(speedRange[0], speedRange[1]),
                    random.randint(healthRange[0], healthRange[1]),
                    damage,500,p,self))
            else:
                self.enemies.append(Enemy(
                    [random.randint(100,WH-150),random.randint(100,WH-150)],
                    random.randrange(speedRange[0], speedRange[1])/2,
                    random.randint(healthRange[0], healthRange[1])*3,
                    damage*3,500,p,self,3))
    def draw_level(self, surf):
        for t in self.tiles:
            t.draw(surf)

    def update(self, surf):
        self.enemies = [e for e in self.enemies if e.despawnTimer>0]
        for e in self.enemies:
            e.update(surf)

