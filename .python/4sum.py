# 4 numbers that sum to 0
from collections import defaultdict
def foursum(lst):
	sums = defaultdict(list)
	for i in range(len(lst)):
		for j in range(i,len(lst)):
			sums[lst[i]+lst[j]].append((i,j))
	for k in sums:
		if -k in sums:
			for a,b in sums[k]:
				for c,d in sums[-k]:
					if a !=c and a!=d and b!=c and b!=d: return True

test = [1,3,6, 10,-5,-10,-2,-3]
print(foursum(test))
		
