aValue = float(input(""))
bValue = float(input(""))

if aValue == 0 and bValue == 0:
    print("indeterminate")
elif aValue == 0:
    print("undefined")
else:
    xValue = (- bValue)/aValue
    print("%0.2f" %(xValue))