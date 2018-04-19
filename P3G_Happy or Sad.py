ans = input()
if ans.count(":-)") ==  0 and ans.count(":-(") == 0:
    print ("none")
elif ans.count(":-)") > ans.count(":-("):
    print ("happy")
elif ans.count(":-)") < ans.count(":-("):
    print ("sad")
else:
    print ("unsure")