num = int(input())
finalList = []
for count in range (0, num):
    temp = float(input())
    finalList.append(temp)

print(max(finalList))