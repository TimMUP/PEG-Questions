import sys
print ("Ready")
while True:
    ans = input()
    if ans == "  ":
        break
    elif ans == "pq" or ans == "qp" or ans == "bd" or ans == "db":
        print ("Mirrored pair")
    else:
        print ("Ordinary pair")

while True:
    ans = input()