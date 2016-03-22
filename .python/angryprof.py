numTestCases = int(input())
for i in range(numTestCases):
    testCase = input()
    studentsNeeded = int(testCase.split()[1])
    times = input().split()
    kids = 0
    for time in times:
        if int(time) <= 0: kids+=1
    if kids < studentsNeeded: print("YES") 
    else: print("NO")
