letterCount = ['a','e','i','o','u']
while True:
    string = input()
    if len(string) >= 4 and letterCount.count(string[-3]) == 0:
        print(string[:-2]+"our")
    elif string == "quit!":
        break
    else:
        print(string)