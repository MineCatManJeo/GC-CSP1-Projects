#Gabriel Crozier, Simple Calculator

firstNum = str(input('What is the first number you want in these equations:\n'))
secNum = str(input('What is the second number you want in these equations:\n'))

print(firstNum + ' + ' + secNum + ' = ' + str(int(firstNum)+int(secNum)))
print(firstNum + ' - ' + secNum + ' = ' + str(int(firstNum)-int(secNum)))
print(firstNum + ' * ' + secNum + ' = ' + str(int(firstNum)*int(secNum)))
print(firstNum + ' / ' + secNum + ' = ' + str(int(firstNum)/int(secNum)))
print(firstNum + ' ** ' + secNum + ' = ' + str(int(firstNum)**int(secNum)))
print(firstNum + ' % ' + secNum + ' = ' + str(int(firstNum)%int(secNum)))
print(firstNum + ' // ' + secNum + ' = ' + str(int(firstNum)//int(secNum)))