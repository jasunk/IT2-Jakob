import pygame as py
from pygame.locals import *
import random, settings


#Splitter opp spritesheet for animasjoner
def splitSheet(sheet, imgSize, split, index, flip = 0):
    xSize = imgSize[0]/split[0]
    ySize = imgSize[1]/split[1]
    img = py.Surface((xSize,ySize), py.SRCALPHA)
    img.blit(sheet, (0,0), (xSize*(index[0]), ySize*(index[1]), xSize*(index[0]+1), ySize*(index[1]+1)))

    img = py.transform.scale(img,(xSize*3,ySize*3))
    img = py.transform.flip(img, flip, 0)
    return img

#Definerer animasjoner for 3 forskjellige monstre
spriteType = {
    1:{
        "Idle":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Idle.png"),                  [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Attack1":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Attack1.png"),            [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Attack2":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Attack2.png"),            [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Death":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Death.png"),                [256, 32], [8,1], [i, 0]) for i in range(8)],
        "Hurt":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Hurt.png"),                  [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Run":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Run.png"),                    [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Throw":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Throw.png"),                [128, 32], [4,1], [i, 0]) for i in range(4)],
        "WalkAttack":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Walk+Attack.png"),     [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Walk":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Walk.png"),                  [192, 32], [6,1], [i, 0]) for i in range(6)]
    },
    2:{
        "Idle":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Idle_4.png"),              [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Attack1":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Attack1_4.png"),        [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Attack2":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Attack2_6.png"),        [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Death":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Death_8.png"),            [256, 32], [8,1], [i, 0]) for i in range(8)],
        "Hurt":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Hurt_4.png"),              [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Run":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Run_6.png"),                [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Throw":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Throw_4.png"),            [128, 32], [4,1], [i, 0]) for i in range(4)],
        "WalkAttack":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Walk+Attack_6.png"), [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Walk":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Walk_6.png"),              [192, 32], [6,1], [i, 0]) for i in range(6)]
    },
    3:{
        "Idle":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Idle_4.png"),                [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Attack1":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Attack1_4.png"),          [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Attack2":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Attack2_6.png"),          [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Death":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Death_8.png"),              [256, 32], [8,1], [i, 0]) for i in range(8)],
        "Hurt":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Hurt_4.png"),                [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Run":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Run_6.png"),                  [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Throw":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Throw_4.png"),              [128, 32], [4,1], [i, 0]) for i in range(4)],
        "WalkAttack":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Walk+Attack_6.png"),   [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Walk":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Walk_6.png"),                [192, 32], [6,1], [i, 0]) for i in range(6)]
    }
}


class Background:

    def __init__(self):
        self.pos1 = [-12, 0]
        self.pos2 = [-20, -300]
        self.pos3 =  [-13, -300]
        self.spriteGroup = py.sprite.Group()
        self.spriteGroup.add()
        self.lengstBak = py.transform.scale(py.image.load("sprites/Platformer - desert/Background/BG-sky.png").convert(),(settings.WW+24, settings.WW))
        self.middels   = py.transform.scale(py.image.load("sprites/Platformer - desert/Background/BG-mountains.png").convert_alpha(),(settings.WW+24, settings.WW))
        self.framst    = py.transform.scale(py.image.load("sprites/Platformer - desert/Background/BG-ruins.png").convert_alpha(),(settings.WW+24, settings.WW))


    def movePic(self, mousePos):
        self.pos1 = [(-12),0]
        self.pos2 = [(-20-(mousePos[0]-settings.WW/2)/65),-settings.WH/2-(mousePos[1]-settings.WH/2)/130]
        self.pos3 = [(-13-(mousePos[0]-settings.WW/2)/30),-settings.WH/1.75-(mousePos[1]-settings.WH/2)/60]
    def update(self, surf):

        surf.blit(self.lengstBak, (self.pos1[0], self.pos1[1]))
        surf.blit(self.middels, (self.pos2[0], self.pos2[1]))
        surf.blit(self.framst, (self.pos3[0], self.pos3[1]))



