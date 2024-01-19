import random


import pygame as py
from pygame.locals import *
import math
from settings import *
from maps import rooms, nextRoom



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
        self.inithp = health
        self.hp = health
        self.particles = []
        self.bullets = []
        self.alive = True
        self.deathImg = py.image.load("sprites/topdown_shooter_assets/sEnemyDead.png")
        self.deathImg = py.transform.scale(self.deathImg, (self.deathImg.get_rect().width*self.size, self.deathImg.get_rect().height*self.size))
        self.rect = py.rect.Rect(pos[0]+leftSidePadding, pos[1], self.deathImg.get_size()[0], self.deathImg.get_size()[0])
        self.game = game
        self.hitsound = py.mixer.Sound("sounds/hit.wav")
        self.dieSound = py.mixer.Sound("sounds/die.wav")

        self.bulletSprites = py.sprite.LayeredUpdates()
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

    def hitScaling(self):
        self.size = self.hitSize
        self.vel[0]*=-1
        self.vel[1]*=-1

    def checkIfExit(self):
        hits = py.sprite.spritecollide(self, self.game.exits, False)

        if hits:

            nextRoom(self.game.currentRoomIndex+1, self)
            self.allocation_points +=1
            self.game.currentRoomIndex+=1
            self.game.load_level()
            self.game.spawnEnemies(self, (2+self.game.currentRoomIndex),[3,7], [15,30], 20, 15 )


        #hits = py.sprite.spritecollide(self, self.game.entrances, False)

        #if hits:
            #nextRoom(self.game.currentRoomIndex-1, self)
            #self.game.currentRoomIndex-=1
            #self.game.load_level()
    def checkIfShot(self):
        hits = py.sprite.spritecollide(self, self.bulletSprites, False)
        if hits and self.alive and hits[0].canHit:
            self.hitsound.play()
            self.hp -= hits[0].dmg
            if hits[0].dmg >=50:
                hits[0].dmg *= 0.8
            else:
                hits[0].canHit = False
                hits[0].lifetime=-1
                hits[0].dmg=0

            for i in range(10):
                size = random.randint(3,8)
                self.particles.append(Particle([size,size],[self.rect.x+30, self.rect.y+30], [random.randint(-6,6),random.randint(-6,6)],"red",random.randint(10,20) ))
            self.hitScaling()
            self.game.display()

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



    def draw(self, surf):



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

        self.checkIfShot()
        if self.alive:
            self.move()
        if self.hp <=0:
            if self.alive:
                self.dieSound.play()
            self.alive = False


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
        self.circle_radius = seekArea/2
        self.player = player
        self.dir = "Right"
        self.spriteList = self.animations["run"+self.dir]
        self.changeDir = 10
        self.despawnTimer = 150
        self.name = random.choice(self.game.randomEnemyNames).upper()
        self.game.display()

    def chaseState(self):
        vector = [self.player.rect.x-self.rect.x, self.player.rect.y-self.rect.y]
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
        self.personalGun = {
            "dmg":3,
            "recoil": 10,
            "fireRate":10,
            "size":[1,1]
        }
        self.allocation_points = 0
        self.spriteList = self.animations["run"+self.dir]
        self.dashCooldown = 20
        self.guns = [Gun(self, self.personalGun["dmg"], self.personalGun["recoil"], self.personalGun["fireRate"], self.personalGun["size"], self.game),Gun(self, 2, 1.2,0, [1, 0.5], self.game), Gun(self, 18, 10,10, [0.75, 0.75], self.game), Gun(self, 15, 15,5, [1.5,1.5], self.game), Gun(self, 50, 40,15, [3, 1.5], self.game), Gun(self, 100, 140,15, [6, 3], self.game)]
        self.activeGunIndex = 0
        self.game.spawnEnemies(self, (2+self.game.currentRoomIndex),[3,7], [15,30], 20, 15 )
        self.dashSound = py.mixer.Sound("sounds/dash.wav")
        self.headerFont = returnFont(64)
        self.UI = py.Surface((400,1000))
        self.playerUI([0,0])




    def input(self, mousePos):
        keystrokes = py.key.get_pressed()
        usedSpeed = self.speed
        diagonalSpeed = math.sqrt((self.speed**2 + self.speed**2)/2)
        self.dashCooldown-=1
        if keystrokes[K_LSHIFT] and self.dashCooldown<0:
            for i in range(10):
                self.particles.append(Particle([5,5], [self.rect.x, self.rect.y],[random.randrange(-10,10), random.randrange(-10,10)], "gray", 15, 0.7))
            self.dashCooldown=20
            py.mixer.Sound.play(self.dashSound)
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


    def update_personal_gun(self):
        if self.personalGun["dmg"]<0: self.personalGun["dmg"]=0
        self.personalGun["size"][0] = self.personalGun["dmg"]/10 + 1
        self.personalGun["size"][1] = self.personalGun["dmg"]/12 + 1

        if self.personalGun["fireRate"]<0: self.personalGun["fireRate"]=0
        if self.personalGun["recoil"]==0: self.personalGun["recoil"]=0.1
        self.guns[0] = Gun(self, self.personalGun["dmg"], self.personalGun["recoil"], self.personalGun["fireRate"], self.personalGun["size"], self.game)
    def gunStatHandler(self,  mousePos):
        damageUp = Button([300, 200], [30, 30], "+", 1, True)
        dmg_label = Label([200, 200], 20, "DAMAGE", "black")
        damageDown = Button([100, 200], [30, 30], "-", -1, True)

        fireRateUp = Button([300, 250], [30, 30], "+", 1, True)
        fireRate_label = Label([200, 250], 20, "FIRERATE", "black")
        fireRateDown = Button([100, 250], [30, 30], "-", -1, True)

        recoilUp = Button([300, 300], [30, 30], "+", 1, True)
        recoildLabel = Label([200, 300], 20, "RECOIL", "black")
        recoilDown = Button([100, 300], [30, 30], "-", -1, True)

        dmg_stat = Label([200, 350],20, f"Damage: {self.personalGun['dmg']}", "black")
        fireRate_stat = Label([200, 370],20, f"Firerate: {self.personalGun['fireRate']}", "black")
        recoil_stat = Label([200, 390],20, f"Recoil: {self.personalGun['recoil']}", "black")

        availible_mods = Label([200, 410],20, f"Modifications available: {self.allocation_points}", "black")

        preset_section_height = 930
        preset_title = Label([200, preset_section_height], 30, "GUN PRESETS", "black")
        smg_preset = Button([50, preset_section_height+40], [90, 30], "SMG",0, True)
        pistol_preset = Button([150, preset_section_height+40], [90, 30], "COCK",0, True)
        AR_preset = Button([250, preset_section_height+40], [90, 30], "AK-69",0, True)
        sniper_preset = Button([350, preset_section_height+40], [90, 30], "WAP",0, True)


        if py.mouse.get_pressed()[0]:

            if self.allocation_points>0:
                if damageUp.is_pressed(mousePos):
                    self.personalGun["dmg"]+=1
                    self.allocation_points-=1
                if recoilDown.is_pressed(mousePos):
                    self.personalGun["recoil"]-=5
                    self.allocation_points-=1
                if fireRateUp.is_pressed(mousePos):
                    self.personalGun["fireRate"]-=0.5
                    self.allocation_points-=1


            if damageDown.is_pressed(mousePos):
                self.personalGun["dmg"]-=1
                self.allocation_points+=1
            if fireRateDown.is_pressed(mousePos):
                self.personalGun["fireRate"]+=2
                self.allocation_points+=2
            if recoilUp.is_pressed(mousePos):
                self.personalGun["recoil"]+=5
                self.allocation_points+=1

            if smg_preset.is_pressed(mousePos):self.activeGunIndex=1
            if pistol_preset.is_pressed(mousePos):self.activeGunIndex=2
            if AR_preset.is_pressed(mousePos):self.activeGunIndex=3
            if sniper_preset.is_pressed(mousePos):self.activeGunIndex=4


        buttons = [damageUp, damageDown, fireRateUp, fireRateDown, recoilUp, recoilDown, smg_preset, pistol_preset, AR_preset, sniper_preset]
        labels = [preset_title, recoildLabel, fireRate_label, dmg_label, dmg_stat, fireRate_stat, recoil_stat, availible_mods]

        for l in labels:
            l.draw(self.UI)

        for b in buttons:
            if b.is_pressed(mousePos): self.update_personal_gun()
            b.update(self.UI, mousePos)

    def playerUI(self, mousePos):
        text = self.headerFont.render("PLAYER", True, "black")
        _ = py.rect.Rect(0,0,400,1000)
        py.draw.rect(self.UI,"pink", _)
        textRect = text.get_rect()
        textRect.center = (200, 100)
        self.UI.blit(text, textRect)
        self.gunStatHandler(mousePos)

    def drawPlayerUI(self, surf, mousePos):
        surf.blit(self.UI,(1400,0))
        if mousePos[0]>1400:

            self.playerUI(mousePos)

    def update(self, surf, mousePos):

        self.guns[self.activeGunIndex].update(surf, mousePos)
        self.input(mousePos)

        super().draw(surf)
        self.drawPlayerUI(surf, mousePos)

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

        if cooldownSTD<3:
            self.shootSound = py.mixer.Sound("sounds/shoot_light.wav")
        elif cooldownSTD<8:
            self.shootSound = py.mixer.Sound("sounds/shoot_def.wav")
        else:
            self.shootSound = py.mixer.Sound("sounds/shoot_deep.wav")

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
        if (py.key.get_pressed()[K_SPACE] or py.mouse.get_pressed()[0]) and self.cooldown<0 and leftSidePadding< mouse_pos[0]<1400:
            py.mixer.Sound.play(self.shootSound)
            self.cooldown=self.cooldownSTD
            lengdeDia = math.sqrt((vector[0]**2 + vector[1]**2)/2)
            _ = Bullet(self.currentPos,[vector[0]/(lengdeDia/15), vector[1]/(lengdeDia/15)],self.dmg, self.size, self.game )

            self.parent.bullets.append(_)
            for e in self.game.enemies:
                e.bulletSprites.add(_)
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
        self.img = py.transform.scale(self.img, (self.img.get_size()[0]*size, self.img.get_size()[1]*size))
        self.imgRect = self.img.get_rect()
        self.rect = py.rect.Rect(pos[0], pos[1],self.imgRect.width, self.imgRect.height, center=pos)

        self.game = game
        self.canHit = True

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
        self.rect = py.rect.Rect(pos[0]*self.sprite.get_size()[0]-self.sprite.get_size()[0]+leftSidePadding, pos[1]*self.sprite.get_size()[0]-self.sprite.get_size()[0], self.sprite.get_size()[0], self.sprite.get_size()[1])


    def draw(self, surf):
        surf.blit(self.sprite, (self.rect.x, self.rect.y))




