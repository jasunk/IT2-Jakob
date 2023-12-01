import pygame as py
from pygame.locals import *
import random, settings, saves, saves_V2
import gtts, time


py.init()

py.mixer.init() # add this line

#Splitter opp spritesheet for animasjoner
def splitSheet(sheet, imgSize, split, index, flip = 0):
    xSize = imgSize[0]/split[0]
    ySize = imgSize[1]/split[1]
    img = py.Surface((xSize,ySize), py.SRCALPHA)
    img.blit(sheet, (0,0), (xSize*(index[0]), ySize*(index[1]), xSize*(index[0]+1), ySize*(index[1]+1)))

    img = py.transform.scale(img,(xSize*3,ySize*3))
    img = py.transform.flip(img, flip, 0)
    return img

#Definerer animasjoner for 3 forskjellige monstre (listcomprehention my love <3)
spriteType = {
    1:{
        "Idle":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Idle.png"),                  [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Attack1":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Attack1.png"),            [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Attack2":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Attack2.png"),            [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Death":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Death.png"),                [256, 32], [8,1], [i, 0]) for i in range(8)],
        "Hurt":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Hurt.png"),                  [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Run":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Run.png"),                    [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Throw":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Throw.png"),                [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Throw2":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Throw.png"),                [128, 32], [4,1], [i, 0]) for i in range(4)],
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
        "Throw2":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Throw_4.png"),            [128, 32], [4,1], [i, 0]) for i in range(4)],
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
        "Throw2":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Throw_4.png"),              [128, 32], [4,1], [i, 0]) for i in range(4)],
        "WalkAttack":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Walk+Attack_6.png"),   [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Walk":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Walk_6.png"),                [192, 32], [6,1], [i, 0]) for i in range(6)]
    }
}

#tegner bakgrunn
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

    #lager paralax-effekt om aktivt i innstillinger (håndteres i main)
    def movePic(self, mousePos):
        self.pos1 = [(-12),0]
        self.pos2 = [(-20-(mousePos[0]-settings.WW/2)/65),-settings.WH/2-(mousePos[1]-settings.WH/2)/130]
        self.pos3 = [(-13-(mousePos[0]-settings.WW/2)/30),-settings.WH/1.75-(mousePos[1]-settings.WH/2)/60]
    #tegner
    def update(self, surf):

        surf.blit(self.lengstBak, (self.pos1[0], self.pos1[1]))
        surf.blit(self.middels, (self.pos2[0], self.pos2[1]))
        surf.blit(self.framst, (self.pos3[0], self.pos3[1]))