#Klasse som håndterer tegning og animasjon av monstre
class SpriteHandler():

    def __init__(self, spriteNum,  player=False):
        self.spriteNum = spriteNum
        self.frame = 0
        self.counter = 0
        self.state = "Idle"
        self.player = player
        self.pos = [0,0]
        self.particlePos = [0,0]
        self.shouldDisplay = True
        if self.player:
            self.activePos = [0, self.pos[1]]
        else:
            self.activePos = [settings.WW-32*3, self.pos[1]]
        self.enemySpeed = self.activePos[0]-(settings.WW/2-settings.WW/8)



    def setState(self, state):
        self.frame = 0
        self.state = state

    def draw(self, plane, mousepos):
        imageToDraw = spriteType[self.spriteNum][self.state][self.frame]
        self.particlePos = [self.pos[0]+(32*3)/2, self.pos[1]+(32*3)/2]
        #flip sprite
        if not self.player:
            self.pos = [settings.WW/2+settings.WW/20, settings.WH/2]
            imageToDraw = py.transform.flip(imageToDraw,1,0)
        else:
            self.pos = [settings.WW/2-settings.WW/8, settings.WH/2]


        if self.activePos[0] < self.pos[0] and self.player:
            imageToDraw = spriteType[self.spriteNum]["Walk"][self.frame]
            self.activePos[0] += (self.pos[0])/100
        if self.activePos[0]> self.pos[0] and not self.player:
            imageToDraw = spriteType[self.spriteNum]["Walk"][self.frame]
            imageToDraw = py.transform.flip(imageToDraw,1,0)
            self.activePos[0] -= (self.enemySpeed)/120

        if settings.respondToMouse:
            plane.blit(imageToDraw.convert_alpha(), (self.activePos[0]-mousepos[0], self.pos[1]-mousepos[1]))
        else:
            plane.blit(imageToDraw.convert_alpha(), (self.activePos[0], self.pos[1]))
    def update(self, plane, mousepos):

        if self.counter<3:
            self.counter+=1
        else:
            self.counter=0
            if self.frame < len(spriteType[self.spriteNum][self.state])-1:
                self.frame+=1
            elif self.state != "Death":
                self.frame = 0
                if self.state != "Idle" :
                    self.state = "Idle"
            else:
                self.shouldDisplay=False

        if self.shouldDisplay: self.draw(plane, mousepos)







