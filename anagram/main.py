# Gabriel Crozier, anagram assignment for the raid


import random
name = input("What's your name:\n").lower()

name1 = [x for x in name]

nameList = []

for i in range(5):
    nameList.append(random.shuffle(name1))
    print(nameList[-1])