#Klasse som håndterer tegning og animasjon av monstre
class SpriteHandler():

    def __init__(self, spriteNum,  player=False, shouldWalk = True):
        print(spriteNum)
        self.spriteNum = spriteNum
        self.shouldWalk = shouldWalk
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


    #bestemmer hvilke animasjon som skal vises
    def setState(self, state):
        self.frame = 0
        self.state = state


    def draw(self, plane, mousepos):
        #Velger bilde å tegne, angir en posisjon for partikler å spawne fra
        try:
            imageToDraw = spriteType[self.spriteNum][self.state][self.frame]
        except IndexError:
            imageToDraw = spriteType[self.spriteNum]["Idle"][0]
            self.frame=0
        self.particlePos = [self.pos[0]+(32*3)/2, self.pos[1]+(32*3)/2]
        #flip sprite om ikke spiller
        if not self.player:
            self.pos = [settings.WW/2+settings.WW/20, settings.WH/2]
            imageToDraw = py.transform.flip(imageToDraw,1,0)
        else:
            self.pos = [settings.WW/2-settings.WW/8, settings.WH/2]


        #introsekvens, får monstre til å løpe mot ønsket posisjon i self.[pos]
        if self.activePos[0] < self.pos[0] and self.player and self.shouldWalk:
            imageToDraw = spriteType[self.spriteNum]["Run"][self.frame]
            self.activePos[0] += (self.pos[0])/80
        if self.activePos[0]> self.pos[0] and not self.player and self.shouldWalk:
            try:
                imageToDraw = spriteType[self.spriteNum]["Run"][self.frame]
            except IndexError:
                imageToDraw = spriteType[self.spriteNum]["Idle"][0]
            imageToDraw = py.transform.flip(imageToDraw,1,0)
            self.activePos[0] -= (self.enemySpeed)/90

        if settings.respondToMouse:
            if self.shouldWalk:
                plane.blit(imageToDraw.convert_alpha(), (self.activePos[0]-mousepos[0], self.pos[1]-mousepos[1]))
            else:
                plane.blit(imageToDraw.convert_alpha(), (self.pos[0]-mousepos[0], self.pos[1]-mousepos[1]))
        else:
            if self.shouldWalk:
                plane.blit(imageToDraw.convert_alpha(), (self.activePos[0], self.pos[1]))
            else:
                plane.blit(imageToDraw.convert_alpha(), (self.pos[0], self.pos[1]))
    def update(self, plane, mousepos):

        #Bruker konstant 3 for å ikke oppdatere sprite for hver frame
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
    #init-values :)
    def __init__(self, name, spritehandler, level, initHealth, abilities, playable = False):
        self.name = name
        self.level = level
        self.initHealth = initHealth
        self.currentHealth = initHealth
        self.healthDisplay = initHealth
        self.abilities = abilities

        self.playable = playable
        self.spriteHandler = spritehandler
        self.spriteHandler.setState("Idle")
        self.particles = []
        self.yourTurn = True
        self.AITimer = -10
        self.dead = False
        self.target = ""
        self.XPtoNextLevel = 100
        self.currentXP = 0




    #oppdaterer verdi i abilies
    def refreshTarget(self, target):
        self.target=target
        for a in self.abilities:
            a.target = target

    #bruker ability, tar inn index som ønsket angrep
    def useAbility(self, index):
        for a in self.abilities:
            a.target=self.target

        #gjenomføres bare om man lever og har sin tur tilgjengelig
        if not self.dead and self.yourTurn:
            self.yourTurn=False
            #bruker ability, og returnerer en bool om angrep var vellykket eller ikke
            if not self.abilities[index].use():
                #skriver bommet ved monsters riktige posisjon, basert på om den er playable eller ikke
                if not self.playable:
                    self.particles.append(DamageNumber("Bommet", [5,-5], self.spriteHandler.particlePos))

                    #om angrepet er av type throw, og man bommer kastes steinen for kort
                    if self.abilities[index].animtype=="Throw" and self.abilities[index].healingFactor <10:
                        self.particles.append(Particle([15,15], self.spriteHandler.particlePos, [-130, -5], "black", 3, [0,-20], "sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Rock2.png"))

                #samme logikk, men for spiller
                else:
                    self.particles.append(DamageNumber("Bommet", [-5,-5], self.spriteHandler.particlePos))
                    if self.abilities[index].animtype=="Throw" and self.abilities[index].healingFactor <10:
                        self.particles.append(Particle([15,15], self.spriteHandler.particlePos, [130, -5], "black", 3, [0,-20], "sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Rock2.png"))


            #dersom ability er av type throw, tegner vi en stein som treffer:)
            elif self.abilities[index].animtype=="Throw":

                if not self.playable:
                    self.particles.append(Particle([15,15], self.spriteHandler.particlePos, [-250, -55], "black", 2.5, [0,-30], "sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Rock2.png"))
                else:
                    self.particles.append(Particle([15,15], self.spriteHandler.particlePos, [250, -55], "black", 2.5, [0,-30], "sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Rock2.png"))
            self.spriteHandler.setState(self.abilities[index].animtype)




    #helbredings-logikk
    def heal(self, factor, randomness):
        #tar inn healingfactor, og endrer basert på ability-randomness
        toHeal = factor +(random.randint(-1,1)*randomness)


        healSound = py.mixer.Sound(f"playerAudio/heal.wav")
        py.mixer.Sound.play(healSound)
        #undersøker om helse blir over max, eller ikke
        if self.currentHealth + toHeal>self.initHealth:
            self.currentHealth=self.initHealth
        else:
            self.currentHealth += toHeal

        #nødvendig failsafe-partikkel
        self.particles.append(Particle([1,1], [0,0], [0,0], "black", 13))

        #spawner healing-partikler ved riktig posisjon
        for i in range(25):
            #flipper neste partikkel for en litt mer symmetrisk eksplosjon
            if self.particles[i-1].velocity[0]>0:
                oppositeDir = -1
            else:
                oppositeDir=1

            self.particles.append(Particle([7,7], [self.spriteHandler.particlePos[0], self.spriteHandler.particlePos[1]], [random.randint(-round(settings.WW/40), round(settings.WW/40))*(oppositeDir), random.randint(int(-settings.WH/40),0)], "green", 12, [0,0]))



    #håndterer helse, xp og level-tegning
    def drawHealthBar(self, surf):

        font = py.font.Font('sprites/free-pixel-art-tiny-hero-sprites/Font/Planes_ValMore.ttf', 20)

        #velger tekst å skrive
        nameTxt = font.render(f"{self.name} ", True, settings.colors["TXT"])
        lvlTxt = font.render(f"Level: {self.level} ", True, settings.colors["TXT"])

        #gjør tekst mindre
        font = py.font.Font('sprites/free-pixel-art-tiny-hero-sprites/Font/Planes_ValMore.ttf', 16)
        XPtext = font.render(f"XP: {self.currentXP} / {self.XPtoNextLevel} ", True, settings.colors["TXT"])

        #lager rects for hver
        nameRect = nameTxt.get_rect()
        lvlRect = lvlTxt.get_rect()
        XPrect = XPtext.get_rect()

        #posisjonerer pos basert på hvem sine stats det er
        if self.playable:
            nameRect.x = 50
            nameRect.y = settings.WH-220
            lvlRect.x = settings.WW-150
            lvlRect.y = settings.WH-220
            XPrect.x = settings.WW-290
            XPrect.y = lvlRect.y
        else:
            nameRect.x = 50
            nameRect.y = 50
            lvlRect.x = settings.WW-150
            lvlRect.y = 50

        #tegner navn, level og xp
        surf.blit(nameTxt, nameRect)
        surf.blit(lvlTxt, lvlRect)
        surf.blit(XPtext, XPrect)

        #velger posisjon for helsebar basert på playable
        xPos, yPos = 0, 0
        if self.playable:
            xPos, yPos = settings.WW/2-220, settings.WH-220
        else:
            xPos, yPos = settings.WW/2-220, 50
        outerRect = py.rect.Rect(xPos, yPos, 400, 20)

        #håndterer smooth animasjon mellom helse-states
        if self.healthDisplay > self.currentHealth:
            self.healthDisplay-=1
            if self.currentHealth<0:
                self.healthDisplay-=3
        if self.healthDisplay< self.currentHealth:
            self.healthDisplay+=1


        innerRect = py.rect.Rect(xPos+2, yPos+2, ((self.healthDisplay/self.initHealth)*400)-4, 14)
        #tegner bakgrunn for helse
        py.draw.rect(surf, settings.colors["BG"], outerRect)

        #tegner helse
        py.draw.rect(surf, settings.colors["HP"], innerRect)

        #skriver HP med tall
        font = py.font.Font('Pixelify_Sans/static/PixelifySans-Bold.ttf', 13)
        txt = font.render(f"{self.currentHealth:.0f} / {self.initHealth} HP", True, settings.colors["BG"])
        txtRect = txt.get_rect()
        txtRect.x=xPos+5
        txtRect.y = yPos+1
        surf.blit(txt, txtRect)

        #tegner opp interface for valg av ablity
    def drawOptions(self, surf):

        #tilpasser 3 firkanter for litt estetisk nammenam
        backBox0 = py.rect.Rect(0,settings.WH-settings.WH/4,settings.WW, settings.WH/5)
        backBox1 = py.rect.Rect(2,settings.WH-settings.WH/4.1,settings.WW-4, settings.WH/5)
        backBox2 = py.rect.Rect(8,settings.WH-settings.WH/4.2,settings.WW-16, settings.WH/5)
        py.draw.rect(surf, settings.colors["UI"], backBox0, 0, 10)
        py.draw.rect(surf, settings.colors["BG"], backBox1, 0, 10)
        py.draw.rect(surf, settings.colors["UI"], backBox2, 0, 10)

        #variabel som bestemmer posisjon
        xIncrease = 0
        yIncrease = 0

        #plasserer hver ability
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

    #tegner boks med litt informasjon om fiende
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


    #håndterer å ta skade
    def takeDamage(self, damage, critChance, randomness):

        ouch = py.mixer.Sound(f"playerAudio/hitHurt{random.randint(0,3)}.wav")
        py.mixer.Sound.play(ouch)


        #init-verdier
        damageToTake = 0
        critHit = False

        #undersøker om angrepet blir critical
        if random.randint(0,100) < critChance:
            #tar skade basert på basis-skade, tilfeldighet og ganger til slutt med 2 for crithit
            damageToTake = (damage+(random.randrange(-1,2)*(randomness/(random.randrange(1,randomness*10)/10))))*2
            critHit = True

        else:
            #tar skade basert på basis-skade og tilfeldighet
            damageToTake = damage+(random.randrange(-1,2)*(randomness/(random.randrange(1,randomness*10)/10)))

        #for å sørge for at ingen angrep helbreder den andre
        if damageToTake<0:
            damageToTake=3

        #tegner damage-numbers for inkommende angrep
        if not self.playable:
            self.particles.append(DamageNumber(round(damageToTake), [5,-5], self.spriteHandler.particlePos))
        else:
            self.particles.append(DamageNumber(round(damageToTake), [-5,-5], self.spriteHandler.particlePos))

        #skriver critical hit om truffet med crit
        if critHit:
            if not self.playable:
                self.particles.append(DamageNumber("CRITICAL HIT", [-5,-2], self.spriteHandler.particlePos))
            else:
                self.particles.append(DamageNumber("CRITICAL HIT", [5,-2], self.spriteHandler.particlePos))

        #fjerner (endelig) skade
        self.currentHealth-=damageToTake

        #spiller animasjon hurt, og death om en er tom for liv
        self.spriteHandler.setState("Hurt")
        if self.currentHealth<=0:
            self.spriteHandler.setState("Death")

        #spawner blod partikler, skiller mellom spiller og ikke for velocity sin del
        for i in range(30):
            if not self.playable:
                self.particles.append(Particle([7,7], [self.spriteHandler.particlePos[0], self.spriteHandler.particlePos[1]], [random.randint(-20,151), random.randint(-150,-80)], "red", 12, [0,-12]))
            else:
                self.particles.append(Particle([7,7], [self.spriteHandler.particlePos[0], self.spriteHandler.particlePos[1]], [random.randint(-151,20), random.randint(-150,-80)], "red", 12, [0,-12]))


    #håndterer museklikk på knapper
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


    #kjører alle funksjoner nødvendig pr frame
    def update(self, surf, mousePos):

        #tegner og håndterer partikler
        for p in self.particles:
            p.update(surf)
            if p.lifetime<0:
                self.particles.remove(p)

        #oppdaterer verdier, tegner riktig UI
        if self.playable:
            self.drawOptions(surf)
            self.input(mousePos)
            self.currentXP = saves_V2.loadSave()["player"]["currentXP"]
            self.XPtoNextLevel = saves_V2.loadSave()["player"]["XPtoLevelUp"]
            self.level = saves_V2.loadSave()["player"]["lvl"]
        else:
            self.enemyInfo(surf)
            self.currentXP = saves_V2.loadSave()["enemy"]["currentXP"]
            self.XPtoNextLevel = saves_V2.loadSave()["enemy"]["XPtoLevelUp"]
            self.level = saves_V2.loadSave()["enemy"]["lvl"]
        self.drawHealthBar(surf)


        #oppdaterer spriteHandler-klassen med surf og posisjon å tegne på
        self.spriteHandler.update(surf, [(mousePos[0]-settings.WW/2)/50, (mousePos[1]-settings.WH/2)/100])

        #håndterer AI-angrep basert på AITimer timeren :)
        if not self.playable:
            self.AITimer-=0.2
            if -1< self.AITimer<1:

                self.useAbility(random.randint(0, len(self.abilities)-1))
                self.AITimer=-100

        # om død: dø
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
        print(self.character.name, self.target.name)
        #endrer tur til motstander
        self.target.yourTurn = True
        self.target.AITimer = random.randint(3,11)

        #om angrep er succesfull, gjør skade, eller heal deg selv
        if random.randrange(0,101)<self.successrate:
            print(f"Utfører {self.name}")
            if self.damage != 0:
                self.target.takeDamage(self.damage, self.critChance, self.randomness)
            if self.healingFactor != 0:
                self.character.heal(self.healingFactor, self.randomness)

            #self explanatory B)
            if self.name == "Yo mama joke":
                self.urMomJoke()

            return True
        else:


            print(f"{self.name} feilet")
            return False
    def urMomJoke(self):
        #masse yo mama vitser fra internett :)
        jokes = [
            "Yo mama's so fat, when she fell I didn't laugh, but the sidewalk cracked up.",
            "Yo mama's so fat, when she skips a meal, the stock market drops.",
            "Yo mama's so fat, it took me two buses and a train to get to her good side.",
            "Yo mama's so fat, when she goes camping, the bears hide their food.",
            "Yo mama's so fat, if she buys a fur coat, a whole species will become extinct.",
            "Yo mama's so fat, she stepped on a scale and it said: 'To be continued.'",
            "Yo momma is so fat, I swerved to miss her in my car and ran out of gas.",
            "Yo mama's so fat, when she wears high heels, she strikes oil.",
            "Yo mama's so fat, she was overthrown by a small militia group, and now she's known as the Republic of Yo Mama.",
            "Yo mama is so fat, not even Dora can explore her.",
            "Yo mama is so fat, she gets group insurance.",
            "Yo mama's so fat, when she went to KFC and the cashier asked what size bucket she wanted, she said, 'The one on the roof!'",
            "Yo mama is so big, her belt size is equator.",
            "Yo mama so fat, when she talks to herself, it's a long-distance call.",
            "Yo mama so fat, she left in high heels and came back in flip flops.",
            "Yo mama is so fat that when she hauls ass, she has to make two trips.",
            "Yo mama so fat, her job title is Spoon and Fork Operator.",
            "Yo mama so fat, when she walked past the TV, I missed three episodes.",
            "Yo momma's so fat, when she sits around the house, she SITS AROUND the house.",
            "Yo mama's so fat, her car has stretch marks.",
            "Yo mama's so fat, she can't even jump to a conclusion.",
            "Yo mama's so fat, her blood type is Ragu.",
            "Yo mama's so fat, if she was a Star Wars character, her name would be Admiral Snackbar.",
            "Yo mama's so fat, she brought a spoon to the Super Bowl."
        ]
        #legger til en partikkel med joken på, for jokes tihi
        joke = jokes[random.randint(0,len(jokes)-1)]
        self.character.particles.append(DamageNumber(joke, [0, -2], [settings.WW/4, settings.WH/2], False, 25))
        self.character.speak(12)




        #et generelt partikkel
