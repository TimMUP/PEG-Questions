amount, interest, year = input().split(' ')
amount = float(amount)
interest = 1 + int(interest)*0.01
year = int(year)
print(interest)

for i in range(0, year+1):
    print("%i %0.2f" %(i, amount))
    amount = amount*interest