class PokerMann:
    def __init__(self, name, spritehandler, level, initHealth, abilities, sprite, playable = False):
        self.name = name
        self.level = level
        self.initHealth = initHealth
        self.currentHealth = initHealth
        self.healthDisplay = initHealth
        self.abilities = abilities
        self.sprite = sprite
        self.playable = playable
        self.spriteHandler = spritehandler
        self.spriteHandler.setState("Idle")
        self.particles = []
        self.yourTurn = True
        self.AITimer = -10
        self.dead = False

    def useAbility(self, index):

        if not self.dead and self.yourTurn:
            self.yourTurn=False
            if not self.abilities[index].use():
                if not self.playable:
                    self.particles.append(DamageNumber("Bommet", [5,-5], self.spriteHandler.particlePos))
                    if self.abilities[index].animtype=="Throw" and self.abilities[index].healingFactor <10:
                        self.particles.append(Particle([15,15], self.spriteHandler.particlePos, [-130, -5], "black", 3, [0,-20], "sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Rock2.png"))

                else:
                    self.particles.append(DamageNumber("Bommet", [-5,-5], self.spriteHandler.particlePos))
                    if self.abilities[index].animtype=="Throw" and self.abilities[index].healingFactor <10:
                        self.particles.append(Particle([15,15], self.spriteHandler.particlePos, [130, -5], "black", 3, [0,-20], "sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Rock2.png"))
            elif self.abilities[index].animtype=="Throw" and self.abilities[index].healingFactor <10:

                if not self.playable:
                    self.particles.append(Particle([15,15], self.spriteHandler.particlePos, [-250, -55], "black", 2.5, [0,-30], "sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Rock2.png"))
                else:
                    self.particles.append(Particle([15,15], self.spriteHandler.particlePos, [250, -55], "black", 2.5, [0,-30], "sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Rock2.png"))
            self.spriteHandler.setState(self.abilities[index].animtype)



    def heal(self, factor, randomness):
        toHeal = factor +(random.randint(-1,1)*randomness)
        if self.currentHealth + toHeal>self.initHealth:
            self.currentHealth=self.initHealth
        else:
            self.currentHealth += toHeal

        self.particles.append(Particle([1,1], [0,0], [0,0], "black", 13))
        for i in range(25):
            if self.particles[i-1].velocity[0]>0:
                oppositeDir = -1
            else:
                oppositeDir=1
            if not self.playable: #Funker faen ikke
                self.particles.append(Particle([7,7], [self.spriteHandler.particlePos[0], self.spriteHandler.particlePos[1]], [random.randint(-round(settings.WW/40), round(settings.WW/40))*(oppositeDir), random.randint(int(-settings.WH/40),0)], "green", 12, [0,0]))
            else:
                self.particles.append(Particle([7,7], [self.spriteHandler.particlePos[0], self.spriteHandler.particlePos[1]], [random.randint(-round(settings.WW/40), round(settings.WW/40))*(oppositeDir), random.randint(int(-settings.WH/40),0)], "green", 12, [0,0]))


    def drawHealthBar(self, surf):
        font = py.font.Font('sprites/free-pixel-art-tiny-hero-sprites/Font/Planes_ValMore.ttf', 20)

        nameTxt = font.render(f"{self.name} ", True, settings.colors["TXT"])
        lvlTxt = font.render(f"Level: {self.level} ", True, settings.colors["TXT"])

        nameRect = nameTxt.get_rect()
        lvlRect = lvlTxt.get_rect()

        if self.playable:
            nameRect.x = 50
            nameRect.y = settings.WH-220
            lvlRect.x = settings.WW-150
            lvlRect.y = settings.WH-220
        else:
            nameRect.x = 50
            nameRect.y = 50
            lvlRect.x = settings.WW-150
            lvlRect.y = 50
        surf.blit(nameTxt, nameRect)
        surf.blit(lvlTxt, lvlRect)
        xPos, yPos = 0, 0
        if self.playable:
            xPos, yPos = settings.WW/2-220, settings.WH-220
        else:
            xPos, yPos = settings.WW/2-220, 50
        outerRect = py.rect.Rect(xPos, yPos, 400, 20)


        if self.healthDisplay > self.currentHealth:
            self.healthDisplay-=1
            if self.currentHealth<0:
                self.healthDisplay-=3
        if self.healthDisplay< self.currentHealth:
            self.healthDisplay+=1
        innerRect = py.rect.Rect(xPos+2, yPos+2, ((self.healthDisplay/self.initHealth)*400)-4, 14)


        py.draw.rect(surf, settings.colors["BG"], outerRect)
        py.draw.rect(surf, settings.colors["HP"], innerRect)

        font = py.font.Font('Pixelify_Sans/static/PixelifySans-Bold.ttf', 13)

        txt = font.render(f"{self.currentHealth:.0f} / {self.initHealth} HP", True, settings.colors["BG"])
        txtRect = txt.get_rect()

        txtRect.x=xPos+5
        txtRect.y = yPos+1
        surf.blit(txt, txtRect)

    def drawOptions(self, surf):
        backBox0 = py.rect.Rect(0,settings.WH-settings.WH/4,settings.WW, settings.WH/5)
        backBox1 = py.rect.Rect(2,settings.WH-settings.WH/4.1,settings.WW-4, settings.WH/5)
        backBox2 = py.rect.Rect(8,settings.WH-settings.WH/4.2,settings.WW-16, settings.WH/5)
        py.draw.rect(surf, settings.colors["UI"], backBox0, 0, 10)
        py.draw.rect(surf, settings.colors["BG"], backBox1, 0, 10)
        py.draw.rect(surf, settings.colors["UI"], backBox2, 0, 10)

        xIncrease = 0
        yIncrease = 0

        for ability in self.abilities:
            font = py.font.Font('Pixelify_Sans/static/PixelifySans-Medium.ttf', 20)
            text = font.render(f"{ability.name} ({ability.damage} damage and {ability.healingFactor} healing)", True, settings.colors["TXT"])

            textRect = text.get_rect()
            textRect.x = settings.WW/10 +xIncrease
            textRect.y = settings.WH/2+settings.WH/3 + yIncrease
            surf.blit(text, textRect)
            if xIncrease ==0:
                xIncrease+=settings.WW/2+80
            else:
                xIncrease=0
                yIncrease+=80

    def enemyInfo(self,surf):
        backBox0 = py.rect.Rect(0,0,settings.WW, 120)
        backBox1 = py.rect.Rect(2,2,settings.WW-4, 116)
        backBox2 = py.rect.Rect(8,8,settings.WW-16, 104)
        py.draw.rect(surf, settings.colors["UI"], backBox0, 0, 10)
        py.draw.rect(surf, settings.colors["BG"], backBox1, 0, 10)
        py.draw.rect(surf, settings.colors["UI"], backBox2, 0, 10)

        font = py.font.Font('Pixelify_Sans/static/PixelifySans-Bold.ttf', 20)

        txt = font.render(f"Enemy", True, settings.colors["TXT"])
        txtRect = txt.get_rect()

        txtRect.x=settings.WW/2-45
        txtRect.y = 10
        surf.blit(txt, txtRect)


    def takeDamage(self, damage, critChance, randomness):
        damageToTake = 0
        critHit = False
        if random.randint(0,100) < critChance:
            damageToTake = (damage+(random.randrange(-1,2)*(randomness/random.randrange(1,randomness))))*2
            critHit = True

        else:
            damageToTake = damage+(random.randrange(-1,2)*(randomness/random.randrange(1,randomness)))

        if not self.playable:
            self.particles.append(DamageNumber(round(damageToTake), [5,-5], self.spriteHandler.particlePos))
        else:
            self.particles.append(DamageNumber(round(damageToTake), [-5,-5], self.spriteHandler.particlePos))
        if critHit:
            if not self.playable:
                self.particles.append(DamageNumber("CRITICAL HIT", [-5,-2], self.spriteHandler.particlePos))
            else:
                self.particles.append(DamageNumber("CRITICAL HIT", [5,-2], self.spriteHandler.particlePos))




        self.currentHealth-=damageToTake


        self.spriteHandler.setState("Hurt")
        if self.currentHealth<=0:
            self.spriteHandler.setState("Death")
        for i in range(30):
            if not self.playable:
                self.particles.append(Particle([7,7], [self.spriteHandler.particlePos[0], self.spriteHandler.particlePos[1]], [random.randint(-20,151), random.randint(-150,-80)], "red", 12, [0,-12]))
            else:
                self.particles.append(Particle([7,7], [self.spriteHandler.particlePos[0], self.spriteHandler.particlePos[1]], [random.randint(-151,20), random.randint(-150,-80)], "red", 12, [0,-12]))


    def input(self, mousePos):
        keystrokes = py.key.get_pressed()

        if mousePos[0]< settings.WW/2 and  (settings.WH-200<mousePos[1]<settings.WH-100):
            if py.mouse.get_pressed()[0]:
                self.useAbility(0)
        elif mousePos[0]> settings.WW/2 and  (settings.WH-200<mousePos[1]<settings.WH-100):
            if py.mouse.get_pressed()[0]:
                self.useAbility(1)
        if mousePos[0]< settings.WW/2 and  (settings.WH-100<mousePos[1]<settings.WH):
            if py.mouse.get_pressed()[0]:
                self.useAbility(2)
        elif mousePos[0]> settings.WW/2 and  (settings.WH-100<mousePos[1]<settings.WH):
            if py.mouse.get_pressed()[0]:
                self.useAbility(3)
    def update(self, surf, mousePos):

        for p in self.particles:
            p.update(surf)
            if p.lifetime<0:
                self.particles.remove(p)

        if self.playable:
            self.drawOptions(surf)
        else:
            self.enemyInfo(surf)

        self.drawHealthBar(surf)

        if self.playable: self.input(mousePos)

        self.spriteHandler.update(surf, [(mousePos[0]-settings.WW/2)/50, (mousePos[1]-settings.WH/2)/100])

        if not self.playable:
            self.AITimer-=0.2
            if -1< self.AITimer<1:

                self.useAbility(random.randint(0, len(self.abilities)-1))
                self.AITimer=-100

        if self.currentHealth<=0:
            if not self.dead: self.spriteHandler.setState("Death")
            self.dead=True




