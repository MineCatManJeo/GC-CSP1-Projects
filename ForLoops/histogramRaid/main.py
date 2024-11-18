# Gabriel Crozier, Histogram raid
numList = []
num = 0
while num <= -1:
    num += 1
    try: numList.append(int(input('Choose a number: ')))
    except: print('Not a Number')
    if num >= 7:
        try:
            if not bool(input('Would you like to continue adding numbers (True / False): ')):
                break
        except: print('Error No Bool')

print(numList)
print(bool('True'))