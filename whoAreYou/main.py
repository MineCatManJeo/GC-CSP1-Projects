#Gabriel Crozier, Who are you

#This function was for me to have fun if it isn't wanted I have the easy function
def complicate():
    stuff = input('Put your name (Last names and Middle names are allowed, allowed with spaces as well), age, and favorite color (One Word) with a space between each one down below:\n')
    stuff = stuff.split()
    if len(stuff[0:-2]) >= 2:
        stuff[1] = stuff[1][0].upper() + '.'

    print("So " + ' '.join(stuff[0:-2]).title() + ", you're " + str(stuff[-2]) + " right? I heard your favorite color was " + stuff[-1].lower() + "!")

#This function is for the assignment in case the more complicated one is not what is wanted
def easy():
    name = input("Please input your name below:\n").strip()
    age = input("Please input your age below:\n").strip()
    color1 = input("Please input your favorite color below:\n").strip()

    print("So " + name.title() + ", you're " + str(age) + " right? I heard your favorite color was " + color1.lower() + "!")

#This asks if you want to use the easy or complicated function
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
