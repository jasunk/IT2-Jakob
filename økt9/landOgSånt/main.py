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
    global score, avgAccuracy
    randIndex = r.randint(0,len(landData)-1)
    tries=3
    answerStrings= []
    for svar in landData[randIndex]['capital']:
        answerStrings.append(svar.lower())


    while tries>0:
        print()
        print(f"Current score: {score} and your current average correctness is {avgAccuracy:.2f} %")
        print(f"What is the capital of {landData[randIndex]['name']['common']}?")
        print(f"You have {tries} tries")
        answer = input("Answer:     ")
        correctLetters = 0
        for letter in answer:
            if letter in answerStrings[0]:
                correctLetters +=1

        avgAccuracy =( avgAccuracy + correctLetters/len(answerStrings[0])*100)/2

        #print(f"Your answer was {correctLetters/len(answerString)*100:.2f} ish % correct")
        if answer.lower() in answerStrings :
            print()
            print("YESLADS, U WON")
            score+=1

            newGame()

        if correctLetters/len(answerStrings[0])*100 >=75:
            print()
            print(f"Close enough, the answer was {answerStrings} ")
            print()
            score+=1
            newGame()

        else:
            print()
            print("Nah, try again")

            if tries==1:
                print(f"The answer was {answerStrings}")
            tries-=1
    else:
        print("U suck")

        newGame()

newGame()

file.close()