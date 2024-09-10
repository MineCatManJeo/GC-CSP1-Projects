#Gabriel Crozier, Who are you

def complicate():
    stuff = input('Put your name (Last names and Middle names are allowed, allowed with spaces as well), age, and favorite color (One Word) with a space between each one: ')
    stuff = stuff.split()
    if len(stuff[0:-2]) >= 2:
        stuff[1] = stuff[1][0].upper() + '.'

    print("So " + ' '.join(stuff[0:-2]).title() + ", you're " + str(stuff[-2]) + " right? I heard your favorite color was " + stuff[-1].lower() + "!")

def easy():
    name = input("Please input your name here --> ")
    age = input("Please input your age here --> ")
    color1 = input("Please input your favorite color here --> ")

    print("So " + name.title() + ", you're " + str(age) + " right? I heard your favorite color was " + color1.lower() + "!")

coolstuff = input("Complicated or not? (y/n) --> ")

if coolstuff in ('y','n'):
    if coolstuff == 'y':
        complicate()
    elif coolstuff == 'n':
        easy()