class Game:
    def __init__(self):
        self.dia = Dialog(["YOOO KA SKJER?", "Tissefant"], "yeye")
        self.tiles = []
        self.collisionTiles = py.sprite.LayeredUpdates()
        self.exits = py.sprite.LayeredUpdates()
        self.entrances = py.sprite.LayeredUpdates()
        self.currentRoomIndex = 1
        self.enemies = []
        self.state = "intro"
        self.randomEnemyNames = ["Rolf", "Frank", "Karl", "Fjomp", "Karsten", "Kornelius", "Albert", "Kurt", "Jens", "Ola", "Skalleknuseren", "Glont", "Sivert"]
        self.enemyIcon = py.image.load("sprites/topdown_shooter_assets/enemyIcon.png").convert_alpha()
        self.map_surf = py.Surface((1400, 1000))
        self.leftDisplay = py.Surface((leftSidePadding,1000))
        self.player = ""




    def display(self):

        leftRect = py.rect.Rect(0,0, 400, 1000)
        py.draw.rect(self.leftDisplay, "pink", leftRect)
        for i in range(len([e for e in self.enemies if e.alive])):
            current_enemy = [e for e in self.enemies if e.alive][i]
            displayRect = py.rect.Rect(50,400+100*i,300,100)
            img = self.enemyIcon
            img_rect = img.get_rect()
            img_rect.x, img_rect.y = 75,435+i*100
            py.draw.rect(self.leftDisplay,"beige", displayRect)
            name = Label([200, 430+100*i],15,f"Name: {current_enemy.name}","black" )
            name.draw(self.leftDisplay)

            hp_bar = py.rect.Rect(120, 450+i*100,(current_enemy.hp/current_enemy.inithp)*200, 20)
            hp = Label([150, 460+i*100],15, f"{current_enemy.hp} / {current_enemy.inithp}", "white")
            py.draw.rect(self.leftDisplay, "red", hp_bar)
            hp.draw(self.leftDisplay)
            self.leftDisplay.blit(img, img_rect)

        self.dia.draw(self.leftDisplay)

    def display_draw(self, surf):
        surf.blit(self.leftDisplay, (0,0))


    def load_level(self):
        self.tiles = []
        self.enemies = []
        self.collisionTiles = py.sprite.LayeredUpdates()
        self.exits = py.sprite.LayeredUpdates()
        self.entrances = py.sprite.LayeredUpdates()
        for i in range(0, len(rooms[self.currentRoomIndex]["map"])):
            for j in range(0, len(rooms[self.currentRoomIndex]["map"])):
                if rooms[self.currentRoomIndex]["map"][i][j]==0:
                    self.tiles.append(Tiler("sprites/grass.png",[(j),i]))
                if rooms[self.currentRoomIndex]["map"][i][j]==1:
                    _ = Tiler("sprites/wall.png",[(j),i])
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
        self.update_map()



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
    def update_map(self):
        for t in self.tiles:
            t.draw(self.map_surf)

    def draw_level(self, surf):

        surf.blit(self.map_surf,(0,0))
    def update(self, surf, player):
        self.draw_level(surf)
        self.enemies = [e for e in self.enemies if e.despawnTimer>0]
        self.display_draw(surf)
        for e in self.enemies:
            e.update(surf)


