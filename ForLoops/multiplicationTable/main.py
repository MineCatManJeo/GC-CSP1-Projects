# Gabriel Crozier, Multiplication Table
num = int(input('Hello User!\nInput a number to create a multiplication table!\n1 = normal 12x12 multiplication table\n2 = 2,4,6,8... ect\nInput your number here!: '))
numList = list(range(num,num*12+num,num))
numbList = []
multiList = []
for row in numList:
    addList = []
    for col in numList:
        addList.append(row*col)
    multiList.append(addList)
formats = len(str(multiList[-1][-1]))
for numb in numList:
    numbList.append(f'{numb:>{formats}}')
print(' '*(len(numbList[-1].strip())+1) + '.  '.join(numbList) + '.')
for i in range(len(multiList)):
    for j in range(len(multiList[i])):
        multiList[i][j] = f'{str(multiList[i][j]):>{formats}}'
    print(f"{' '*(len(numbList[-1].strip())+2)}{'-'*len(' | '.join(multiList[0]))}")
    print(f"{numList[i]:>{len(numbList[-1].strip())}}. {' | '.join(multiList[i])}")
print(f"{' '*(len(numbList[-1].strip())+2)}{'-'*len(' | '.join(multiList[0]))}")