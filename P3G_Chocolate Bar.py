finalList = []
ans = int(input())
breakCounter = 0

for count in range (0, ans):
    num = input()
    num1 = int(num[:num.find(" ")])
    num2 = int(num[num.find(" ") + 1:])
    if num1 > num2 or num1 == 1:
        breakCounter = breakCounter + num2-1
        breakCounter = breakCounter + (num1-1)*num2
    else:
        breakCounter = breakCounter + num1-1
        breakCounter = breakCounter + (num2-1)*num1     
    finalList.append(breakCounter)
    breakCounter = 0

for counter in range (0, ans):
    print (finalList[counter])