# Gabriel Crozier, Multiplication Table
num = int(input('NUM: '))
numList = list(range(num,num*12+num,num))
multiList = []
for row in numList:
    addList = []
    for col in numList:
        addList.append(row*col)
    multiList.append(addList)
for li in multiList:
    for num1 in li:
        num1 = str(num1)
for li in multiList:
    print(str(int(li[0]/num)) + ': ' + ' | '.join(li))