class Particle:
    def __init__(self, size, pos, velocity, color, lifetime, damping=[0, 0], image="nah"):
        self.pos = pos
        self.size = [size[0] * random.randint(9, 12) / 10, size[1] * random.randint(9, 12) / 10]
        self.rect = py.rect.Rect(pos[0], pos[1], size[0], size[1])
        self.velocity = velocity
        self.damping = damping
        self.color = color
        self.lifetime = lifetime
        self.image = image

    def draw(self, plane):
        if self.image == "nah":
            py.draw.rect(plane, self.color, self.rect)
        else:
            plane.blit(py.transform.scale(py.image.load(self.image), (24, 24)), (self.pos[0], self.pos[1]))

    def move(self):
        self.pos[0] += self.velocity[0] / 10
        self.pos[1] += self.velocity[1] / 10
        self.velocity[0] -= self.damping[0]
        self.velocity[1] -= self.damping[1]

    def update(self, plane):
        self.rect = py.rect.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.move()
        self.draw(plane)
        self.lifetime -= 0.3


# DamageNumber er en utvidelse av Particle
class DamageNumber(Particle):
    def __init__(self, damage, velocity, pos, crit=False, lifetime=5):
        #Mækker et generelt partikkel
        super().__init__([0, 0], pos, velocity, (0, 0, 0), lifetime)

        if crit:
            self.font = py.font.Font('sprites/free-pixel-art-tiny-hero-sprites/Font/Planes_ValMore.ttf', 34)
        else:
            self.font = py.font.Font('sprites/free-pixel-art-tiny-hero-sprites/Font/Planes_ValMore.ttf', 22)
        self.txt = self.font.render(str(damage), True, settings.colors["TXT"])

    def draw(self, surf):
        surf.blit(self.txt, self.rect)

    def move(self):
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        self.rect.x, self.rect.y = self.pos  # Update rect based on the new position

    def update(self, surf):
        self.draw(surf)
        self.move()
        self.lifetime -= 0.3

