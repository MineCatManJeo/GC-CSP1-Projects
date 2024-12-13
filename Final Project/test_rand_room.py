# Room test generator
# Outline for test:
# Start Room
# Choose room nearby
# Generates Room
# Prints either list with rooms
# ORRR prints grid with rooms labeled
# (0,0) = first room
import random
roomNum = 0
cords = {0:{0:['Room ' + str(roomNum),random.choice(['l','r','u','d'])]}}
current = [0,0]
while True:
    print("You can't move: " + cords[current[0]][current[1]][1])
    move = input('Input movement option (u:up, d:down, l:left, r:right): ')
    print('\033c')
    print('You tried to move: ' + move)
    preRoom = current
    if not move == cords[current[0]][current[1]][1]:
        if move == 'u':
            current[1] += 1
        elif move == 'd':
            current[1] -= 1
        elif move == 'l':
            current[0] -= 1
        elif move == 'r':
            current[0] += 1
        elif move == 's':
            pass
        else:
            break
    else:
        print('You hit a wall!')
    if not current[0] in cords:
        cords[current[0]] = {}
    if not current[1] in cords[current[0]]:
        roomNum += 1
        cords[current[0]][current[1]] = ['Room ' + str(roomNum),random.choice(['l','r','u','d'])] # First is room, second is walls
    print(cords[current[0]][current[1]][0])
print(cords)
# SO FAR! Creates a new generated room inside of a dictionary each time you explore!, Also gives the room a name and a random value
# need to make more changable, do this by using functions and stuff
# Also needs to have more complex wall system that works with more than one wall.
