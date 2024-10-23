# Gabriel Crozier, Test tic tac toe (Cause I felt like it)
import random as r
board = [
    '#','#','#',
    '#','#','#',
    '#','#','#'
]
xo = ['x']
xo.insert(r.choice([0,1]),'o')

def show_board(board,turn):
    print(f'{turn}')
    for i in range(3):
        print(board[0+(3*i)],board[1+(3*i)],board[2+(3*i)])
    print('')
def user_place(board,xo):
    while True:
        show_board(board,'\nYour turn:')
        userNum = int(input(f'Input a number 1-9 (1 being the top left of board) to place your {xo[0].capitalize()}: '))-1
        if userNum > 8:
            userNum = 8
        elif userNum < 0:
            userNum = 0
        if board[userNum] == '#':
            board[userNum] = xo[0]
            break
        else:
            print('That wasn\'t a number 1-9 that could fit in an empty space, try again...')
def comp_rand_place(board,xo):
    while True:
        compNum = r.randint(0,8)
        if board[compNum] == '#':
            board[compNum] = xo[1]
            show_board(board,'\nComputers Placement:')
            break
def check_win(board): # NOTES MAYBE YOU CAN MAKE A % FOR EACH ROW / COLUMN LIKE row 1 has 33% empty and 66% x or smth then if the ratio is 100% it does the thing? Also if not I can try something like this for possdible other thing ALSO don't work on this project WEDNESDAY in class work on UML
    for i in range(3):
        if board[i] == board[i+3] and board[i] == board[i+6] and board[i] != '#':
            print(f'{board[i].capitalize()} won the game at column {i+1}')
            return True
    for i in range(0,9,3):
        if board[i] == board[i+1] and board[i] == board[i+2] and board[i] != '#':
            print(f'{board[i].capitalize()} won the game at row {int((i/3)+1)}')
            return True
    if board[0] == board[4] and board[0] == board[8] and board[4] != '#':
        print(f'{board[4].capitalize()} won the game with a diagonal from the top left')
        return True
    if board[2] == board[4] and board[2] == board[6] and board[4] != '#':
        print(f'{board[4].capitalize()} won the game with a diagonal from the top right')
        return True
    if '#' not in board:
        print('It\'s a draw!')
        return True

if xo[0] == 'x':
    user_place(board,xo)
while True:
    comp_rand_place(board,xo)
    if check_win(board):
        break
    user_place(board,xo)
    if check_win(board):
        break
show_board(board,'\nFinal Board:')
