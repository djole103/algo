class Interval:
	def __init__(self,a,b):
		self.start = a
		self.end = b
	def __str__(self):
		return str((self.start,self.end))

def mergeIntervals(intervals):
	sortd = sorted(intervals, key=lambda interval: interval.start)
	if len(intervals) == 1 or len(intervals) == 0: return intervals
	intvs = []
	for i in range (1,len(sortd)):
		curr = sortd[i]
		prev = sortd[i-1]
		if prev.end >= curr.start:    #FRONT OVERLAP
			if prev.end > curr.end:   #TOTAL OVERLAP
				sortd[i] = prev
			else:
				merge = Interval(prev.start,curr.end)
				sortd[i] = merge
		else:
			intvs.append(prev)
	intvs.append(sortd[-1])
	return intvs

a = Interval(1,3)
b = Interval(2,6)
c = Interval(8,10)
d = Interval(15,18)
intervals = [a,b,c,d]
merged = mergeIntervals(intervals)
for interval in merged:
	print(interval)
