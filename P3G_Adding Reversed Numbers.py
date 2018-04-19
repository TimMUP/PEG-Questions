finalList = []
ans = int(input())
for count in range (0, ans):
    num = input()
    num1 = num[:num.find(" ")]
    num2 = num[num.find(" ") + 1:]
    finalAns = int(num1[::-1]) + int(num2[::-1])
    finalAns = str(finalAns)
    finalAns = int(finalAns[::-1])
    finalList.append(finalAns)

for counter in range (0, ans):
    print (finalList[counter])