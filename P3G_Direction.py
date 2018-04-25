num = int(input())
lowestInt = 0
for count in range (0, num):
    temp = int(input())
    lowestInt = abs(0 - temp)
    ans = "N"
    if abs(90 - temp) < lowestInt:
        lowestInt = abs(90 - temp)
        ans = "E"
    if abs(180 - temp) < lowestInt:
        lowestInt = abs(180 - temp)
        ans = "S"
    if abs(270 - temp) < lowestInt:
        lowestInt = abs(270 - temp)
        ans = "W"
    if abs(360 - temp) < lowestInt:
        lowestInt = abs(360 - temp)
        ans = "N"
    print(ans)