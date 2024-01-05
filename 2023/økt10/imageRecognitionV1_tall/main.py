from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
from PIL import Image
import numpy as np


from collections import Counter

#Åpner bilde, omgjør det til array med piksler (png gir 4 verdier for rgb, jpg gir 3)
#lage gjennkjenning av filtype+
i = Image.open("bilder/birk.jpg")
iar = np.array(i)



#henter inn eksempler fra "læringsett"
def createExamples():
    #lager meg en ny fil med navn eksempler, og skal fylle den med pikselverdier for hvert tall
    numberArrayExamples = open('eksempler.txt','a')
    numbersWeHave = range(1,10)
    for eachNum in numbersWeHave:

        for furtherNum in numbersWeHave:
            #lenke til bilde

            #henter bilde, legger i var
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(furtherNum)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())

            #skriver inn i filen på dette viset:
            #tall :: [array med pikselverdier],  eksempler:
            #0 :: [255,255,255, ........]
            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)


#funskjon som gjør fargede bilder binære med svart og hvitt, basert på average fargeverdier
def grenser(imageArray):
    balanceAr = []
    newAr = imageArray

    #sjekker alt (uten om gjennomsiktighet, derav [:3]) og finner avg farge
    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)

    balance = mean(balanceAr)
    #sjekker hver piksel og ser om fargen er over eller under grensen, og ut i fra det gjør den svart eller hvit
    for eachRow in newAr:
        for eachPix in eachRow:

            if mean(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr



#Sammenlikner med funnede verdier
def whatNumIsThis(filePath):

    #Legger til navn på hver verdi som har en piksel som matcher, skal se hva som treffer best til slutt
    matchedAr = []

    #henter, omgjør til array og splitter data fra tidligere laget fil
    loadExamps = open('eksempler.txt','r').read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    eksempelTeller = 0
    for eachExample in loadExamps:
        print(f"{eksempelTeller/len(loadExamps)*100:.2f}% beregnet")
        try:
            #henter ut nåværende tall lest fra treningssett og arrayen som tilhører
            splitted  = eachExample.split('::')
            currentNum = splitted[0]
            currentAr = splitted[1]

            eachPixEx = currentAr.split('],')
            eachPixInQ = inQuestion.split('],')

            x = 0
            eksempelTeller+=1
            #for hver verdi som er lik, legges navn på tall til i array
            while x < len(eachPixEx):

                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))


                x+=1

        except Exception as e:
            l = (str(e))


    #sjekker hvilket tall som passer best, (flest utslag)
    #print(matchedAr)
    print("100% beregnet")
    print()
    x = Counter(matchedAr)
    print(x)
    print(f"Eg tror lowkey highkey at tallet du skrev er {x.most_common()[0][0]}")


createExamples()
whatNumIsThis('bilder/test.png')