#Generelt tekst-objekt
class Label:
    def __init__(self, text, pos, size):
        self.text = text
        self.pos = pos
        self.size = size
        self.font = py.font.Font('sprites/free-pixel-art-tiny-hero-sprites/Font/Planes_ValMore.ttf', self.size)
        self.txt = self.font.render(str(text), True, settings.colors["TXT"])
        self.textRect = self.txt.get_rect()
        self.textRect.x = pos[0] - self.textRect.width / 2
        self.textRect.y = pos[1] - self.textRect.height / 2

    def draw(self, plane):
        plane.blit(self.txt, self.textRect)


# Button er en utvidelse av Label med en bakgrunn og input-handling
class Button(Label):
    def __init__(self, text, pos, size, bevel, type=None):

        super().__init__(text, pos, size)

        self.type = type
        self.bevel = bevel

        #hentes fra Label
        self.textRect.width += 20
        self.textRect.height += 20
        self.bgColor = settings.colors["UI"]
        self.txtColor = settings.colors["HP"]

    def draw(self, plane):
        py.draw.rect(plane, self.bgColor, py.rect.Rect(self.textRect.x - 10, self.textRect.y - 10, self.textRect.width, self.textRect.height), 0, self.bevel)
        super().draw(plane)

    def inputHandler(self, mousepos):

        if (self.textRect.x - 10 < mousepos[0] < self.textRect.x + self.textRect.width) and (
                self.textRect.y - 10 < mousepos[1] < self.textRect.y + self.textRect.height):
            self.bgColor = settings.colors["HP"]
            self.txtColor = settings.colors["UI"]
            if py.mouse.get_pressed()[0]:
                buttonSound = py.mixer.Sound(f"playerAudio/button.wav")
                py.mixer.Sound.play(buttonSound)
                match self.type:
                    case "FPSup":
                        settings.FPS += 1
                        return True
                    case "FPSdown":
                        settings.FPS -= 1
                        return True
                    case "mousemove": settings.respondToMouse *= -1
                    case "bg": settings.background *= -1
                    case "back": return True
                    case "start": return True
                    case "wipe": return True
        else:
            self.bgColor = settings.colors["UI"]
            self.txtColor = settings.colors["HP"]

        #hentes fra label
        self.txt = self.font.render(str(self.text), True, self.txtColor)

    def update(self, plane, mousepos):
        self.draw(plane)
        super().draw(plane)
        self.inputHandler(mousepos)


#https://www.figma.com/file/LZvW7dB3kNMN1cAMkhsagK/Welcome-to-FigJam?type=whiteboard&node-id=0%3A1&t=ltU1Sqb2Di6CHko0-1
#   c8nwfjxp
