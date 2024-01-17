import random, copy
#_ = bakke
#1 = vegg
#2 = Exit
#3 = entrance
_ = 0

map1 = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,1],
    [1,_,_,1,1,_,_,_,_,1],
    [1,_,_,1,1,_,_,_,_,_],
    [1,_,_,_,_,_,_,_,_,_],
    [1,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,1],
    [1,1,1,1,1,1,1,1,1,1]
]

emptyMap = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]

]
squareMap = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,1,1,0,0,0,1,0],
    [0,1,0,0,0,1,1,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]

]
extMap = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,0,0,1,0,0,1,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,1,0,0,0,0,0,0,1,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,1,0,0,0,0,0,0,1,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,1,0,0,1,0,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]

]
dottedMap1 = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,0,0,0,0,0,1,0,0,1,0],
    [0,1,0,1,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,1,0,1,0],
    [0,1,0,0,1,0,1,0,0,0,1,0],
    [0,1,0,0,0,0,0,1,0,0,1,0],
    [0,1,0,1,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,1,0,0,0,1,0],
    [0,1,1,0,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]

]
dottedMap2 = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,0,0,0,0,0,0,1,0,1,0],
    [0,1,0,1,0,0,0,1,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,0,1,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,1,0,0,1,0],
    [0,1,0,0,1,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,1,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0]

]



def randomMap():

    return random.choice([emptyMap, extMap, squareMap, dottedMap1, dottedMap2])
def changeEntranceExit(map, ent, ext):

    tempMap = copy.deepcopy(map)

    if ent == "Right":
        for row in tempMap:
            row[len(row)-1]=3

        tempMap[5][10], tempMap[6][10] = 0, 0
    if ent == "Left":
        for row in tempMap:
            row[0]=3
        tempMap[5][1], tempMap[6][1] = 0, 0
    if ent == "Top":
        tempMap[0][5], tempMap[0][6] = 3,3
        tempMap[1][5], tempMap[1][6] = 0, 0
    if ent == "Bottom":
        tempMap[11][5], tempMap[11][6] = 2,2
        tempMap[10][5], tempMap[10][6] = 0, 0

    if ext == "Right":
        for row in tempMap:
            row[len(row)-1]=2
        tempMap[5][10], tempMap[6][10] = 0, 0
    if ext == "Left":
        for row in tempMap:
            row[0]=2
        tempMap[5][1], tempMap[6][1] = 0, 0
    if ext == "Top":
        tempMap[0][5], tempMap[0][6] = 2,2
        tempMap[1][5], tempMap[1][6] = 0, 0
    if ext == "Bottom":
        tempMap[11][5], tempMap[11][6] = 2,2
        tempMap[10][5], tempMap[10][6] = 0, 0


    for x in tempMap:
        print(x)
    print(ent, ext)

    return tempMap





def getOpposite(orig):
    ent=""

    match orig:
        case "Left":ent="Right"
        case "Right":ent="Left"
        case "Top":ent="Bottom"
        case "Bottom":ent="Top"
        case "None": ent = "None"
    return ent

def getRandomDir():
    return random.choice(["Right", "Left", "Top", "Bottom"])

lastExit = getRandomDir()


def nextRoom(index, player):
    global lastExit
    newExit = lastExit
    

    if not index in rooms:
        match getOpposite(lastExit):
            case "Right": player.rect.x, player.rect.y = 930, 500
            case "Left": player.rect.x, player.rect.y = 10, 500
            case "Top": player.rect.x, player.rect.y = 500, 10
            case "Bottom": player.rect.x, player.rect.y = 500, 930

        while newExit == getOpposite(lastExit) or newExit==lastExit:

            newExit = getRandomDir()

        print(index, getOpposite(lastExit), newExit)
        rooms[index]={"map":changeEntranceExit(randomMap(),getOpposite(lastExit),newExit)}
        lastExit = newExit
    else:
        match lastExit:
            case "Right": player.rect.x, player.rect.y = 110, 500
            case "Left": player.rect.x, player.rect.y = 890, 500
            case "Top": player.rect.x, player.rect.y = 500, 110
            case "Bottom": player.rect.x, player.rect.y = 500, 890



rooms = {
    1:{
        "map":changeEntranceExit(emptyMap,"Empty", lastExit)
    }

}
