# Gabriel Crozier, Error Handeling Calculator
operate = ['+','-','*','/','**','%','//']
while True:
    userOp = input(f'Choose one of these methods: {", ".join(operate)}: ')
    if userOp in operate:
        break
    print('\nThat was not a Valid Method')

while True:
    try:
        userNum1 = int(input('Whats your first number going to be?: '))
        userNum2 = int(input('Whats your second number going to be?: '))
        break
    except:
        print('\nError, please try again...')

if userOp == operate[0]:
    answer = userNum1 + userNum2
elif userOp == operate[1]:
    answer = userNum1 - userNum2
elif userOp == operate[2]:
    answer = userNum1 * userNum2
elif userOp == operate[3]:
    if userNum2 != 0: answer = userNum1 / userNum2
    else: 
        print('Error: Tried to divide by 0...')
        answer = 'NaN'
elif userOp == operate[4]:
    answer = userNum1 ** userNum2
elif userOp == operate[5]:
    if userNum2 != 0: answer = userNum1 % userNum2
    else: 
        print('Error: Tried to divide by 0...')
        answer = 'NaN'
elif userOp == operate[6]:
    if userNum2 != 0: answer = userNum1 // userNum2
    else: 
        print('Error: Tried to divide by 0...')
        answer = 'NaN'

print(f'{userNum1} {userOp} {userNum2} = {answer}')
