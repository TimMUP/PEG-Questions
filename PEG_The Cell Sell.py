def planACost(daytime, evening, weekend):
    if daytime > 100:
        cost = (daytime - 100)*0.25
    else:
        cost = 0
    cost += evening*0.15
    cost += weekend*0.20
    return cost

def planBCost(daytime, evening, weekend):
    if daytime > 250:
        cost = (daytime - 250)*0.45
    else:
        cost = 0
    cost += evening*0.35
    cost += weekend*0.25
    return cost

dayUsage = int(input())
eveningUsage = int(input())
weekendUsage = int(input())

planATotal = round(planACost(dayUsage, eveningUsage, weekendUsage), 2)
planBTotal = round(planBCost(dayUsage, eveningUsage, weekendUsage), 2)

print("Plan A costs %0.2f" %(planATotal))
print("Plan B costs %0.2f" %(planBTotal))
if planATotal > planBTotal:
    print("Plan B is cheapest.")
elif planATotal < planBTotal:
    print("Plan A is cheapest.")
else:
    print("Plan A and B are the same price.")