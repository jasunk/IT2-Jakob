def navnBaklengs(navn):
    #klarkjør en tom variabel for navn baklengs
    navnBak = ""

    #kjører en forloop baklengs, basert på navnets lengde
    for i in range(len(navn)-1,-1,-1):
        #legger til bokstaver i variabelen som skal returneres
        navnBak+= navn[i]
    return navnBak

#sjekker om input er vellykket
vellykketInput = False
while not vellykketInput:
    navn = input("Skriv navnet ditt:    ")
    navnBak = input("Skriv navnet ditt baklengs:    ")

    #test for å sjekke for rett variabeltype
    try:
        navn = str(navn)
        navnBak = str(navnBak)
        vellykketInput=True
    except ValueError:
        print("Krever input av type STRING")

    #sjekker om brukerinput er likt til navnBaklengs() sitt svar
    if navnBaklengs(navn).lower() == navnBak.lower():
        print("Riktig!!")
    else:
        print("Du stavet navnet ditt feil, prøv igjen!")
        #programet kjøres på nytt ved feil input, så variabelen gjenbrukes (mulig uoversiktlig men jaja)
        vellykketInput=False