#Gabriel Crozier, Simple Calculator

firstNum = str(input('What is the first number you want in this equation:\n'))
operator = input('What do you want to do to these numbers:\n')
secNum = str(input('What is the second number you want in this equation:\n'))


print(firstNum,operator,secNum,'=',str(eval(firstNum+operator+secNum)))