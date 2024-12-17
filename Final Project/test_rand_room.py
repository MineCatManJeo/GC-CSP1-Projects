# Room test generator
# Outline for test:
# Start Room
# Choose room nearby
# Generates Room
# Prints either list with rooms
# ORRR prints grid with rooms labeled
# (0,0) = first room
import random
def preGameAssignment():
    Presets = []
    Presets.append(['to the leftL','to the rightR','in front ofU','behindD'])
    Presets.append(['leftL','rightR','forwardsU','backwardsD'])
    Presets.append(["you see a short hallway with a metal door at the end.","you see a rotting wooden door with 3 long slashes in the middle.","you see a wooden door that is almost prestine, only having a bit of dust which you brush off to see strong wood behind it.","farther than you would like to walk, you see a huge archway leading to another room.","you notice a crack in the wall which you think you can fit in.","there is a large intimidating strong door which you think might take a few shoves to open.","you find a small crawlspace you might be able to fit through.","you can see a heavy stone door, you just hope theres machinery to open it for you."])
    Presets.append({'Trinkets':{'Locket of a Saint':{'Weight':20,'AddHealth':40},'Book of the Strong Punch':{'Weight':30,'AddDamage':15},'Speed Boots':{'Weight':40,'AddSpeed':3},'Heart of an Angel':{'Weight':2,'TimesHealth':2},'Mechanical Arm':{'Weight':3,'TimesDamage':2},'Speed of the Fox':{'Weight':4,'TimesSpeed':2.5}},
                    'Potions':{'Small Health Potion':{'Weight':50,'healing':25},'Medium Health Potion':{'Weight':25,'healing':50},'Large Health Potion':{'Weight':20,'healing':100},'Super Health Potion':{'Weight':5,'healing':2500}}})
    return Presets
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
        rom_cords = data_room({'Orc':{'Damage':20,'Speed':3,'Health':40}},rom_cords,cur_locat)
        print(rom_cords)
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
# Gives everything you own in the inventory
def check_inv(inv):
    print('\033c')  # MAKE SURE TO ALLOW FUNCIONALLITY TO MULTIPLE DATA OF THE SAME ITEM name print description of items you type in as well
    print('Inventory:')
    for slot in inv:
        print(f'{slot} x{inv[slot]["amount"]}')
# Print Your actions
def action(rom_cords, cur_locat, preset, inv):
    print('You walk into the room and look around:')
    #Combat
    moveRun = 'Move'
    if len(rom_cords[cur_locat[0]][cur_locat[1]][2]) > 0:
        enemies = []
        for enemy in rom_cords[cur_locat[0]][cur_locat[1]][2].keys():
            enemies.append(enemy)
        print('In the room you see an ' + ', '.join(enemies))
        moveRun = 'Run'
    else:
        # Large room detail (You find you are in a large puzzle room this is what you see)
        # Easy Find items (Right in front of you is the coolest blade youve ever seen)
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
    actionOps = input(f"""What would you like to do:
1. Check Inventory
2. Check Stats
3. Attack (If possible for now)
4. {moveRun}
5. Exit Game
----> """)
    try: actionOps = int(actionOps)
    except: 
        print('User did not input a number, try again not coded yet!') # if user fails retype everything and clear terminal
        return True, True
    # Combat
    # Item
    # Search
    # Move
    if actionOps == 1:
        return ['inv_check']
    if actionOps == 2:
        return ['stat_check']
    if actionOps == 4:
        if moveRun == 'move':
            return ['move',doorPlace1]
        else:
            return ['run']
    if actionOps == 5:
        return ['break']
# Movement
def movement(preset,doorPlace1, rom_cords, cur_locat):
    print('\033c')
    print('You can: ')
    for move_option in preset[1]:
        for door in doorPlace1:
            if move_option[-1].lower() == door:
                print(f'Move {move_option[0:-1]} ({move_option[-1]})') # ATTENTYION NEEDS TO ADD A RETURN TO PREVIOUS ROOM (P or B)
    move = input('Input movement option (u:up, d:down, l:left, r:right): ').lower()
    print('\033c')
    for option in preset[1]:
        if move.upper() == option[-1]:
            print(f'You moved {option[0:-1].lower()}!')
    if not move == rom_cords[cur_locat[0]][cur_locat[1]][1][1]:
        if move == 'u':
            cur_locat[1] += 1
        elif move == 'd':
            cur_locat[1] -= 1
        elif move == 'l':
            cur_locat[0] -= 1
        elif move == 'r':
            cur_locat[0] += 1
        return False, move, cur_locat
    else:
        print('Not a valid movement option!')
        return True, move, cur_locat
