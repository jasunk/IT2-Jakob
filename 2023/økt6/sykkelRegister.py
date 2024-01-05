import sys
sykler = {}
rammenr = ["WBK0132K", "VE01562512D", "S5A001234", "WN17632Z", "TA78317B", "ME7265T"]

#henter input og flækker det inn i dict med rammenr som key
for nr in rammenr:
    navn = input(f"Eier av sykkel {nr} :  ")
    adresse = input(f"Addresse til sykkel {nr} :  ")
    sykler[nr] = [navn, adresse]

#Trenger ikke å sjekke for valid input ettersom vi gjør det senere
def sok_register(ramme):
    return sykler[ramme]

def main():
    #upper sånn at det ikke er case-sensitive
    rammeSok = input("Søk etter sykkelinfo med ramme:   ").upper()

    #Sjekker om rammenr du skrev er et av de som eksisterer, kjører main() på nytt om ikke
    if rammeSok in rammenr:
        sokEier,sokAdresse=sok_register(rammeSok)
    else:
        print("invalid ramme, prøv igjen")
        main()

    #Printer ut resultatet
    print(f"Sykkel med ramme {rammeSok} tilhører {sokEier} ved adresse {sokAdresse}")

    #Sjekker input (ikke case sensitive) for å se om programm kjøres på nytt
    #Kunne like gjerne brukt if elif else, men liker match kjører 86% kjappere !!
    #info om det her hehe https://tonybaloney.github.io/posts/python-match-statement.html
    kjorPaaNytt = input("Søke etter ny sykkel ? (Y/N):  ")
    match kjorPaaNytt.lower():
        #Kjører på nytt om svar er y (yes)
        case "y":
            main()
        #stopper scriptet om svar er n (no/nei)
        case "n":
            sys.exit()
        #standard-handlingen er å kjøre på nytt, for å ikke straffe skrivefeil
        case _:
            print("Invalid respons, kjører på nytt")
            main()

#init kjøring av main()
main()