class Dialog:
    def __init__(self, text, char):
        self.targetText = text
        self.currentText = ""
        self.dialogIndex = 0
        self.char = char
        self.font = returnFont(12)

    def talk(self):
        if len(self.targetText[self.dialogIndex])>0: self.currentText += self.targetText[self.dialogIndex][0]
        self.targetText[self.dialogIndex] = self.targetText[self.dialogIndex][1:]

    def draw(self, surf):
        self.talk()
        t = self.font.render(str(self.currentText),False,"black")
        textRect = t.get_rect()
        textRect.center = (200, 200)
        surf.blit(t, textRect)

class Label:
    def __init__(self, pos, size, displayText, color):
        self.txtColor = color
        self.d_t = displayText
        self.font = returnFont(int(size/1.5))
        self.text = self.font.render(str(displayText),False,self.txtColor)
        self.textRect = self.text.get_rect()
        self.textRect.center = (pos[0], pos[1])

    def updateColor(self, color):
        self.text = self.font.render(str(self.d_t),False,color)
    def draw(self, surf):

        surf.blit(self.text, self.textRect)





class Button(Label):
    def __init__(self, pos, size, displayText, sound_vibe = 0,UI=False, inactiveColor="beige", hoverColor="gray"):
        self.inactiveColor = inactiveColor
        self.hoverColor = hoverColor
        self.currentColor = [self.inactiveColor, self.hoverColor]
        self.rect = py.rect.Rect(pos[0]-size[0]/2, pos[1]-size[1]/2, size[0], size[1])
        if UI: self.x_d = 1400
        else: self.x_d = 0

        self.clickable = True
        if sound_vibe >0: self.sound = py.mixer.Sound("sounds/button_up.wav")
        elif sound_vibe<0: self.sound = py.mixer.Sound("sounds/button_down.wav")
        else: self.sound = False

        super().__init__(pos, size[1]/1.5, displayText, self.currentColor[1])

    def is_pressed(self, mousePos):
        if self.rect.left+self.x_d<mousePos[0]<self.rect.right+self.x_d and self.rect.top<mousePos[1]<self.rect.bottom:
            self.currentColor = [self.hoverColor, self.inactiveColor]
            if self.txtColor != self.currentColor[1]: self.updateColor(self.currentColor[1])
            if py.mouse.get_pressed()[0] :

                if self.clickable:
                    if not self.sound:
                        print("no sound file")
                    else:
                        self.sound.play()
                        self.sound.set_volume(0.2)
                    return True
                self.clickable = False
        else:
            self.currentColor = [self.inactiveColor, self.hoverColor]
        if not py.mouse.get_pressed()[0]:
            self.clickable=True

    def draw(self, surf):
        py.draw.rect(surf, self.currentColor[0],self.rect)
        if self.txtColor != self.currentColor[1]: self.updateColor(self.currentColor[1])
        super().draw(surf)
    def update(self, surf, mousepos):
        self.is_pressed(mousepos)
        self.draw(surf)



def introScreen(game, surf, mousePos):
    bg = py.rect.Rect(0,0, WW, WH)
    py.draw.rect(surf, "pink", bg)
    title = Label([WW/2, WH/3], 40, "PEWPEWGAME", "Black")
    title.draw(surf)
    play_b = Button([WW/2, WH/2],[200,75], "PLAY", 0,False, "black", "white")
    if play_b.is_pressed(mousePos): game.state = "game"
    play_b.update(surf, mousePos)