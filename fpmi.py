def firstmiss(lst):
	low = float('inf')
	high = 0
	total = 0
	for num in lst:
		if num > high: high = num
		if num < low: low = num
		total +=num
	for i in range(low,high+1):
		total-=i
	return total

lst = [-2,-1,4,8,1,2,3,6,7]
print(firstmiss(lst))
