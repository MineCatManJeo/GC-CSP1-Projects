# Gabriel Crozier
symbols = ['!','@','#','$','%','^','&','*','-','_','=','+','<','>','~','`','?']
while True:
    password = input('\nInput a password: ')
    if len(password) < 8:
        print('Password is not long enough.')
        continue
    if not any(ele.isupper() for ele in password):
        print('Password needs to have a capital letter.')
        continue
    if not any(ele.isdigit() for ele in password):
        print('Password needs to have a number')
        continue
    if not any(sym in password for sym in symbols):
        print('Password needs to have special characters.')
        continue
    break
print('Broken')