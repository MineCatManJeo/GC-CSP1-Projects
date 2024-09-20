# Gabriel Crozier, This is to help me do my chemistry assignment...

numOfNum = int(input("How many numbers do you want to calculate?:\n"))

numList = []
percList = []

multiList = []

if numOfNum == -2:
    for i in range(2):
        numList.append(float(input("\nInput Number:\n")))
    percList.append(float(input("\nInput Atomic Weight:\n")))
    multiList.append(round(numList[-1]-numList[-2],3))
    multiList.append(round(percList[0]-numList[-2],3))
    multiList.append(round(multiList[1]/multiList[0]*100,3))
    print("\n"+str(multiList[-1]) + "%" + ", and " + str(100-multiList[-1]) + "%")

else:
    for i in range(numOfNum):
        numList.append(float(input("\nInput Number:\n")))
        percList.append(float(input("\nInput Percentage:\n")))
        multiList.append(round(numList[-1]*percList[-1],8))
    print("\n"+str(sum(multiList)/100))