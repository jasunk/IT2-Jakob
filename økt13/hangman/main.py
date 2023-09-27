import sys
import words as w
import pygame as py
from pygame.locals import *

py.init()
WW=1000
WH=500
gameSurf = py.display.set_mode((WW,WH))
spriteNum = 0

clock = py.time.Clock()

currentWord = w.randomWord()


base_font = py.font.Font(None, 32)


def checkForLetter(letter):
    indexOfLetter = []
    ownVerOfWord = list(currentWord.word.lower())

    shouldCheck = True
    indexAdd = 0

    while shouldCheck:
        try:
            indexOfLetter.append(int(ownVerOfWord.index((letter))+indexAdd))
            ownVerOfWord.pop(ownVerOfWord.index(letter))
            indexAdd+=1
        except ValueError:
            shouldCheck=False
    return indexOfLetter

def checkWord(word):
    if word.lower() == currentWord.word.lower():
        return True
    return False

knownLetters = ["" for letter in currentWord.word]


class letterPlace(py.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = py.image.load("sprites/Drawing-12.sketchpad.png")
        self.pos = [x,y]
class gameSprite(py.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = py.image.load(f"sprites/sprite{str(11-spriteNum)}.png")
        self.pos = (x,y)
    def draw(self):
        gameSurf.blit(self.image,(self.pos[0],self.pos[1]))

active = False
guessedLetters = []
state =""
while True:

    gameSurf.fill("beige")
    guessingString=""
    for letter in knownLetters:
        guessingString += letter
    if checkWord((guessingString)):
        gameSurf.fill("green")
        state="Yoooo du vant!"
    if state != "Yoooo du vant!" and state != "":
        gameSurf.fill("red")

    displaySprite = gameSprite(WW/2-200,-100)
    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            sys.exit()
        if e.type ==KEYDOWN:

            if checkForLetter(str(e.unicode)) and state=="":
                for ind in checkForLetter(str(e.unicode)):
                    knownLetters[ind] = str(e.unicode)

            elif spriteNum<10:
                guessedLetters.append(str(e.unicode))
                spriteNum+=1
                gameSurf.fill("red")
            else:
                state=f"Du tapte mann, ordet var {currentWord.word}"


    ordStreker = []
    ordXvals = []
    grense = (WW/3)*2
    x_pos=(WW-grense)/(currentWord.length)+(grense/2)
    toAddToX=0

    for i in range(0,currentWord.length):
        ordStreker.append(letterPlace(x_pos+toAddToX,400))
        ordXvals.append(x_pos+toAddToX)
        toAddToX+=50


    for strek in ordStreker:
        for known in knownLetters:

            bokstavToShow = base_font.render(known, True, (0, 0, 0))
            for index in checkForLetter(known):

                gameSurf.blit(bokstavToShow, (ordXvals[index]+15, 405))
        gameSurf.blit(strek.image,(strek.pos[0],strek.pos[1]))



    stringAvGjett=""
    for letter in guessedLetters:
        stringAvGjett += letter+", "

    guessedDisp = base_font.render(stringAvGjett, True, (0, 0, 0))
    gameSurf.blit(guessedDisp, (100, 225))

    condition = base_font.render(state, True, (0, 0, 0))

    gameSurf.blit(condition, (450, 300))

    tut = base_font.render("Skriv for å gjette", True, (0, 0, 0))

    gameSurf.blit(tut, (0, 475))

    displaySprite.draw()

    clock.tick(12)

    py.display.update()