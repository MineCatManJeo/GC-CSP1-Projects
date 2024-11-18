# Gabriel Crozier, Character creator
# Avg: Strength 20, health 50, dexterity 15, intellegence 50 RACE

races = ['Human','Elf','Werewolf','Vampire','Dwarf','Giant','Dragonborn']
stats = [[20,50,15,50],[2,75,20,80],[50,100,10,5],[25,25,17,70],[30,30,30,70],[150,200,1,1],[40,75,25,5]] # Strength, health, dexterity, intellegence
classes = ['Rogue','Paladin','Ranger','Wizard','Necromancer','Barbarian','Healer']
statsClass = [[-5,-10,20,10],[20,20,-20,10],[0,-5,15,10],[-10,20,-10,30],[-15,-15,-15,60],[50,50,10,-100],[-40,60,10,15]]

person = input("\nChoose a race:\n" + '\n'.join(races) + '\n')
personClass = input("\nChoose a class:\n" + '\n'.join(classes) + '\n')
personName = input('\nWhat would you like to call yourself: ')

print(f'Your name is {personName.capitalize()}')
for i in range(len(races)):
    if races[i] == person:
        playerStatsRace = stats[i]
        print(f'You are a {races[i]}')
for i in range(len(classes)):
    if classes[i] == personClass:
        playerStatsClass = statsClass[i]
        print(f'You are a {classes[i]}')
for i in range(4):
    playerStatsRace[i] += playerStatsClass[i]
    if playerStatsRace[i] < 0:
        playerStatsRace[i] = 0
print(f'Your strength is: {playerStatsRace[0]}')
print(f'Your health is: {playerStatsRace[1]}')
print(f'Your dexterity is: {playerStatsRace[2]}')
print(f'Your intellegence is: {playerStatsRace[3]}')
