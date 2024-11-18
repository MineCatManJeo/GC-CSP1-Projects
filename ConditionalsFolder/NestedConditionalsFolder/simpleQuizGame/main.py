# Gabriel Crozier, Nested conditionals simple quiz game
import time as t
quzQutins = [
    # Easy Difficulty
    'What drops when you break a grass block with your fist?||A. Grass\nB. Dirt\nC. Grass Block\nD. Gravel||B',
    'What pickaxe do you need to break obsidian?||A. Diamond\nB. Iron\nC. Wooden\nD. Golden||A',
    'How do you craft a furnace?||A. 8 cobblestone around the middle square of a crafting table\nB. 4 cobblestone inside of your inventory crafting\nC. 8 cobblestone around a peice of coal in a crafting table\nD. Trick question, you find one in a village||A',
    'What would you NORMALLY press in order to attack a mob?||A. Right Click\nB. Left Click\nC. E\nD. F||B',
    'What do you use to trade with villagers?||A. Rubies\nB. Diamonds\nC. Bread\nD. Emeralds||D',
    # Normal Difficulty
    'What do you need to control a saddled pig in Minecraft?||A. Warped Fungus on a Stick\nB. Potato on a Stick\nC. Carrot on a Stick\nD. Raw Porkchop||C',
    'What is the effect you get when you kill a pillager captain?||A. Raiders Incoming\nB. Raid\nC. Bad Omen\nD. Vile||C',
    'Where do you get blaze rods?||A. The Nether Fortress\nB. Bastion\nC. Sky Islands\nD. The Nether Forges||A',
    'Where does the end portal spawn in Minecraft?||A. The Sky Islands\nB. Stronghold\nC. Below the Void\nD. The Weathered Ruins||B',
    'How do you tame a cat in Minecraft?||A. You rush the cat with fish\nB. You walk slowly to the cat and feed it cooked fish\nC. You slowly walk up to the cat and feed it raw fish\nD. You drop fish on the ground and wait for the cat to eat it||C',
    # Hard Difficulty
    'Which one of these items can you get as a treasure item from fishing?||A. Leather Boots\nB. Golden Apple\nC. Heart of the Sea\nD. Fishing Rod||D',
    'How would you summon a horde of 25 zombies onto a player named Steve using a command?||A. /summon zombie at Steve 25\nB. /execute at Steve as @e[limit=25] run summon zombie ~ ~ ~\nC. /zombie 25 at Steve\nD. /execute at Steve summon zombie 25||B',
    'How much iron would you need for a full set of iron armor?||A. 46\nB. 18\nC. 24\nD. 42||C',
    'How do you get the star trader advancement in Minecraft?||A. Trade with a villager at height limit\nB. Fly into the sky islands and trade with a sky villager\nC. Bring a villager to The End and trade with them\nD. Find the special sky villager class and trade with them||A',
    'What is the arbalistic advancement in Minecraft?||A. Trick question, there is no achievement called arbalistic\nB. It is an advancement where you kill 500 mobs with a bow\nC. It is where you shoot and kill 5 different mobs with one peircing arrow of a crossbow\nD. It is when you find a rare diamond crossbow inside of a pillager dungeon.||C'
]

def quiz():
    print('\nWelcome to my epic most amazing quiz about Minecraft!!!!\n')
    time = t.time()
    while True:
        diff = input('Choose a difficulty 1-3: ')
        try: 
            diff = int(diff) - 1
            break
        except: print('\nTry Again...\n')
    corAns = 0
    for i in range(5):
        print(f'\n{quzQutins[i+diff*5].split("||")[0]}')
        answer = input(f'\n{quzQutins[i+diff*5].split("||")[1]}\n\n Answer Here: ').lower()
        if answer[0] in 'abcd':
            if answer[0] == 'a':
                if quzQutins[i+diff*5].split('||')[2].lower() == 'a':
                    print('\nCorrect\n')
                    corAns += 1
                    if diff != 2:
                        diff += 1
                        print('Difficulty Increase!\n')
                    else: print('')
                    continue
            elif answer[0] == 'b':
                if quzQutins[i+diff*5].split('||')[2].lower() == 'b':
                    print('\nCorrect\n')
                    corAns += 1
                    if diff != 2:
                        diff += 1
                        print('Difficulty Increase!\n')
                    else: print('')
                    continue
            elif answer[0] == 'c':
                if quzQutins[i+diff*5].split('||')[2].lower() == 'c':
                    print('\nCorrect\n')
                    corAns += 1
                    if diff != 2:
                        diff += 1
                        print('Difficulty Increase!\n')
                    else: print('')
                    continue
            else:
                if quzQutins[i+diff*5].split('||')[2].lower() == 'd':
                    print('\nCorrect\n')
                    corAns += 1
                    if diff != 2:
                        diff += 1
                        print('Difficulty Increase!')
                    continue
            print('\nIncorrect')
            if diff != 0:
                diff -= 1
                print('Difficulty Decrease!')
    time = t.time() - time
    if round(time//60) == 0: print(f'It took you {round(time%60)} seconds to get {corAns} out of 5 questions correct!')
    else: print(f'It took you {round(time//60)} minutes and {round(time%60)} seconds to get {corAns} out of 5 questions correct!')
quiz()

