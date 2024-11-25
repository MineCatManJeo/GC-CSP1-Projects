# Gabriel Crozier, Loop thingy
# I LOVE MAKING THINGS COMPLEX FOR NO REASON :D
grid = [

['A', 'B', 'C', 'A', 'D'],

['C', 'A', 'B', 'D', 'E'],

['A', 'D', 'C', 'E', 'A'],

['B', 'A', 'C', 'A', 'D'],

['D', 'C', 'B', 'E', 'A'] ]

ltrTrue = [[],[]]

for row in grid:
    for ltr in row:
        if not ltr in ltrTrue:
            ltrTrue[0].append([ltr])
            ltrTrue[1].append([1])
        else:
            ltrTrue[ltrTrue.index(ltr)+1] += 1
for i in range(len(ltrTrue[0])):
    print(ltrTrue[0][i])