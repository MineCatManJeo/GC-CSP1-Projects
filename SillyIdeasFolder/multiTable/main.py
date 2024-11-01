# SAilly bilal

num = int(input('Number Alert: '))
baseList = list(range(1,num+1))
print(baseList)
multi = []
for mult1 in baseList:
    newList = []
    for mult2 in baseList:
        newList.append(mult1*mult2)
    multi.append(newList)
print(multi)