from nltk import *
from collections import *
import string, re
import itertools
from random import *

song = open('song.txt', 'r').read()
markov = {}
level = 2

lines = song.split("\n")
tokens = []


for i in lines:              #generate list of words
    if i.split() != []:
        tokens += i.split()
        

def makeStrAlphanumeric(inp):
    return re.sub(r'[a-zA-Z ]+', '', inp)

def makeListAlphanumeric(inp):
    return map((lambda x: makeStrAlphanumeric(x), inp))

def makemarkov(tokens, level):
    markov = {}
    for index, word in enumerate(tokens):
        if index < level:
            continue;
        else:
            toenter = tokens[index-level:index]
            toenter = tuple(toenter)
            if markov.get(toenter, False):
                markov[toenter][word] += 1
            else:
                markov[toenter] = Counter()
                markov[toenter][word] += 1
    return markov

        
markov = makemarkov(tokens, level)


def getRandomItemInCounter(markov, word):
    i = randrange(sum(markov[word].values()))
    return next(itertools.islice(markov[word].elements(), i, None))

def getRandomItemInDict(markov):
    return choice(list(markov.keys()))

def getText(length):
    result = ""
    startWordIndex = randint(0, len(tokens)-level)
    currstate = []
    for i in range(level):
        currstate += [tokens[startWordIndex + i]]
    for i in range(0, length):
        currstate += [getRandomItemInCounter(markov, tuple(currstate))]
        currstate = currstate[1:]
              
        result += currstate[0] + " "
    return result

print(getText(1000))

    
