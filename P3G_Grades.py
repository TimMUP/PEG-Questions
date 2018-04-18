finalList = []
t = int(input())
for count in range (0, t):
    x = int(input())
    if 80 <= x <= 100:
        finalList.append("A")
    elif 70 <= x <= 79:
        finalList.append("B") 
    elif 60 <= x <= 69:
        finalList.append("C")    
    elif 50 <= x <= 59:
        finalList.append("D")
    elif 0 <= x <= 49:
        finalList.append("F")    
    else:
        finalList.append("X")

for counter in range (0, t):
    print(finalList[counter])