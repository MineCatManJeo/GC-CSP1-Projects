# Gabriel Crozier, Test tic tac toe (Cause I felt like it)
import random as r
board = [
    '#','#','#',
    '#','#','#',
    '#','#','#'
]
xo = ['x']
xo.insert(r.choice([0,1]),'o')

def show_board(board):
    for i in range(3):
        print(board[0+(3*i)],board[1+(3*i)],board[2+(3*i)])
    print('')
def user_place(board,xo):
    while True:
        show_board(board)
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
            break
def check_win(board):
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

for i in range(3):
    user_place(board,xo)
if check_win(board):
    show_board(board)
