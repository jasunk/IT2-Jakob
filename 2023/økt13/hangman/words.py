import random as r
class Word():
    def __init__(self, word):
        self.word = word
        self.length = len(word)

words=[
    "Panda", "Papir", "And", "Katt", "Anus", "Kake", "Fjompenisse", "Lompe", "Klump", "Kebab", "Ris", "Diskotek", "Tiss", "Eirik", "Seigmenn"
]

wordObj = []
for word in words:

    wordObj.append(Word(word))

def randomWord():
    return wordObj[r.randint(0,len(wordObj)-1)]


