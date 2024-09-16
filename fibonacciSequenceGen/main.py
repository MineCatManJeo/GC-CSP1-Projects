#Gabriel Crozier, Fibonacci Sequence Generator RAID

# How far into the sequence do you want to go
num = int(input('How much of the Fibonacci thingy do you want:\n'))
# If the number is greater than 10000 it just says nuh because the computer doesn't want to do that
if num > 10000:
    print(f'Your number {str(num)} exceded the 100000 limit good thing we set it back down.')
    num = 10000
# Starting Number
fibonacci = [0,1]

# Prints starting numbers
print('\n'+str(fibonacci[0]))
print(fibonacci[1])

# For i in range the number you input add a new correct value to the list and print it
for i in range(num):
    fibonacci.append(fibonacci[-2]+fibonacci[-1])

    # If the value is too high it will print in scientific notation.
    if fibonacci[-1] >= 1e200:
        print('{:e}'.format(fibonacci[-1]))
    else:
        print(fibonacci[-1])