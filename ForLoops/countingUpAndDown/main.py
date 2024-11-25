# Gabriel Crozier, Epic Counting Thangy
try: countAmount = int(input('What number would you like to count to?: '))
except: print('Nuh You Can\'t Try Again...')
for i in range(1,countAmount * 2+1):
    if i <= countAmount:
        print(i)
    else:
        print((countAmount*2+1)-i)
