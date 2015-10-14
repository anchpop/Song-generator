from nltk import *
from collections import *
import itertools
import random

song = open('song.txt', 'r').read()
markov = {}
level = 1

lines = song.split("\n")
tokens = []

def makemarkov(tokens, level):
    markov = {}
    for index, word in enumerate(tokens):
        if index < level:
            continue;
        else:
            toenter = tuple(tokens[index-level:index])
            if markov.get(toenter, False):
                markov[toenter][word] += 1
            else:
                markov[toenter] = Counter()
                markov[toenter][word] += 1
    return markov

for i in lines:
    if i.split() != []:
        tokens += [i.split()]
        
markov = makemarkov(tokens, level)


def getRandomItemInCounter(markov, word):
    i = random.randrange(sum(markov[word].values()))
    return next(itertools.islice(markov[word].elements(), i, None))

def getRandomItemInDict(markov):
    return random.choice(list(markov.keys()))

curr = getRandomItemInDict(markov)
print(curr)
for i in range(0, 1000):
    curr = getRandomItemInCounter(markov, curr)
    if curr == '\n':
        print('')
        curr = getRandomItemInCounter(markov, '\n')
        print(curr + " ", end="")
    else:
        print(curr + " ", end="")
    
