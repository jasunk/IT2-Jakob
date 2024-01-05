

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

saker = [
    "Stoppe oljeutvinning","Drepe ulver","Privat-skoler","Høyere skatt", "Flere sykehus",
    "Fjerne bompenger", "Obligatorisk legobygging i skolen","statskirke", "eksamen i skolen", "dødsstraff"
]

fjompePartiet = Parti(
    navn="fjompepartiet",
    forkortelse="FP",
    medlemmer = ["Frank Fisk", "Kurt DårligForholdMedKonen"],
    saker = [[0, False], [1, True],[2, True],[3, False],[4,True],[5,True],[9, True]],
    stemmer = 23,
    enighet=0
)
partier = [fjompePartiet]
nåværende = fjompePartiet
print(f"Introduserer {nåværende.navn} syn på følgende saker:")
for partiSaker in nåværende.saker:
    stilling =""
    if partiSaker[1]:
        stilling = "for"
    elif not partiSaker[1]:
        stilling = "imot"

    #print(f"Til saken {saker[partiSaker[0]]} stiller {nåværende.forkortelse} seg {stilling}.")

egneSaker = []
for sak in saker:
    print(f"Hvordan stiller du deg til {sak}?")
    stilling = input("For (f) eller mot (m):    ")
    match stilling.lower():
        case "f":
            egneSaker.append([sak,True])
        case "m":
            egneSaker.append([sak,False])


for parti in partier:
    for psak in parti.saker:
        print(psak[1], egneSaker[psak[1]])
        if psak[1] == egneSaker[psak[0]]:
            print("YEE")