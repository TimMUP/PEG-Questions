numerator = int(input())
denominator = int(input())
reminder = numerator % denominator
integer = ""

if denominator != 2:
    for i in range (int(denominator/2), 1, -1):
        if denominator % i == 0 and reminder % i == 0:
            finalDenominator = denominator/i
            finalReminder = reminder/i
            break
        else:
            finalDenominator = denominator
            finalReminder = reminder
else:
    finalDenominator = denominator
    finalReminder = reminder

integer = numerator//denominator

if finalReminder != 0 and integer != 0:
    print("%i %i/%i" %(integer, finalReminder, finalDenominator))
elif integer == 0 and finalReminder !=0:
    print("%i/%i" %(finalReminder, finalDenominator))
else:
    print(integer)