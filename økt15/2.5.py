#SteinSaks Papir
import random as r

trekk = {
    1:"Stein",
    2:"Saks",
    3:"Papir"
}
print("Velkommen te stein saks papir")
score = 0
aiScore = 0
def runde():
    global score, aiScore
    print()
    print(f"Du har {score} poeng, motstander har {aiScore} poeng")
    print()
    ai_valg = r.randint(1,3)
    p_valg = input("Stein(1), Saks(2) eller Papir(3)?:    ")
    match p_valg:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case _:
            print("Feil i input, prøv på nytt")
            runde()
    if int(p_valg) == int(ai_valg):
        print("Seier mann")
        score+=1
    else:
        print("Du tapte as, huffda")
        aiScore+=1
    runde()
runde()
