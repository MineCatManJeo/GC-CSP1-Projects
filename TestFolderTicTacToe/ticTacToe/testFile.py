# This is my test file
def find_percent(board):
    rows = []
    columns = []
    indexes = []
    percent = []
    for row in board:
        rows.append(round(row.count('#')/0.03))
        try: indexes.append(row.index('#'))
        except: indexes.append(-1)
    for col in range(3):
        column = ''
        for row in range(3):
            column += board[row][col]
        columns.append(round(column.count('#')/0.03))
        try: indexes.append(column.index('#'))
        except: indexes.append(-1)
    percent.append(rows)
    percent.append(columns)
    percent.append(indexes)
    return percent

board = [
    ['x','x','#'],
    ['o','#','#'],
    ['o','x','x']
]

print(find_percent(board))