# Item Management
def item(inv, action, items = 0, amount = 1, dataItem = {}):
    # options for data: damage, coming soon
    # 2 options, delete, add (works with multiple items / you can add 2 arrows to 4 arrows)
    if action == 'add':
        if items != 0:
            if not items in inv:
                inv[items] = {}
                inv[items]['amount'] = 0
                inv[items]['dataItem'] = dataItem
            if dataItem == inv[items]['dataItem']:
                inv[items]['amount'] += amount
            else:
                items += '|' + str(len(inv))
                inv[items] = {}
                inv[items]['amount'] = amount
            inv[items]['dataItem'] = dataItem
        else: pass
        # maybe for random weopons     
    elif action == 'addTriPot': # Adds a specific type of tool / trinket to the inventory (Not done needs presets)
        randNum = random.random()
        if items == 'Trinket':
            pass
        if items == 'Potion':
            pass
    elif action == 'del':
        try:
            inv[items]['amount'] -= amount
            if inv[items]['amount'] == 0:
                inv.pop(items)
        except:
            print('Error, item does not exist')
    return inv
# Stat Management
def stat(stats, action, statToCng, data = 0):
    if action == 'add':
        stats[statToCng] = data
    elif action == 'del':
        stats.pop(statToCng)
    elif action == 'mod':
        pass
    return stats
# Stats Checker
def check_stats(stats):
    print('\033c')  # MAKE SURE TO ALLOW FUNCIONALLITY TO MULTIPLE DATA OF THE SAME ITEM name print description of items you type in as well
    print('Stats:')
    for stat in stats:
        print(f'{stat}: {stats.get(stat)}')
# Combat
def combat(stats, inv, rom_cords, cur_locat):
    pass
# Starting values
Presets = preGameAssignment()
print('\033c')
roomNum = 0
preRoom = 0
breakLoop = False
current = [0,0]
cords = {}
inv = {}
stats = {}
# Starting Gear
inv = item(inv, 'add', 'Copper Sword', 1, {'damage':15})
inv = item(inv, 'add', 'Chainmail Pants', 1, {'armor':3})
inv = item(inv, 'add', 'Leather Chestplate', 1, {'armor':4})
inv = item(inv, 'add', 'Small Health Potion', 3, {'healing':25})
# add type trinket (extra speed, extra health, speed boots, blah, blah)
# Optional gold
# Starting stats
stats = stat(stats, 'add', 'Health', 100.0)
stats = stat(stats, 'add', 'BaseArmor', 0.0)
stats = stat(stats, 'add', 'BaseSpeed', 5.0)
stats = stat(stats, 'add', 'BaseDamage', 1.0)
stats = stat(stats, 'add', 'Xp', 0)
stats = stat(stats, 'add', 'Level', 0)
cords, roomNum = assign_room(cords, current, roomNum)

while True:
    print('\033c')
    action_vars = action(cords, current, Presets, inv)
    if action_vars[0] == 'move':
        breakLoop, move, current = movement(Presets, action_vars[1], cords, current)
        preRoom = current
        if breakLoop:
            break
        cords, roomNum = assign_room(cords, current, roomNum, move, preRoom)
        input('\nReady to continue?')
    elif action_vars[0] == 'run':
        print('You ran (running not finished yet)')
    elif action_vars[0] == 'inv_check':
        check_inv(inv)
        input('\nReady to continue?')
    elif action_vars[0] == 'stat_check':
        check_stats(stats)
        input('\nReady to continue?')
    elif action_vars[0] == 'break':
        break
print(cords)
# Almost finished movement sysstem, doesnt work very well with other systems but thats a later me problem
# Inventory system started, not even close to done

# IMPORTANT I was able to walk through a will in room 0 possibly because of a previous room error or smth
# also im noticing the 2nd room i enter sometimes has only 3 possible walls/doors, because of how i coded it it wont breal, but it might be worth looking into if i have the time