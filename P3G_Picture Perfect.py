from math import *
while True:
    num = int(input())
    if num == 0:
        break
    else:
        if (sqrt(num)).is_integer():
            perimeter = sqrt(num)*4
            print ("Minimum perimeter is %i with dimensions %i x %i" %(perimeter, sqrt(num), sqrt(num)))
        else:
            for i in range(floor(sqrt(num)), 0, -1):
                if num % i == 0:
                    perimeter = 2*i + 2*(num/i)
                    print("Minimum perimeter is %i with dimensions %i x %i" %(perimeter, i, num/i))
                    break