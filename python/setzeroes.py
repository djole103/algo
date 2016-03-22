def setZeroes(matrix):
	val = {}
	for m in range(len(matrix)):
		for n in range(len(matrix[0])):
			if matrix[m][n] == 0:
				val[m] = 0
				val[n] = 0
			if m in val: matrix[m][n] = 0
			elif n in val: matrix[m][n] = 0
	return matrix
#matrix = [[0,1,2],[3,4,5],[6,7,8]]

matrix = [[1,0]]
result = setZeroes(matrix)
print(result)
