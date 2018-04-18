ansList = []
ans = int(input())
times = int(input())
ansList.append(ans)
for count in range (0, times):
    ans = ans*10
    ansList.append(ans)

print (sum(ansList))