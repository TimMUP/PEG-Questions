answerList = []
scenario = int(input())
for count in range (0, scenario):
    flow = int(input())
    temp = int(input())
    listOfNum = [temp]
    for count2 in range (1, flow):
        temp = int(input())
        listOfNum.append(temp)
    answerList.append(max(listOfNum))

for counter in range (0, scenario):
    print (answerList[counter])