import sys
quarters = 0
dimes = 0
nickels = 0
cents = 0
number = int(input())
print("%i cents requires" %(number), end="")

def calculations(value, name):
    global number
    if number%value == 0:
        amount = number//value
        number = 0
        if amount == 1:
            print(" %i %s." %(amount, name))
        else:
            print(" %i %ss." %(amount, name))
    elif value > number:
        amount = 0
    else:
        amount = number//value
        number = number-amount*value
        if amount == 1:
            print(" %i %s," %(amount, name), end="")    
        else:
            print(" %i %ss," %(amount, name), end="")
    return amount

quarters = calculations(25, "quarter")

if number != 0:
    dimes = calculations(10, "dime")
    if number != 0:
        dimes = calculations(5, "nickel")
        if number != 0:
            dimes = calculations(1, "cent")        
        else:
            sys.exit()
    else:
        sys.exit()
else:
    sys.exit()
        