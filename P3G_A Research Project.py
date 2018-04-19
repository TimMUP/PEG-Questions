tempList = []
finalList = []

times = int(input())
for attempt in range (0, times):
    num = int(input())
    temp = input()
    temp = " " + temp + " "    
    for picture in range (0, num):
        tempList.append(int(temp[temp.find(" ") + 1: (temp[:temp.find(" ")] + temp[temp.find(" ")+1:]).find(" ") + 1]))
        temp = (temp[:temp.find(" ")] + temp[temp.find(" ") + 1:])
    finalList.append(min(tempList))
    finalList.append(max(tempList))
    tempList[:] = []

for count in range (0, 2*times, 2):
    print("%i %i" %(finalList[count], finalList[count+1]))