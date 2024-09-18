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
print(f"There are {staffA} staff attending, {studentA} students being awarded, {guestA} guests attending. {guestPTable} people can sit at each table!\n")
print((staffA+studentA+guestA)/guestPTable)