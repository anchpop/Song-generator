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


for i in lines:                                           #generate list of words
    if i.split() != []:
        tokens += i.split()
        
def list_range(offset, length, l):
    # this handles both negative offsets and offsets larger than list length
    start = offset % len(l)
    end = (start + length) % len(l)
    if end > start:
        return l[start:end]
    return l[start:] + l[:end]


def makeStrAlphanumeric(inp):
    return re.sub(r'[a-zA-Z ]+', '', inp)

def makeListAlphanumeric(inp):
    return map(makeStrAlphanumeric, inp)

def makemarkov(tokens, level):                            #generates a dictionary in the style of {tuple: Counter} 
    markov = {}                                           #where tuple is the current state and the counter is the words that the state follows
    for index in range(len(tokens)):
        endIndex = (index+level)
        word = tokens[endIndex % len(tokens)]
        toenter = list_range(index, level, tokens)
        toenter = tuple(toenter)
        if markov.get(toenter, False):
            markov[toenter][word] += 1
        else:
            markov[toenter] = Counter()
            markov[toenter][word] += 1
        
    return markov

        
markov = makemarkov(tokens, level)


def getRandomItemInCounter(markov, state):                #takes a state in the chain and gives you a random word that can come after it
    i = randrange(sum(markov[state].values()))
    return next(itertools.islice(markov[state].elements(), i, None))

def getRandomItemInDict(markov, level):                   #gives a ranom possible state
    startWordIndex = randint(0, len(tokens)-level)
    state = []
    for i in range(level):
        state += [tokens[startWordIndex + i]]
    return state

def getText(length):
    result = ""
    currstate = getRandomItemInDict(markov, level)
    for i in range(0, length):
        currstate += [getRandomItemInCounter(markov, tuple(currstate))]
        currstate = currstate[1:]
        result += currstate[0] + " "
    return result

print(getText(100))


def rhyme(inp, level):
     entries = corpus.cmudict.entries()
     syllables = [(word, syl) for word, syl in entries if word == inp]
     rhymes = []
     for (word, syllable) in syllables:
             rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
     return set(rhymes)

#print(rhyme('kettle', 1))
