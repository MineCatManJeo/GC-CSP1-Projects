# Gabriel Crozier, anagram assignment for the raid

# imports random
import random

# Variables
name = input("What's your name:\n").lower()
name1 = [x for x in name]
nameList = []

# Little thing to make view easier
print('')

# Shuffels the characters in the name around
for i in range(5):
    random.shuffle(name1) # Shuffles the origional list
    listVar = name1 # Assigns the new value to a variable
    nameList.append(listVar) # Appends this to a list
    print(''.join(nameList[-1]).title()) # Prints the full word
