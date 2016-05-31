NN = matrix

for i in range(len(NN[0])):
        for j in range(len(NN[1])):
                curr = NN[i][j]
                tmp = NN[j][len(NN[0]) - i + 1)]

left = 0
right = len(NN[0]) - 1 
row = 0
while(left < right):
        for i in range(4):
                curr = NN[row][col]
                tmp = NN[col][len(NN[1]) - left + 1]

def rotatePix90(row, col, NN):
        cur = NN[row][col]
        nxt = NN[col][len(NN[0])- row + 1]
