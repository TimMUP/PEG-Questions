tempList = []
ans = int(input())
for count in range (0, ans):
    num = int(input())
    num += 1
    while True:
        if str(num**3)[-3::] == "888":
            tempList.append(num)
            break
        else:
            num += 1
            
for counter in range (0, ans):
    print(min(tempList))
    tempList.remove(min(tempList))