class Ability():
    """
    Navn blir displayname for ability i UI
    Character er karakteren som utøver angrepet
    target er karakteren som skal angripes
    damage er basisskaden for angrep
    critchance (oppgitt mellom 0 og 100) bestemmer hvor ofte damage dobles
    randomness er tilfeldige avvik i skade, kan gå både i pluss og minus
    animtype skal bestemme animasjon tik karakter
    successrate og heal sier seg selv (sant?)
    """
    def __init__(self, name, character, target, damage, critchance, randomness, animtype, successrate=100, heal=0):
        self.name = name
        self.damage = damage
        self.character = character
        self.critChance = critchance
        self.randomness = randomness
        self.animtype = animtype
        self.successrate = successrate
        self.healingFactor = heal
        self.target = target

    def use(self):
        self.target.yourTurn = True
        self.target.AITimer = random.randint(3,11)
        if random.randrange(0,101)<self.successrate:
            print(f"Utfører {self.name}")
            if self.damage != 0:
                self.target.takeDamage(self.damage, self.critChance, self.randomness)
            if self.healingFactor != 0:
                self.character.heal(self.healingFactor, self.randomness)

            return True
        else:


            print(f"{self.name} feilet")
            return False


class Particle:
    def __init__(self, size, pos, velocity, color, lifetime, damping = [0,0], image="nah"):
        self.pos = pos
        self.size = [size[0]*random.randint(9,12)/10, size[1]*random.randint(9,12)/10]
        self.rect = py.rect.Rect(pos[0], pos[1], size[0], size[1])
        self.velocity = velocity
        self.damping = damping
        self.color = color
        self.lifetime = lifetime
        self.image = image


    def draw(self, plane):
        if self.image =="nah":
            py.draw.rect(plane, self.color, self.rect)
        else:
            plane.blit(py.transform.scale(py.image.load(self.image),(24,24)), (self.pos[0], self.pos[1]))

    def move(self):
        self.pos[0] += self.velocity[0]/10
        self.pos[1] += self.velocity[1]/10
        self.velocity[0] -= self.damping[0]
        self.velocity[1] -= self.damping[1]

    def update(self, plane):
        self.rect = py.rect.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.move()
        self.draw(plane)
        self.lifetime-=0.3
        print(self.velocity)

