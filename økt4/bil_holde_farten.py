#variabel for å kontrollere om program skal kjøres på nytt
ønskerÅKjøre =True


def speedFromTime(dist, tid):
    #kan bare returnere her, siden jeg sjekker for valueErrors i main()
    return (dist/tid)


def speedCheck(hastighet):
    #sjekker om hastighet er over 80 km/t, og returnerer en formatert streng med ekstra info
    if hastighet*3.6 > 80:
        return f"{(hastighet*3.6)-80:.2f} km/h over fartsgrensen"
    else:
        return f"{80-(hastighet*3.6):.2f} km/h under fartsgrensen"

def main():
    #henter inn variabel slik at den er innen funskjonens "scope"
    global ønskerÅKjøre

    #variabel for å se om input har vært vellykket
    confirmedInput = False

    while not confirmedInput:
        distanse = input("Distanse: ")
        tid = input("Tid:   ")
        registNum = input("Registreringsnummer: ")

        #tester om input er av riktig variabeltype, lar bruker prøve igjen om feil
        try:
            distanse = int(distanse)
            tid = int(tid)
            confirmedInput = True
        except ValueError:
            print("Feil i input-type, krever type INTEGER")

    #printer ut en streng med info om bil
    print(f"Bilen under registreringsnummeret {registNum} "
          f"kjørte {speedFromTime(distanse,tid):.2f} m/s, noe som er "
          f"{speedCheck(speedFromTime(distanse, tid))}")

    #sjekker om bruker vil kjøre igjen, standard-verdien _(alt annet enn N) kjører programmet på nytt
    kjørIgjen = input("Ønsker du å kjøre programmet igjen? (Y/N)    ").lower()
    match kjørIgjen:
        case "n":
            ønskerÅKjøre=False
        case _:
            print("inputFeil, kjører programmet igjen")


#sjekker om program skal kjøres igjen, sier "adios" om ikke
while ønskerÅKjøre:
    main()
else:
    print("adios")