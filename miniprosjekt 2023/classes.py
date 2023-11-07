import pygame as py
from pygame.locals import *
import random, settings

def splitSheet(sheet, imgSize, split, index, flip = 0):
    xSize = imgSize[0]/split[0]
    ySize = imgSize[1]/split[1]
    img = py.Surface((xSize,ySize), py.SRCALPHA)
    img.blit(sheet, (0,0), (xSize*(index[0]), ySize*(index[1]),xSize*(index[0]+1), ySize*(index[1]+1)))

    img = py.transform.scale(img,(xSize*3,ySize*3))
    img = py.transform.flip(img,flip, 0)
    return img


spriteType = {
    1:{
        "Idle":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Idle.png"), [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Attack1":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Attack1.png"), [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Attack2":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Attack2.png"), [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Death":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Death.png"), [256, 32], [8,1], [i, 0]) for i in range(8)],
        "Hurt":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Hurt.png"), [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Run":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Run.png"), [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Throw":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Throw.png"), [128, 32], [4,1], [i, 0]) for i in range(4)],
        "WalkAttack":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Walk+Attack.png"), [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Walk":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster_Walk.png"), [192, 32], [6,1], [i, 0]) for i in range(6)]
    },
    2:{
        "Idle":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Idle_4.png"), [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Attack1":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Attack1_4.png"), [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Attack2":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Attack2_6.png"), [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Death":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Death_8.png"), [256, 32], [8,1], [i, 0]) for i in range(8)],
        "Hurt":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Hurt_4.png"), [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Run":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Run_6.png"), [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Throw":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Throw_4.png"), [128, 32], [4,1], [i, 0]) for i in range(4)],
        "WalkAttack":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Walk+Attack_6.png"), [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Walk":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/2 Owlet_Monster/Owlet_Monster_Walk_6.png"), [192, 32], [6,1], [i, 0]) for i in range(6)]
    },
    3:{
        "Idle":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Idle_4.png"), [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Attack1":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Attack1_4.png"), [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Attack2":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Attack2_6.png"), [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Death":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Death_8.png"), [256, 32], [8,1], [i, 0]) for i in range(8)],
        "Hurt":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Hurt_4.png"), [128, 32], [4,1], [i, 0]) for i in range(4)],
        "Run":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Run_6.png"), [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Throw":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Throw_4.png"), [128, 32], [4,1], [i, 0]) for i in range(4)],
        "WalkAttack":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Walk+Attack_6.png"), [192, 32], [6,1], [i, 0]) for i in range(6)],
        "Walk":[splitSheet(py.image.load("sprites/free-pixel-art-tiny-hero-sprites/3 Dude_Monster/Dude_Monster_Walk_6.png"), [192, 32], [6,1], [i, 0]) for i in range(6)]
    }
}





class SpriteHandler():

    def __init__(self, spriteNum, player=False):
        self.spriteNum = spriteNum
        self.frame = 0
        self.counter = 0
        self.state = "Idle"
        self.player = player
        self.pos = [0,0]

    """
    Kan være:
    Attack1
    Attack2
    Death
    Hurt
    Idle
    Run
    WalkAttack
    Walk
    Throw
    """

    def setState(self, state):
        self.state = state

    def draw(self, plane):
        imageToDraw = spriteType[self.spriteNum][self.state][self.frame]
        #flip sprite
        if not self.player:
            self.pos = [550, settings.WH/2]
            imageToDraw = py.transform.flip(imageToDraw,1,0)
        else:
            self.pos = [350, settings.WH/2]

        plane.blit(imageToDraw, (self.pos[0], self.pos[1]))
    def update(self, plane):
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



        self.draw(plane)




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

    def useAbility(self, index):
        self.abilities[index].use()
        self.spriteHandler.frame = 0
        if 0 < self.abilities[index].damage <= 20:
            self.spriteHandler.setState("Attack1")
        if 20 < self.abilities[index].damage <= 100:
            self.spriteHandler.setState("Attack2")

    def heal(self, factor, randomness):
        print(f"{self.name} sin bønn ble besvart")
        print(factor)
        toHeal = factor +(random.randint(-1,1)*randomness)
        if self.currentHealth + toHeal>self.initHealth:
            self.currentHealth=self.initHealth
        else:
            self.currentHealth += toHeal
        print(self.currentHealth)

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
        if self.healthDisplay< self.currentHealth:
            self.healthDisplay+=1
        innerRect = py.rect.Rect(xPos+2, yPos+2, ((self.healthDisplay/self.initHealth)*400)-4, 14)


        py.draw.rect(surf, settings.colors["BG"], outerRect)
        py.draw.rect(surf, settings.colors["HP"], innerRect)

    def drawOptions(self, surf):
        backBox0 = py.rect.Rect(0,settings.WH-250,settings.WW, 250)
        backBox1 = py.rect.Rect(2,settings.WH-248,settings.WW-4, 246)
        backBox2 = py.rect.Rect(8,settings.WH-242,settings.WW-16, 242)
        py.draw.rect(surf, settings.colors["UI"], backBox0, 0, 10)
        py.draw.rect(surf, settings.colors["BG"], backBox1, 0, 10)
        py.draw.rect(surf, settings.colors["UI"], backBox2, 0, 10)

        xIncrease = 0
        yIncrease = 0

        for ability in self.abilities:
            font = py.font.Font('Pixelify_Sans/static/PixelifySans-Medium.ttf', 20)
            text = font.render(f"{ability.name} ({ability.damage} damage and {ability.healingFactor} healing)", True, settings.colors["TXT"])

            textRect = text.get_rect()
            textRect.x = 50 +xIncrease
            textRect.y = settings.WH/2+250 + yIncrease
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

        print(f"{self.name} blir angrepet")
        print(self.currentHealth)
        self.currentHealth-=damageToTake
        print(self.currentHealth)
        self.spriteHandler.frame = 0
        self.spriteHandler.setState("Hurt")
        if self.currentHealth<0:
            self.spriteHandler.setState("Death")



    def update(self, surf):
        if self.playable:
            self.drawOptions(surf)
        else:
            self.enemyInfo(surf)
        self.drawHealthBar(surf)


        self.spriteHandler.update(surf)




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
        if random.randrange(0,101)<self.successrate:
            print(f"Utfører {self.name}")
            if self.damage != 0:
                self.target.takeDamage(self.damage, self.critChance, self.randomness)
            if self.healingFactor != 0:
                self.character.heal(self.healingFactor, self.randomness)
        else:
            print(f"{self.name} feilet")



mann = PokerMann(
    "Jens",
    SpriteHandler(1,True),
    10,
    100,
    [],
    0,
    True
)
pikk = PokerMann(
    "Fjomperompe",
    SpriteHandler(2),
    4,
    100,
    [],
    0
)

mann.abilities = \
[
    Ability("Klor", mann, pikk, 10, 10, 2, 1, 80),
    Ability("Bønn", mann, pikk, 0, 0, 10, 1, 50, 50),
    Ability("SMÆKK", mann, pikk, 24, 50, 10, 1, 50),
    Ability("BOOM", mann, pikk, 100, 25, 2, 1, 10)
]

#mann.useAbility(random.randint(0,1))


