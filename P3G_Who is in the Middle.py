compareList = []
compareList.append(int(input()))
compareList.append(int(input()))
compareList.append(int(input()))

compareList.remove(max(compareList))
compareList.remove(min(compareList))

print(compareList[0])