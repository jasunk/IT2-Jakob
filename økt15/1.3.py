import random
fornavn = ["Rolf", "Roger", "Jens", "Kornelius", "Frank", "Frans", "Eirik", "Jakob", "Rasmus", "Fredrik", "Albert"]
etternavn = ["Vindumann", "Krankel", "Jakobsen", "Aabrek", "Lunde", "White", "Gelemauren", "Fjompenisse", "Smith"]
domene = ["bergen.kommune.no","gmail.com","balleby.no","vestlandFylke.no","icloud.com"]

for i in range(0,10):
    fullstendigAdresse = f"{fornavn[random.randint(0,len(fornavn)-1)]}.{etternavn[random.randint(0,len(etternavn)-1)]}@{domene[random.randint(0,len(domene)-1)]}"
    print(fullstendigAdresse)