# Gabriel Crozier, Test tic tac toe (Cause I felt like it)
import random as r
board = [
    ['#','#','#'],
    ['#','#','#'], # Add alignment to things later
    ['#','#','#']
]
xo = ['x']
xo.insert(r.choice([0,1]),'o')

def show_board(board,turn):
    print(f'{turn}')
    for i in range(3):
        print(board[i][0],board[i][1],board[i][2])
    print('')
def user_place(board,xo):
    show_board(board,'\nYour turn:')
    while True:
        userNum = input(f'Input a number 1-9 (1 being the top left of board) to place your {xo[0].capitalize()}: ')
        try: 
            userNum = int(userNum)-1
        except:
            show_board(board,'\nInvalid input. Try again:')
            continue
        if userNum > 8:
            userNum = 8
        elif userNum < 0:
            userNum = 0
        if board[userNum//3][userNum%3] == '#':
            board[userNum//3][userNum%3] = xo[0]
            break
        else:
            show_board(board,'\nInvalid placement location. Try again:')
def comp_rand_place(board,xo): # simple & non random
    indexValueOff = True
    percent1 = find_percent(board,xo[1]) # Gets percent of computer sybol (x o) for each row / column
    percentHash = find_percent(board,'#') # Gest percent of the # sybol for row & column also first index of it in the row column
    for i in range(2): # loops 1 for row and 1 for column
        for j in range(3): # 3 rows and 3 columns
            if percent1[i][j] + percentHash[i][j] == 100 and percent1[i][j] == 67: # checks if computer has a 67% to 33% match
                inVal = percentHash[2][j+(3*i)] # indexes based off of row
                if i == 0: indexValue = inVal+(3*j) # changes to 0-8 for rows
                elif i == 1: indexValue = ((inVal*2)+j)+inVal # changes ro 0-8 for columns
                indexValueOff = False # breaks and says index has been found
                break
    while True:
        if indexValueOff: compNum = r.randint(0,8) # random num (simple)
        elif not indexValueOff: 
            compNum = indexValue # non random always wins if 2 in row / column
        if board[compNum//3][compNum%3] == '#':
            board[compNum//3][compNum%3] = xo[1]
            show_board(board,'\nComputers Placement:')
            break
def find_percent(board,value): # NEED TO ADD FUNCTION FOR DIAGONAL
    rows = []
    columns = []
    indexes = []
    percent = []
    for row in board:
        rows.append(round(row.count(value)/0.03))
        try: indexes.append(row.index(value))
        except: indexes.append(-1)
    for col in range(3):
        column = ''
        for row in range(3):
            column += board[row][col]
        columns.append(round(column.count(value)/0.03))
        try: indexes.append(column.index(value))
        except: indexes.append(-1)
    percent.append(rows)
    percent.append(columns)
    percent.append(indexes)
    return percent
def check_win(board): # NOTES MAYBE YOU CAN MAKE A % FOR EACH ROW / COLUMN LIKE row 1 has 33% empty and 66% x or smth then if the ratio is 100% it does the thing? Also if not I can try something like this for possdible other thing ALSO don't work on this project WEDNESDAY in class work on UML
    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != '#': # maybe try using % instead of this stuff this could be redundent
            print(f'{board[0][i].capitalize()} won the game at column {i+1}')
            return True
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != '#':
            print(f'{board[i][0].capitalize()} won the game at row {i+1}')
            return True
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[1][1] != '#':
        print(f'{board[0][0].capitalize()} won the game with a diagonal from the top left')
        return True
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[1][1] != '#':
        print(f'{board[1][1].capitalize()} won the game with a diagonal from the top right')
        return True
    for row in board:
        if '#' in row:
            return False
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
