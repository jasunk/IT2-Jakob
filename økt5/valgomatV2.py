import pygame as py
import sys
from pygame.locals import *

py.init()

window_width=500
window_height = 500

FPS = 60
FramePerSec = py.time.Clock()

gameSurf = py.display.set_mode((window_width,window_height))

font = py.font.Font('freesansbold.ttf', 32)

titleText = font.render('Jasunks valgomat', True, "white")
font = py.font.Font('freesansbold.ttf', 16)

# light shade of the button
color_light = (170,170,170)

# dark shade of the button
color_dark = (100,100,100)

buttonFont = py.font.Font("freesansbold.ttf", 14)

class Parti:

    def __init__(self, navn, forkortelse, medlemmer, saker,stemmer, enighet):
        self.navn = navn
        self.forkortelse = forkortelse
        self.medlemmer = medlemmer
        self.saker = saker
        self.stemmer = stemmer
        self.enighet = enighet

    def leggTilMedlem(self,medlem):
        self.medlemmer.append(medlem)

    def leggTilSak(self,sak):
        self.saker.append(sak)

    def leggTilStemmer(self,antal):
        self.stemmer += antal
    def leggTilEnighet(self,antal):
        self.enighet+=antal

saker = [
    "Stoppe oljeutvinning","Drepe ulver","Privat-skoler","Høyere skatt", "Flere sykehus",
    "Fjerne bompenger", "Obligatorisk legobygging i skolen","statskirke", "eksamen i skolen", "dødsstraff"
]

fjompePartiet = Parti(
    navn="fjompepartiet",
    forkortelse="FP",
    medlemmer = ["Frank Fisk", "Kurt DårligForholdMedKonen"],
    saker = [[0, False], [1, True],[2, True],[3, False],[4,True],[5,True],[9, False], [6,True]],
    stemmer = 23,
    enighet=0
)
haterAltOgAllePartiet = Parti(
    navn="haterAltOgAllePartiet",
    forkortelse="HAOAP",
    medlemmer=["Kurt-Ivar Krungsnes", "Rolf-Rune Hvitmannsætt"],
    saker = [[0,False],[1,True],[3,False],[6,False],[7,True],[9,True]],
    stemmer=3,
    enighet=0
)


partier = [fjompePartiet, haterAltOgAllePartiet]
nåværende = fjompePartiet

#print(f"Introduserer {nåværende.navn} syn på følgende saker:")
for partiSaker in nåværende.saker:
    stilling =""
    if partiSaker[1]:
        stilling = "for"
    elif not partiSaker[1]:
        stilling = "imot"

    #print(f"Til saken {saker[partiSaker[0]]} stiller {nåværende.forkortelse} seg {stilling}.")

egneSaker = []
spørsmålDisp = font.render('', True, "white")
def forImot():
    global egneSaker, spørsmålDisp, gameSurf
    for sak in saker:
        spørsmålDisp = font.render(f"Hvordan stiller du deg til å {sak}?", True, "white")
        print(f"Hvordan stiller du deg til å {sak}?")
        stilling = input("For (f) eller mot (m):    ")
        match stilling.lower():
            case "f":
                egneSaker.append([sak,True])
            case "m":
                egneSaker.append([sak,False])

qstNm = 0
def nyttSpørsmål(index):
    global gamesurf, spørsmålDisp, egneSaker, qstNm, font


    if qstNm ==6:
        font = py.font.Font('freesansbold.ttf', 13)
    else:
        font = py.font.Font('freesansbold.ttf', 16)
        spørsmålDisp = saker[index]
    return (font.render(f"Hvordan stiller du deg til {saker[index]}", True, "white"))

harSjekket = False
enighetsProsenter = []
def sjekkEnighet():
    global egneSaker, harSjekket, prevString, enighetsProsenter
    if not len(enighetsProsenter) == len(partier):
        for parti in partier:
            for psak in parti.saker:
                if psak[1] == egneSaker[psak[1]][1]:
                    parti.leggTilEnighet(1)

            print("Du er "+ str(round(parti.enighet/len(parti.saker)*100,2)) +"% enig med "+parti.navn)
            font = py.font.Font('freesansbold.ttf', 16)
            harSjekket=True
            enighetsProsenter.append(font.render("Du er "+ str(round(parti.enighet/len(parti.saker)*100,2)) +"% enig med "+parti.navn, True, "white"))








while True:

    mouse = py.mouse.get_pos()
    gameSurf.fill("black")
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if 100 <= mouse[0] <= 200 and 200 <= mouse[1] <= 250:
                egneSaker.append([spørsmålDisp,True])
                if qstNm < len(saker)-1:
                    qstNm+=1
                else:
                    sjekkEnighet()
            if 300 <= mouse[0] <= 400 and 200 <= mouse[1] <= 250:
                egneSaker.append([spørsmålDisp,False])
                if qstNm < len(saker)-1:
                    qstNm+=1
                else:
                    sjekkEnighet()




    if 100 <= mouse[0] <= 200 and 200 <= mouse[1] <= 250:
        py.draw.rect(gameSurf,color_light,[100,200,100,50])

    else:
        py.draw.rect(gameSurf,"green",[100,200,100,50])
    if 300 <= mouse[0] <= 400 and 200 <= mouse[1] <= 250:
        py.draw.rect(gameSurf,color_light,[300,200,100,50])

    else:
        py.draw.rect(gameSurf,"red",[300,200,100,50])

    gameSurf.blit(nyttSpørsmål(qstNm),(70,100))
    gameSurf.blit(titleText,(100,20))

    gameSurf.blit(buttonFont.render("For",True,"black") , (138,220))
    gameSurf.blit(buttonFont.render("Imot",True,"white") , (338,220))

    res_y=400
    for resultat in enighetsProsenter:
        gameSurf.blit(resultat,(110, res_y))
        res_y+=40

    FramePerSec.tick(FPS)
    py.display.update()

