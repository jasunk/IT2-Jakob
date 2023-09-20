import matplotlib.pyplot as plt
from statistics import mean
from PIL import Image
import numpy as np
from collections import Counter

def startTrening():
    stiDokument = open("stier.txt", "a")
    for i in range(1,3):
        for j in range(1,31):
            filSti = f"bilder/{i}.{j}.png"
            print(filSti)
            tempI = Image.open(filSti)
            tempIA = np.array(tempI)
            temapIATL = str(tempIA.tolist())

            linjeTilDok = str(i)+"::"+temapIATL + "\n"
            stiDokument.write(linjeTilDok)


def forenkle(bildeSti):
    i = Image.open(bildeSti)
    iar = np.array(i)

    gjennomsnittsFarge = []
    for rad in iar:
        for piksel in rad:
            gjennomsnittsTall = mean(piksel[:3])
            gjennomsnittsFarge.append(gjennomsnittsTall)
    grense = (mean(gjennomsnittsFarge))

    for rad in iar:
        for piksel in rad:
            if mean(piksel[:3]) > grense:
                piksel[0] = 255
                piksel[1] = 255
                piksel[2] = 255
                piksel[3] = 255
            else:
                piksel[0] = 0
                piksel[1] = 0
                piksel[2] = 0
                piksel[3] = 255
    return iar


def sammenlikne(fil):
    samsvarerMed = []
    lastTrening = open('stier.txt','r').read()
    lastTrening = lastTrening.split('\n')
    lastTrening[-1:].pop()


    i = forenkle(fil)
    iar = np.array(i)
    iarl = iar.tolist()

    nåværendeBilde = str(iarl)

    prosentmessigTall = 0

    for eksempel in lastTrening:
        if prosentmessigTall%2==0:
            print(f"{prosentmessigTall/len(lastTrening)*100:.2f}% prosessert :)")
        else:
            print(f"{prosentmessigTall/len(lastTrening)*100:.2f}% prosessert :(")
        try:

            splittetData = eksempel.split("::")
            vekt = splittetData[0]
            data = splittetData[1]


            hverEksempelPiksel = data.split('],')
            hverNåværendePiksel = nåværendeBilde.split('],')

            x = 0

            while x < len(hverEksempelPiksel):

                if hverEksempelPiksel[x] == hverNåværendePiksel[x]:

                    samsvarerMed.append(int(vekt))
                x+=1

            prosentmessigTall +=1
        except Exception as e:
            #print(e)
            l = e


    resultat = Counter(samsvarerMed)
    print(resultat)
    if resultat.most_common()[0][0] == 1:
        print("100% prossesert :)")
        print("Highkey et smilefjes as")
    if resultat.most_common()[0][0] == 2:
        print("100% prossesert :(")
        print("Lowkey et surt fjes as")



startTrening()
sammenlikne("test.png")


#FUNKER IKKE HELT AS
#MEN NÆRME OG LAGER FRA BUNNEN SELV
#PROGRESS LESS GO

#tror problemet er at den ser på pikselposisjon, og at smilefjes er større / mer sentrert i treningssettet (da enn leisegFjes)
