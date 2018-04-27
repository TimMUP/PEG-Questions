num = int(input())
compareList = []
for i in range(0, num):
    compareList.append(input())

for x in range(65, 71):
    print(compareList.count(chr(x)))
    num = num - compareList.count(chr(x))
print (num)