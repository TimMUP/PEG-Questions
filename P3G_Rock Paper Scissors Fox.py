ansList = []
temp = 0
times = int(input())
containue = True
for count in range (0, times):
    string = input()
    if string == "Foxen" and containue:
        containue = False
    elif string == "Paper" and containue:
        ans = "Scissors"
        temp += 1
        ansList.append(ans)
    elif string == "Rock" and containue:
        ans = "Paper"
        temp += 1
        ansList.append(ans)
    elif string == "Fox" and containue:
        ans = "Foxen"
        temp += 1
        ansList.append(ans)
    elif string == "Scissors" and containue:
        ans = "Rock"
        temp += 1
        ansList.append(ans) 
        
for counter in range (0, temp):
    print (ansList[counter])