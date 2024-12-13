# Room test generator
# Outline for test:
# Start Room
# Choose room nearby
# Generates Room
# Prints either list with rooms
# ORRR prints grid with rooms labeled
# (0,0) = first room
import random
cords = {}
roomNum = 0
current = [0,0]
while True:
    move = input('Input movement option (u:up, d:down, l:left, r:right): ')
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
    if not current[0] in cords:
        cords[current[0]] = {}
    if not current[1] in cords[current[0]]:
        cords[current[0]][current[1]] = ['Room ' + str(roomNum),random.choice(['a','b','c'])]
        roomNum += 1
    print(cords[current[0]][current[1]])
print(cords)
# SO FAR! Creates a new generated room inside of a dictionary each time you explore!, Also gives the room a name and a random value
