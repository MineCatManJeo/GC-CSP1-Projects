def add(itemList):
    item = input('What would you like to add to your list?: ')
    item = item.split()
    for itm in item:
        itemList.append(itm)

def remove(itemList):
    item = input('''
  What would you like to do?
   Enter the item you would like to remove
   Enter the location of the item you would like to remove:\n''')
    if item.isdigit(): # allows for finding the location of an item
        item = int(item) - 1
        itemList.pop(item)
    else:
        itemList.remove(item)

list1 = []
while True:
    action = input("""
  What would you like to do?
   Enter 1 to add item
   Enter 2 to remove item
   Enter 3 to print your list
   Enter 4 to leave the list:\n""")

    if action =="1":
        add(list1)
    elif action =="2":
        remove(list1)
    elif action =='3': # added a print function
        print('\nYour list:')
        for i in range(len(list1)):
            print(f'{i+1}. {list1[i]}')
    else:
        print("Have a nice day!")
        break