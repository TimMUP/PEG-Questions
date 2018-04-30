import math
num = int(input())
compareList = []
for i in range(0, num):
    compareList.append(float(input()))
compareList = sorted(compareList)
if num % 2 == 0:
    median = (compareList[int(num/2-1)] + compareList[int(num/2)])/2
else:
    median = compareList[math.floor(num/2)]
print ("The median on the test is %0.1f" %(median))
