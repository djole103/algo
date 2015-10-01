def checkForPattern(matrixG, matrixP):
    #recursively check rows
    for row in range(rowsG - rowsP):
        if startPatternCheck(matrixG[row:-1],matrixP):
            return True
        else:
            continue
    return False

def startPatternCheck(subsetG,matrixP):
    for index, row in enumerate(matrixP):
        if row in subsetG[index]:
            continue
        else:
            return False
    return True

numTestCases = int(input())
while(numTestCases!=0):
    rcG = input().split()
    rowsG = int(rcG[0])
    widthG = int(rcG[1])
    matrixG = [input() for _ in range(rowsG)]
    
    rcP = input().split()
    rowsP = int(rcP[0])
    widthP = int(rcP[1]) 
    matrixP = [input() for _ in range(rowsP)]

    if checkForPattern(matrixG,matrixP): print("YES")
    else: print("NO")
    
    numTestCases -=1
