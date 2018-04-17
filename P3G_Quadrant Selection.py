xValue = int(input())
yValue = int(input())

if xValue > 0:
    if yValue > 0:
        quad = 1
    else:
        quad = 4
if xValue < 0:
    if yValue > 0:
        quad = 2
    else:
        quad = 3

print (quad)