import json
import random as r


#åpner fil
file = open("countries.json")

landData = json.load(file)

#setter grunnscore til 0
score = 0
avgAccuracy = 0
#main game loop
def newGame():
    #henter noen variabler som ikke skal nullstilles hver runde
    global score, avgAccuracy
    #skaffer en tilfeldig index innen rangen i datasettet
    randIndex = r.randint(0,len(landData)-1)
    #definerer antall forsøk for spiller
    tries=3

    #finner svar (for loop for flertallige korrekte svar)
    answerStrings= []
    for svar in landData[randIndex]['capital']:
        answerStrings.append(svar.lower())

    #kjører når man ikke er tom for forsøk
    while tries>0:
        print()
        print(f"Current score: {score} and your current average correctness is {avgAccuracy:.2f} %")
        print(f"What is the capital of {landData[randIndex]['name']['common']}?")
        print(f"You have {tries} tries")
        answer = input("Answer:     ")
        correctLetters = 0

        #sjekker hvor mange bokstaver er rett og regner ut accuracy (litt sloppy metode men jaja)
        for letter in answer:
            if letter in answerStrings[0]:
                correctLetters +=1

        avgAccuracy =( avgAccuracy + correctLetters/len(answerStrings[0])*100)/2

        #print(f"Your answer was {correctLetters/len(answerString)*100:.2f} ish % correct")

        #win og lose conditions her
        if answer.lower() in answerStrings :
            print()
            print("YESLADS, U WON")
            score+=1

            newGame()

        if correctLetters/len(answerStrings[0])*100 >=75:
            print()
            print(f"Close enough, the answer was {answerStrings}")
            print()
            score+=1
            newGame()

        else:
            print()
            print("Nah, try again")

            if tries==1:
                print(f"The answer was {answerStrings}")
            tries-=1
    #om du er tom for forsøk, tilbakemelding og restart
    else:
        print("U suck")

        newGame()

newGame()

file.close()