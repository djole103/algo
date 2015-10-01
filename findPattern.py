numTestCases = int(input())
while(numTestCases!=0):
    rcG = input().split()
    rowsG = int(rcG[0])
    widthG = int(rcG[1])
    matrixG = [input() for _ in range(rowsG)]
    
    rcP = input().split('\t')
    rowsP = int(rcP[0])
    widthP = int(rcP[1]) 
    matrixP = [input() for _ in range(rowsP)]

    if checkforPattern(matrixG,matrixP): print("YES")
    else: print("NO")
    
def checkForPattern(matrixG, matrixP):
    #recursively check rows 
