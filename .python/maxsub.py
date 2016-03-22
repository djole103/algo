def subArray(lst):
	start = 0
	end = 0
	for i in range(len(lst)):
		pass

def msa(lst):
	return max(sum(lst[i:j]) for i in range(len(lst)) for j in range(i,len(lst)+1 ) )

def msaTrack(lst):
	maxSum = 0 - float('inf')
	for s in (sum(lst[i:j]) for i in range(len(lst)) for j in range(i,len(lst)+1)):
		if s > maxSum: maxSum = s
	return maxSum

def msaGood(lst):
	best = cur = 0
	for i in lst:
		print("BEFORE Best is: %i\nCurr is: %i\n" % (best,cur))
		cur = max(cur + i,0)
		best = max(best,cur)
		print("AFTER Best is: %i\nCurr is: %i\n" % (best,cur))
	return best

print(msaGood([1,2,3,-10,6,20]))
