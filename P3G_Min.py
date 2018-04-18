ansList = []

n = int(input())
for count in range (0, n):
    ans = float(input())
    ansList.append(ans)

print("%0.2f" %(min(ansList)))