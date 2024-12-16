# Room test generator
# Outline for test:
# Start Room
# Choose room nearby
# Generates Room
# Prints either list with rooms
# ORRR prints grid with rooms labeled
# (0,0) = first room
import random
# Function to add data to each room
def data_room(data,room_cords, cur_locat):
    try:
        room_cords[cur_locat[0]][cur_locat[1]].append(data)
        return room_cords
    except:
        print('Error, something went wrong in the data_room function')
# Function to assign a room (cords thing)
def assign_room(rom_cords, cur_locat, roomNumb, move = 'u', pre = 0):
    if not cur_locat[0] in rom_cords:
        rom_cords[cur_locat[0]] = {}
    if not cur_locat[1] in rom_cords[cur_locat[0]]:
        rom_cords[cur_locat[0]][cur_locat[1]] = ['Room ' + str(roomNumb)]
        roomNumb += 1
        rom_cords = data_room(add_walls(pre,move),rom_cords,cur_locat)
    return rom_cords, roomNumb
# Walls function
def add_walls(pre_room, move):
    move_options = ['l','r','u','d']
    doorList, wall_accept = move_options, move_options
    if not pre_room == 0:
        wall_accept.pop(wall_accept.index(move)+1-2*(wall_accept.index(move)%2))
    wall_num = random.randint(0,3)
    wallSet = set({})
    for i in range(wall_num):
        wallSet.add(random.choice(wall_accept))
    wallList = list(wallSet)
    for wall in wallList:
        doorList.remove(wall)
    all4Walls = []
    all4Walls.append(doorList)
    all4Walls.append(wallList)
    return all4Walls
# Print Your actions
def action(rom_cords, cur_locat, preset):
    print('You walk into the room and look around:')
    # Enemy (suddenly an orc... blah)
    # Large room detail (You find you are in a large puzzle room this is what you see)
    # Easy Find items (Right in front of you is the coolest blade youve ever seen)
    # Exits (Room entrances / exits) (You see a door to the right)
    doorPlace = []
    doorPlace1 = []
    for pos1 in rom_cords[cur_locat[0]][cur_locat[1]][1][0]:
        for pos2 in preset[0]:
            if pos1.upper() == pos2[-1]:
                doorPlace.append(pos2[0:-1])
                doorPlace1.append(pos1)
    if len(doorPlace) > 2: print('You see doors ' + ', '.join(doorPlace[0:-1]) + ', and ' + doorPlace[-1] + ' you.')
    elif len(doorPlace) == 2: print('You see doors ' + ', '.join(doorPlace[0:-1]) + ' and ' + doorPlace[-1] + ' you.')
    else: print('You see a door ' + doorPlace[0] + ' you.')
    # Small Room detail (optional maybe) (There are a few cracks on the wall to the right)
    # Actions (What would you like to do)
    print('\n')
    actionOps = input("""What would you like to do:
1. Move
2.
3.
4.
----> """)
    try: actionOps = int(actionOps)
    except: print('User did not input a number, try again not coded yet!')
    # Combat
    # Item
    # Search
    # Move
    if actionOps == 1:
        breakLoop, move = movement(preset,doorPlace1)
    return breakLoop, move
# Movement
def movement(preset,doorPlace1):
    print('You can: ')
    for move_option in preset[1]:
        for door in doorPlace1:
            if move_option[-1].lower() == door:
                print(f'Move {move_option[0:-1]} ({move_option[-1]})')
    move = input('Input movement option (u:up, d:down, l:left, r:right): ')
    print('\033c')
    print('You moved [insert move here]')
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
            return True, move
        else:
            return False, move
    else:
        print('You hit a wall!')


# In Game text preset
Presets = []
Presets.append(['to the leftL','to the rightR','in front ofU','behindD'])
Presets.append(['leftL','rightR','forwardsU','backwardsD'])
Presets.append(["you see a short hallway with a metal door at the end.","you see a rotting wooden door with 3 long slashes in the middle.","you see a wooden door that is almost prestine, only having a bit of dust which you brush off to see strong wood behind it.","farther than you would like to walk, you see a huge archway leading to another room.","you notice a crack in the wall which you think you can fit in.","there is a large intimidating strong door which you think might take a few shoves to open.","you find a small crawlspace you might be able to fit through.","you can see a heavy stone door, you just hope theres machinery to open it for you."]) # Doors
# Starting values
print('\033c')
roomNum = 0
preRoom = 0
current = [0,0]
cords = {}
cords, roomNum = assign_room(cords, current, roomNum)
action(cords, current, Presets)
while True:
    preRoom = current
    breakLoop, move = action(cords, current, Presets)
    if not breakLoop:
        break
    cords, roomNum = assign_room(cords, current, roomNum, move, preRoom)
print(cords)
# SO FAR! Creates a new generated room inside of a dictionary each time you explore!, Also gives the room a name and a random value
