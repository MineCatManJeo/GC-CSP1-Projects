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
    diagonals.append(0)
    indexes.append(-1)
    percent.append(rows)
    percent.append(columns)
    percent.append(diagonals)
    percent.append(indexes)
    return percent

board = [
    ['x','x','o'],
    ['o','#','#'],
    ['o','x','#']
]

#print(find_percent(board,'#'))
for i in range(0): print('hi')
