import  settings, classes, random

#navneliste for tilfeldig genererte karakterer
names = ["Jens", "Jomar", "Fjomp", "Gelemaur", "Slump", "Fis", "Fjomp", "Rassgutt", "MR Man", "Rasistikus", "Klump", "Bleknet nakenkatts haarstraa", "Ankelsluker"]


playerAbilityNames = []
enemyAbilityNames = []

#håndterer HELT TILFELDIGE MONSTre
def createRandom(player=False):
    global playerAbilityNames, enemyAbilityNames

    #har abilitypools seperat, for å kunne legge til difficulty og for å kunne fjerne irriterende angrep fra motstander
    enemyPool = [
        classes.Ability("Klæss", "self", "target", 3+3* (settings.currentSave["enemy"]["lvl"]/3), 10, 2, "Attack1", 90),
        classes.Ability("KÆÆZING", "self", "target", 5+5*(settings.currentSave["enemy"]["lvl"]/3), 10, 2, "Attack1", 80),
        classes.Ability("Mediter", "self", "target", 0, 0, 10, "Throw2", 65, 10*settings.currentSave["enemy"]["lvl"]),
        classes.Ability("Yo mama joke", "self", "target", 10+15*(settings.currentSave["player"]["lvl"]/3), 10, 2, "Throw2", 65),
        classes.Ability("SMÆKK SMÆKK", "self", "target", 5+5*(settings.currentSave["enemy"]["lvl"]/3), 50, 10, "Attack2", 75),
        classes.Ability("YEET", "self", "target", 50+(5*settings.currentSave["enemy"]["lvl"]/3), 25, 2, "Throw", 10)
    ]
    playerPool = [
        classes.Ability("Klæss", "self", "target", 3+3*(settings.currentSave["player"]["lvl"]/3), 10, 2, "Attack1", 90),
        classes.Ability("KÆÆZING", "self", "target", 5+5*(settings.currentSave["player"]["lvl"]/3), 10, 2, "Attack1", 80),
        classes.Ability("Yo mama joke", "self", "target", 10+15*(settings.currentSave["player"]["lvl"]/3), 10, 2, "Throw2", 65),
        classes.Ability("Mediter", "self", "target", 0, 0, 10, "Throw2", 65, 10*settings.currentSave["player"]["lvl"]),
        classes.Ability("SMÆKK SMÆKK", "self", "target", 5+5*(settings.currentSave["player"]["lvl"]/3), 50, 10, "Attack2", 75),
        classes.Ability("YEET", "self", "target", 50+5*(settings.currentSave["player"]["lvl"]/3), 25, 2, "Throw", 10)
    ]

    #lager to arrays som håndterer navnene til abilities, brukes for å finne index i semirandom()
    playerAbilityNames = [playerPool[i].name for i in range(len(playerPool))]
    enemyAbilityNames = [enemyPool[i].name for i in range(len(enemyPool))]

    #velger tilfeldig spirte
    sprite = random.randint(1,3)

    #tilpasser variabler basert på lagret data i saves
    if player:
        level = settings.currentSave["player"]["lvl"]
        settings.currentSave["player"]["sprite"]= sprite
        health = 23 + settings.currentSave["player"]["lvl"]*5
    else:
        level =settings.currentSave["enemy"]["lvl"]
        settings.currentSave["enemy"]["sprite"]= sprite
        health = 23 + settings.currentSave["enemy"]["lvl"]*5

    #lager karakter
    char = classes.PokerMann(
        names[random.randint(0,len(names)-1)],
        classes.SpriteHandler(sprite,player),
        level,
        health,
        [],
        player
    )

    #legger til 4 abilities
    for i in range(4):
        index = random.randint(0, len(playerPool)-1)
        if player:
            char.abilities.append(playerPool[index])
        else:
            char.abilities.append(enemyPool[index])

    #oppdaterer verdier i abilities
    for a in char.abilities:
        a.playable = player
        a.character = char
        if not player:
            a.damage*=settings.currentSave["game"]["difficulty"]
        a.damage = round(a.damage,2)



    return char


#brukes for seirende monster, for å bevare navn, utseende og abilities
def semiRandom(original, player=True):
    #oppdaterer verdier (funker det?)
    enemyPool = [
        classes.Ability("Klæss", "self", "target", 3+3* (settings.currentSave["enemy"]["lvl"]/3), 10, 2, "Attack1", 90),
        classes.Ability("KÆÆZING", "self", "target", 5+5*(settings.currentSave["enemy"]["lvl"]/3), 10, 2, "Attack1", 80),
        classes.Ability("Mediter", "self", "target", 0, 0, 10, "Throw2", 65, 10*settings.currentSave["enemy"]["lvl"]),
        classes.Ability("Yo mama joke", "self", "target", 10+15*(settings.currentSave["player"]["lvl"]/3), 10, 2, "Throw2", 65),
        classes.Ability("SMÆKK SMÆKK", "self", "target", 5+5*(settings.currentSave["enemy"]["lvl"]/3), 50, 10, "Attack2", 75),
        classes.Ability("YEET", "self", "target", 50+(5*settings.currentSave["enemy"]["lvl"]/3), 25, 2, "Throw", 10)
    ]
    playerPool = [
        classes.Ability("Klæss", "self", "target", 3+3*(settings.currentSave["player"]["lvl"]/3), 10, 2, "Attack1", 90),
        classes.Ability("KÆÆZING", "self", "target", 5+5*(settings.currentSave["player"]["lvl"]/3), 10, 2, "Attack1", 80),
        classes.Ability("Yo mama joke", "self", "target", 10+15*(settings.currentSave["player"]["lvl"]/3), 10, 2, "Throw2", 65),
        classes.Ability("Mediter", "self", "target", 0, 0, 10, "Throw2", 65, 10*settings.currentSave["player"]["lvl"]),
        classes.Ability("SMÆKK SMÆKK", "self", "target", 5+5*(settings.currentSave["player"]["lvl"]/3), 50, 10, "Attack2", 75),
        classes.Ability("YEET", "self", "target", 50+5*(settings.currentSave["player"]["lvl"]/3), 25, 2, "Throw", 10)
    ]

    #velger variable basert på hvem som overlevde
    if player:
        level = settings.currentSave["player"]["lvl"]
        health = 23 + settings.currentSave["player"]["lvl"]*5
        sprite = settings.currentSave["player"]["sprite"]
    else:
        level = settings.currentSave["enemy"]["lvl"]
        health = 23 + settings.currentSave["enemy"]["lvl"]*5
        sprite = settings.currentSave["enemy"]["sprite"]


    char = classes.PokerMann(
        original.name,
        classes.SpriteHandler(sprite, player, False),
        level,
        health,
        original.abilities,
        player
    )

    #gir overlevende til bake mye helse
    char.currentHealth = original.currentHealth + health/1.5
    if char.currentHealth>char.initHealth:
        char.currentHealth = char.initHealth

    #oppdaterer abilitites
    for a in char.abilities:
        a.playable = player
        a.character = char
        if player:
            a = playerPool[playerAbilityNames.index(a.name)]
        else:
            a = enemyPool[enemyAbilityNames.index(a.name)]
            a.damage*=settings.currentSave["game"]["difficulty"]
        a.damage = round(a.damage,2)



    return char

