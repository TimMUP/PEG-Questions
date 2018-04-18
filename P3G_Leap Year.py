finalList = []
n = int(input())

for count in range (0, n):
    ans = int(input())
    if (ans%4 == 0 and ans%100 != 0) or ans%400 == 0:
        finalList.append("1")
    else:
        finalList.append("0")

for counter in range (0, n):
    print(finalList[counter])