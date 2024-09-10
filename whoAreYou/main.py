#Gabriel Crozier, Who are you

def complicate():
    stuff = input('Put your name (Last names and Middle names are allowed, allowed with spaces as well), age, and favorite color (One Word) with a space between each one down below:\n')
    stuff = stuff.split()
    if len(stuff[0:-2]) >= 2:
        stuff[1] = stuff[1][0].upper() + '.'

    print("So " + ' '.join(stuff[0:-2]).title() + ", you're " + str(stuff[-2]) + " right? I heard your favorite color was " + stuff[-1].lower() + "!")

def easy():
    name = input("Please input your name below:\n")
    age = input("Please input your age below:\n")
    color1 = input("Please input your favorite color below:\n")

    print("So " + name.title() + ", you're " + str(age) + " right? I heard your favorite color was " + color1.lower() + "!")

while True:
    coolstuff = input("Complicated or not? (y/n):\n").lower()
    
    if coolstuff == 'y':
        complicate()
        break
    elif coolstuff == 'n':
        easy()
        break
    else:
        print('That was not \"y or n\"... Please try again...')
