from nltk import *
from nltk.tokenize import WhitespaceTokenizer
Wstknzr = WhitespaceTokenizer()
song = """
Ramos's fight, he was whipping vines,
swinging all through Coumarine
Lumiose's flashing lights,
grounded Clemont's electric types

Wulfric's Abomasnow,
whole team left me feeling cold,
TM13 for me to hold
This journey's the one thing I know

And I feel strong in this fight
mega evolving
And I love watching these lights
with you here beside me

Can't get enough, get enough, get enough
Things that fail to kill me make me level up

You know I've been, I've been losing sleep,
dreaming of Kalos and its new cities
Chaining shinies, looking for those stars
and no more counting EVs, we're Super Training hard

You know I've been, I've been losing sleep,
dreaming of Kalos and its new cities
Chaining shinies, looking for those stars
and no more counting EVs, we're Super Training hard

I feel this love from Valerie,
fairy types, so new to me
Big doll house, teleporting,
blinded by a Dazzling Gleam

Oh Olympia,
gym felt like another world
Psychic Badge is in my palm
TM04, my Mind is Calm

And I am feeling you crawl
in your Infestation
And I am feeling so strong
crushing Grant's Tyrunt

Can't get enough, get enough, get enough
Things that fail to kill me make me level up

You know I've been, I've been losing sleep,
dreaming of Kalos and its new cities
Chaining shinies, looking for those stars
and no more counting EVs, we're Super Training hard

You know I've been, I've been losing sleep,
dreaming of Kalos and its new cities
Chaining shinies, looking for those stars
and no more counting EVs, we're Super Training hard

League was easy, Team Flare burnt
Take a look at all the badges I've earned
League was easy, Team Flare burnt
Take a look at all the badges I've earned
League was easy, Team Flare burnt
Take a look at all the badges I've earned

Things that fail to kill me make me level up

You know I've been, I've been losing sleep,
dreaming of Kalos and its new cities
Chaining shinies, looking for those stars
and no more counting EVs, we're Super Training hard

You know I've been, I've been losing sleep,
dreaming of Kalos and its new cities
Chaining shinies, looking for those stars
and no more counting EVs, we're Super Training hard
"""

lines = song.split("\n")
tokens = []
for i in lines:
    if i.split() != []:
        tokens += [i.split()]
for i in tokens:
    print(i)
