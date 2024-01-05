def oppgave1():
    handlekurv = {
        "melk": 17.90,
        "smør": 38.90,
        "kokt skinke": 23.10,
        "sjokolade": 11.90,
        "oppvaskmiddel": 24.40,
        "frossenpizza": 29.90 }

    laveste=100
    lavesteInd = 0
    høyeste = 0
    høyesteInd=0
    tilSammen = 0
    for vare in handlekurv.items():
        tilSammen+=vare[1]
        if vare[1] < laveste:
            laveste = vare[1]
            lavesteInd = list(handlekurv.values()).index(vare[1])
        if vare[1] > høyeste:
            høyeste=vare[1]
            høyesteInd = list(handlekurv.values()).index(vare[1])
    print(f"Den lavest prisede varen er {list(handlekurv.keys())[lavesteInd]}, til {laveste} kr")
    print(f"Den høyest prisede varen er {list(handlekurv.keys())[høyesteInd]}, til {høyeste} kr")
    print(f"Summen av alt på listen er {tilSammen:.2f} kr")
    main()

def oppgave2():
    byinfo = {
        "Oslo":1043168,
        "Bergen":265470,
        "Stavanger/Sandnes":229911,
        "Trondheim":191771,
        "Fredrikstad/Sarpsborg":117663,
        "Drammen":110236,
        "Porsgrunn/Skien":94102,
        "Kristiansand":64913,
        "Ålesund":54399,
        "Tønsberg":53818
    }
    validChoice=False
    while not validChoice:
        try:
            laveste = int(input("Velg laveste grense:    "))
            høyeste = int(input("Velg høyeste grense:    "))
            validChoice=True
        except ValueError:
            print("wallah, prøv på nytt")
    for by in byinfo.items():
        if laveste<by[1]<høyeste:
            print(by)
    main()

def oppgave3():
    personer = {   "Sophie": 18, "Noah": 18, "Olivia": 29, "Oscar": 21,   "Oliver": 25, "Sofia": 27, "Ella": 23, "Leah": 21,   "Lucas": 23, "Maya": 25, "Isaac": 29, "Axel": 27,    "Frida": 23, "Emil": 26, "Emma": 23, "Ingrid": 18,   "Phillip": 25, "Jacob": 24, "Nora": 21, "William": 22 }

    unikeAldre = {}
    for person in personer.items():
        if person[1] not in list(unikeAldre.values()):
            unikeAldre[person[0]] = person[1]
    print(unikeAldre)
    main()

def oppave4():
    dna = "GCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACAGC"


    DNAtoRNA = {
        "A":"U",
        "T":"A",
        "C":"G",
        "G":"C"
    }

    rnaString=""
    for bokstav in dna:
        rnaString+=DNAtoRNA[bokstav]
    print(rnaString)

    kodontabell = {     "UUU": "Fenylalanin", "CUU": "Leucin",          "AUU": "Isoleucin",   "GUU": "Valin",            "UUC": "Fenylalanin", "CUC": "Leucin",      "AUC": "Isoleucin",   "GUC": "Valin",           "UUA": "Leucin",      "CUA": "Leucin",           "AUA": "Metionin",    "GUA": "Valin",     "UUG": "Leucin",      "CUG": "Leucin",          "AUG": "Metionin",    "GUG": "Valin",            "UCU": "Serin",       "CCU": "Prolin",      "ACU": "Treonin",     "GCU": "Alanin",          "UCC": "Serin",       "CCC": "Prolin",           "ACC": "Treonin",     "GCC": "Alanin",     "UCA": "Serin",       "CCA": "Prolin",    "ACA": "Treonin",     "GCA": "Alanin",           "UCG": "Serin",       "CCG": "Prolin",      "ACG": "Treonin",     "GCG": "Alanin",          "UAU": "Tyrosin",     "CAU": "Histidin",         "AAU": "Asparagin",   "GAU": "Asparaginsyre",     "UAC": "Tyrosin",     "CAC": "Histidin",        "AAC": "Asparagin",   "GAC": "Asparaginsyre",
                          "UAA": "Stopp",       "CAA": "Glutamin",    "AAA": "Lysin",       "GAA": "Glutaminsyre",    "UAG": "Stopp",       "CAG": "Glutamin",         "AAG": "Lysin",       "GAG": "Glutaminsyre",     "UGU": "Cystein",     "CGU": "Arginin",         "AGU": "Serin",       "GGU": "Glycin",           "UGC": "Cystein",     "CGC": "Arginin",     "AGC": "Serin",       "GGC": "Glycin",          "UGA": "Stopp",       "CGA": "Arginin",          "AGA": "Arginin",     "GGA": "Glycin",     "UGG": "Tryptofan",   "CGG": "Arginin",        "AGG": "Arginin",     "GGG": "Glycin"  }
    nåværendeSyre = ""
    syreStruktur = []
    skalLeggetil=True
    for bokstav in rnaString:
        if len(nåværendeSyre) <3:
            nåværendeSyre+=bokstav
        else:
            if kodontabell[nåværendeSyre]=="Stopp":
                skalLeggetil=False
            if skalLeggetil:
                syreStruktur.append(kodontabell[nåværendeSyre])
            nåværendeSyre=""
    print(syreStruktur)





    main()


def main():
    print("")
    validChoice=False

    while not validChoice:
        oppgaveValg = input("Velg oppgave (skriv tall): ")
        try:
            oppgaveValg = int(oppgaveValg)
            validChoice = True
        except ValueError:
            print("Invalid svar, prøv igjen")

    print("")
    match oppgaveValg:
        case 1:
            oppgave1()
        case 2:
            oppgave2()
        case 3:
            oppgave3()
        case 4:
            oppave4()

        case _:
            print("Oppgave finnes ikke, velg nytt tall")
            main()



main()