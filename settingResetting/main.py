#Gabriel Crozier, setting & resetting

# Variables
staffA = 32
studentA = 100
guestA = 2 * studentA
guestPTable = 12

print(f"There are {staffA} staff attending, {studentA} students being awarded, {guestA} guests attending. {guestPTable} people can sit at each table!\n")
# Changes
studentA -= 1
staffA -= 3
guestA = 2 * studentA - 15
staffA += 1
print(f"There are now {staffA} staff attending, {studentA} students being awarded, {guestA} guests attending. {guestPTable} people can sit at each table!\n")

# Prints the answer to the equation, the -0.001 is just to make sure than when converting to an integer and adding 1 if the equation is aleary an integer it doesnt just add one
# 26-0.001 = 25.999 int(25.999) = 25 25 + 1 = 26 whule when you do this with another number 1.5 - 0.001 = 1.499 int = 1 then it goes to 2
print('There has to be at least ' + str(int((staffA+studentA+guestA)/guestPTable-0.001)+1) + ' tables.')