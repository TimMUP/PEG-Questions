import math

count = 0
counter = 0
i = 1
num = int(input())
while True:
    i += 1
    for x in range (2, i):
        if i % x == 0:
            count += 1
            break
    if count == 0:
        print(i)
        counter += 1
    count = 0
    if counter == num:
        break