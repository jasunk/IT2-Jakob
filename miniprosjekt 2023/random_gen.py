import saves, settings, classes, random
enemyPool = [
    classes.Ability("Klæss", "self", "target", 3*saves.save_1["enemy"]["lvl"], 10, 2, "Attack1", 90),
    classes.Ability("KÆÆZING", "self", "target", 5*saves.save_1["enemy"]["lvl"], 10, 2, "Attack1", 80),
    classes.Ability("Mediter", "self", "target", 0, 0, 10, "Throw", 65, 10*saves.save_1["enemy"]["lvl"]),
    classes.Ability("Ur mom joke", "self", "target", 15*saves.save_1["player"]["lvl"], 10, 2, "Throw", 65),
    classes.Ability("SMÆKK SMÆKK", "self", "target", 5*saves.save_1["enemy"]["lvl"], 50, 10, "Attack2", 75),
    classes.Ability("YEET", "self", "target", 50+5*saves.save_1["enemy"]["lvl"], 25, 2, "Throw", 10)
]
playerPool = [
    classes.Ability("Klæss", "self", "target", 3*saves.save_1["player"]["lvl"], 10, 2, "Attack1", 90),
    classes.Ability("KÆÆZING", "self", "target", 5*saves.save_1["player"]["lvl"], 10, 2, "Attack1", 80),
    classes.Ability("Ur mom joke", "self", "target", 15*saves.save_1["player"]["lvl"], 10, 2, "Throw", 65),
    classes.Ability("Mediter", "self", "target", 0, 0, 10, "Throw", 65, 10*saves.save_1["player"]["lvl"]),
    classes.Ability("SMÆKK SMÆKK", "self", "target", 5*saves.save_1["player"]["lvl"], 50, 10, "Attack2", 75),
    classes.Ability("YEET", "self", "target", 50+5*saves.save_1["player"]["lvl"], 25, 2, "Throw", 10)
]

names = ["Jens", "Jomar", "Fjomp", "Gelemaur", "Slump", "Fis", "Fjomp", "Rassgutt", "MR Man", "Rasistikus", "Klump", "Bleknet nakenkatts haarstraa", "Ankelsluker"]

def createRandom(player=False):
    global enemyPool, playerPool
    sprite = random.randint(1,3)
    if player:
        level = saves.save_1["player"]["lvl"]+random.randint(-1,2)
        saves.save_1["player"]["sprite"]= sprite
        health = 23 + saves.save_1["player"]["lvl"]*5
    else:
        level =saves.save_1["enemy"]["lvl"]+random.randint(-1,2)
        saves.save_1["enemy"]["sprite"]= sprite
        health = 23 + saves.save_1["enemy"]["lvl"]*5

    char = classes.PokerMann(
        names[random.randint(0,len(names)-1)],
        classes.SpriteHandler(sprite,player),
        level,
        health,
        [],
        player
    )

    for i in range(4):
        if player:
            char.abilities.append(playerPool[random.randint(0, len(playerPool)-1)])
        else:
            char.abilities.append(enemyPool[random.randint(0, len(enemyPool)-1)])
    for a in char.abilities:
        a.playable = player
        a.character = char

    return char

def semiRandom(original, player=True):
    if player:
        level =saves.save_1["player"]["lvl"]
        health = 23 + saves.save_1["player"]["lvl"]*5
        sprite = saves.save_1["player"]["sprite"]
    else:
        level =saves.save_1["enemy"]["lvl"]
        health = 23 + saves.save_1["enemy"]["lvl"]*5
        sprite = saves.save_1["enemy"]["sprite"]
    if player:
        char = classes.PokerMann(
            original.name,
            classes.SpriteHandler(sprite, True, False),
            level,
            health,
            original.abilities,
            True
        )
    else:
        char = classes.PokerMann(
            original.name,
            classes.SpriteHandler(sprite, False, False),
            level,
            health,
            original.abilities,
            False
        )

    char.currentHealth = original.currentHealth + health/2
    if char.currentHealth>char.initHealth:
        char.currentHealth = char.initHealth

    for a in char.abilities:
        a.playable = player
        a.character = char


    return char

