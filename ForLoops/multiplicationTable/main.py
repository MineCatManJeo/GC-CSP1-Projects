# Gabriel Crozier, Multiplication Table
num = int(input('NUM: '))
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
    numbList.append(str(numb) + '. ')
print(' | '.join(numbList))
for i in range(len(multiList)):
    for j in range(len(multiList[i])):
        multiList[i][j] = f'{str(multiList[i][j]):>{formats}}'
    print(f"{numList[i]}. {' | '.join(multiList[i])}")
    print(f"    {'-'*len(' | '.join(multiList[i]))}")