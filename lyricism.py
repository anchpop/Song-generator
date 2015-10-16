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
        

def makeStrAlphanumeric(inp):
    return re.sub(r'[a-zA-Z ]+', '', inp)

def makeListAlphanumeric(inp):
    return map((lambda x: makeStrAlphanumeric(x), inp))

def makemarkov(tokens, level):                            #generates a dictionary in the style of {tuple: Counter} 
    markov = {}                                           #where tuple is the current state and the counter is the words that the state follows
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

print(getText(1000))

    
