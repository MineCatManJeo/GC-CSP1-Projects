# Gabriel Crozier, Loop thingy
# I LOVE MAKING THINGS COMPLEX FOR NO REASON :D
grid = [

['A', 'B', 'T', 'A', 'D'],

['N', 'K', 'C', 'D', 'B'],

['B', 'A', 'D', 'D', 'G'],

['N', 'F', 'C', 'C', 'J'],

['B', 'B', 'C', 'K', 'D'],

['C', 'A', 'B', 'G', 'E'],

['A', 'G', 'C', 'E', 'A'],

['B', 'K', 'J', 'A', 'D'],

['D', 'C', 'B', 'E', 'G'] ]

ltrTrue = [[],[]]

for row in grid:
    for ltr in row:
        if ltr in ltrTrue[0]:
            ltrTrue[1][ltrTrue[0].index(ltr)] += 1
        else:
            ltrTrue[0].append(ltr)
            ltrTrue[1].append(1)
for i in range(len(ltrTrue[0])):
    print(f'{ltrTrue[0][i]}:{ltrTrue[1][i]}')