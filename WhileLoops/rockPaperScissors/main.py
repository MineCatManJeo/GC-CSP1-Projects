# Gabriel Crozier, Rock Paper Scissors
import random as r
moves = ['rock','paper','scissors']
wins = 0
attempts = 0
bigWin = False
while True:
    comp = r.randint(0,2)
    user = input('\nRock, paper or scissors: ').lower()
    if not user in moves:
        if not bigWin:
            if user in ['black hole','gun','knife','silly billy','da binky baby', 'my cat']:
                print('$$$$$$$$$$$$$$$$$ BIG WIN $$$$$$$$$$\n')
                print(f'{user.capitalize()} (almost) ALWAYS beats {moves[comp]}!!!!!!!!')
                wins += 3
                attempts += 3
                bigWin = True
                continue
        else:
            if user in ['black hole','gun','knife','silly billy','da binky baby', 'my cat']:
                print('U lose L\n')
                print(f'{user.capitalize()} (now) ALWAYS LOSES against {moves[comp]}!!!!!!!!')
                wins -= 100000000
                attempts += 100000000
                continue
        print('\nInvalid Move. Try again...')
        continue
    print(f'\nThe computer chose {moves[comp]}!')
    attempts += 1
    if moves[moves.index(user)-1] == moves[comp]:
        print(f'\n{user.capitalize()} beats {moves[comp]}!')
        print('\nYou Won!')
        wins += 1
    if moves[comp-1] == user:
        print(f'\n{user.capitalize()} loses to {moves[comp]} ):')
        print('\nYou Lost!')
    if moves.index(user) == comp:
        print(f'You both did {user}')
        print('\nYou Tied!')
        attempts -= 1
    while True:
        check = input('Would you like to go again? (y/n): ').lower()
        if check == 'n' or check == 'y':
            break
        print('That was not a valid answer. Please Try Again...')
    if check == 'n':
        print(f'See you again soon! Score: {wins} win(s) and {attempts - wins} loss(es)!')
        break
