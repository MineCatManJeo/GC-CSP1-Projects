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
def comp_rand_place(board,xo,diff): # simple & non random
    indexValueOff = True # checks if computer has found a better move
    percentHash = find_percent(board,'#') # Gest percent of the # sybol for row & column also first index of it in the row column
    for repeat in range(diff-1): # this in itself allows for computer to check if user about to win and if computer about to win
        try: percent1 = find_percent(board,xo[repeat-(repeat*1)]) # Gets percent of computer sybol (x o) for each row / column
        except: print('Percent1 Calc off')
        if indexValueOff:
            for i in range(2): # loops 1 for row, 1 for column
                for j in range(3): # 3 rows and 3 columns
                    if percent1[i][j] + percentHash[i][j] == 100 and percent1[i][j] == 67: # checks if computer has a 67% to 33% match
                        inVal = percentHash[3][j+(3*i)] # indexes based off of row
                        if i == 0: indexValue = inVal+(3*j) # changes to 0-8 for rows
                        elif i == 1: indexValue = ((inVal*2)+j)+inVal # changes ro 0-8 for columns
                        indexValueOff = False # breaks and says index has been found
                        break
        if indexValueOff: 
            for dig in range(2): # 2 diagonals
                if percent1[2][dig] + percentHash[2][dig] == 100 and percent1[2][dig] == 67:
                    inVal = percentHash[3][dig+6] # indexes for diagonal
                    indexValue = round(inVal*(4/(dig+1))+2*dig) # convert to 1-8
                    indexValueOff = False
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
    diagonals = []
    indexes = []
    percent = []
    for row in board:
        rows.append(round(row.count(value)/0.03))
        try: indexes.append(row.index(value))
        except: indexes.append(-1)
    for col in range(3):
        column = ''
        for row in board:
            column += row[col]
        columns.append(round(column.count(value)/0.03))
        try: indexes.append(column.index(value))
        except: indexes.append(-1)
    for dig in range(2):
        diagonal = ''
        for row in range(3):
            diagonal += board[row][(row+dig)-(dig*2*(row+dig))] # needs to make the second loop time -1 and not times 0
        diagonals.append(round(diagonal.count(value)/0.03))
        try: indexes.append(diagonal.index(value))
        except: indexes.append(-1)
    percent.append(rows)
    percent.append(columns)
    percent.append(diagonals)
    percent.append(indexes)
    return percent
def check_win(board):
    winCheck = ['row','column','diagonal']
    percent = []
    percent.extend([find_percent(board,xo[0]),find_percent(board,xo[1]),find_percent(board,'#')]) # percent data for x o #
    for i in range(2): # user or comp
        for per in range(3): # column - diagonal
            if 100 in percent[i][per]: # if there is a line of 3 items x or o
                print(f'{xo[i].capitalize()} won the game at a {winCheck[per]}.') # tells who won and if its row, diagonal, or column
                return True
    if percent[2][0].count(0) < 3: # if there is more than 0% of the empty space
        return False
    print('It\'s a draw!')
    return True
while True:
    difficulty = input('\nWhat difficulty would you like 1-3: ') # Need to make this a while loop that allows for stats and other things
    try: 
        difficulty = int(difficulty) -1
        difficulty = difficulty % 3 + 1
        break
    except: print('Try again buddy...')
if xo[0] == 'x':
    user_place(board,xo)
while True:
    comp_rand_place(board,xo,difficulty)
    if check_win(board): break
    user_place(board,xo)
    if check_win(board): break
show_board(board,'\nFinal Board:')