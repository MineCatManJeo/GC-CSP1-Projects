# Gabriel Crozier, Madlib Assignment

import random as rand

# Variables
name = input("Input a name:\n").capitalize()
pronoun = input("Input this persons pronouns (he/she):\n").lower()
verbA = input("Input a verb (ing something you can physically do):\n").lower()
noun = input("Input a noun:\n").lower()
verbB = input("Input a verb (ing something you can physically do):\n").lower()
color = input("Input a color:\n").lower()
emotion = input("Input an emotion:\n").lower()
place = input("Input a place:\n").title()

if pronoun.lower() == "he":
    pronoun1 = "his"
else:
    pronoun1 = "her"


vowels = ["a","e","i","o","u"]

the_noun = "the " + noun

if noun[0].lower() in vowels:
    a_noun = "an " + noun
else:
    a_noun = "a " + noun

# Sentences (not the best ones but yea)

liOSent = [f"One day while {name} was {verbA} {pronoun} encountered {a_noun}. After looking carefully at {the_noun} {pronoun} realized it was {verbB}. \
Soon after {pronoun} asked it for it's favorite color. It said it's favorite color was {color}. This made {name} feel really {emotion} \
and {pronoun} mailed {the_noun} to the {place}.",f"After a long and difficult day, {name} had enough. {pronoun.capitalize()} decided to begin {verbA} while waiting for \
{pronoun1} lovely {noun} to come home. Sadly that wouldn't happen as {pronoun} just got a call. It turns out {pronoun1} lovely {noun} had broken the law because it was {verbB}. After \
a long pause {name} felt {emotion}. {pronoun.capitalize()} immedietly ran across the {color} brick road to rescue {pronoun1} lovely {noun} from {place}!",f"The {color} palace \
was magnificant. {name} was the ruler of all and {pronoun1} biggest law prohibited {verbA}. Most of {pronoun1} citezens decided {pronoun} was a \
bad ruler because of how {emotion} {pronoun} was. They all decided to hold {noun}s and throw them at {name} to retaliate. {name} was so sad \
that {pronoun} was forced to be constantly {verbB} for the rest of {pronoun1} life."]

# Chooses a random one

print(liOSent[rand.randint(0,2)])