class DamageNumber:
    def __init__(self, damage, velocity, pos, crit=False):
        if crit:
            self.font = py.font.Font('sprites/free-pixel-art-tiny-hero-sprites/Font/Planes_ValMore.ttf', 34)
        else:
            self.font = py.font.Font('sprites/free-pixel-art-tiny-hero-sprites/Font/Planes_ValMore.ttf', 22)
        self.txt = self.font.render(str(damage), True, settings.colors["TXT"])
        self.rect = self.txt.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.velocity = velocity
        self.lifetime = 5

    def draw(self, surf):
        surf.blit(self.txt, self.rect)
    def move(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def update(self, surf):
        self.draw(surf)
        self.move()
        self.lifetime-=0.3


class Button:
    def __init__(self, text, pos, size, bevel = -1):
        self.text = text
        self.pos = pos
        self.size = size
        self.bevel = bevel
        self.font = py.font.Font('sprites/free-pixel-art-tiny-hero-sprites/Font/Planes_ValMore.ttf', 22)
        self.txt = self.font.render(str(text), True, settings.colors["TXT"])
        self.textRect = self.txt.get_rect()
        self.textRect.x = pos[0]+ self.textRect.width/2
        self.textRect.y = pos[1]+ self.textRect.width/2
    def draw(self, plane):
        plane.blit(self.txt, self.textRect)

    def inputHandler(self, mousepos):
        pass

    def update(self, plane, mousepos):
        self.draw(plane)
        self.inputHandler(mousepos)



mann = PokerMann(
    "Jens",
    SpriteHandler(1,True),
    10,
    150,
    [],
    0,
    True
)

pikk = PokerMann(
    "Fjomperompe",
    SpriteHandler(2),
    4,
    110,
    [],
    0
)

mann.abilities = \
[
    Ability("Klæss", mann, pikk, 10, 10, 2, "Attack1", 90),
    Ability("Mediter", mann, pikk, 0, 0, 10, "Throw", 65, 30),
    Ability("SMÆKK SMÆKK", mann, pikk, 15, 50, 10, "Attack2", 75),
    Ability("YEET", mann, pikk, 100, 25, 2, "Throw", 10)
]

pikk.abilities = \
    [
        Ability("Klæss", pikk, mann, 10, 10, 2, "Attack1", 90),
        Ability("Klæss", pikk, mann, 10, 10, 2, "Attack1", 90),
        Ability("Mediter", pikk, mann, 0, 0, 10, "Throw", 50, 50),
        Ability("SMÆKK SMÆKK", pikk, mann, 24, 50, 10, "Attack2", 50),
        Ability("YEET", pikk, mann, 100, 25, 2, "Throw", 10)
    ]





#   c8nwfjxp
