import math
numTests = int(input())

for test in range(numTests):
	A,B = input().split()
	squares = 0
	for num in range(A,B+1):
		sq = math.sqrt(num)
		if sq == math.floor(sq): squares+=1

	print(squares)
