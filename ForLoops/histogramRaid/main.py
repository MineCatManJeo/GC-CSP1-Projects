# Gabriel Crozier, Histogram raid
numList = []
numCount1 = 0
while numCount1 <= 20:
    numCount1 += 1
    try: numList.append(int(input('Choose a number: ')))
    except: print('Not a Number')
    if numCount1 >= 6:
        try:
            boole = input('Would you like to continue adding numbers (True / False): ').lower()
            if boole == 'false':
                boole = 0
            if not bool(boole):
                break
        except: print('Error No Bool')

numCount2 = 1
for bar in numList:
    print(f'{numCount2}. {bar*"*"}')
    numCount2 += 1