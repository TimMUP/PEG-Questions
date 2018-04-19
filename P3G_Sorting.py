tempList = []
ans = int(input())
for count in range (0, ans):
    num = int(input())
    tempList.append(num)

for counter in range (0, ans):
    print(min(tempList))
    tempList.remove(min(tempList))
