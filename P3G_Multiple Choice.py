studentList = []
teacherList = []
mark = 0
times = int(input())

for student in range (0, times):
    ans = input()
    studentList.append(ans)
    
for teacher in range (0, times):
    ans = input()
    teacherList.append(ans)
    
for count in range (0, times):
    if studentList[count] == teacherList[count]:
        mark += 1

print (mark)