from nltk import *
from collections import *
import itertools
import random

song = open('song.txt', 'r').read()
markov = {}

lines = song.split("\n")
tokens = []
for i in lines:
    if i.split() != []:
        tokens += [i.split()]
for line in tokens:
    for wordnum, word in enumerate(line):
        if wordnum == 0:
            if markov.get('\n', False):
                markov['\n'][word] += 1
            else:
                markov['\n'] = Counter()
                markov['\n'][word] += 1
        if (wordnum + 1) < len(line):
            if markov.get(word, False):
                markov[word][line[wordnum+1]] += 1
            else:
                markov[word] = Counter()
                markov[word][line[wordnum+1]] += 1
        else:
            if markov.get(word, False):
                markov[word]['\n'] += 1
            else:
                markov[word] = Counter()
                markov[word]['\n'] += 1

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
    
