def primeNumberCheck(ans):
    if ans >= 2:
        for y in range(2, ans):
            if not (ans % y):
                return 0
    else:
        return 0
    return 1

answerList = []
mark = 0
times = int(input())

for prime in range (0, times):
    ans = int(input())
    answerList.append(primeNumberCheck(ans))

for count in range (0, times):
    print (answerList[count])