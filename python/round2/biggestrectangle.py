def BiggestRectangle(graph):
	running = graph[0]
	maxVol = 0
	runningVol = 0
#	for i in range(len(graph)):
#		if graph[i]

def FindMaxLevel(graph):
	return max(graph)

def BRBruteForce(graph):
	maxRec = 0
	maxLevel = FindMaxLevel(graph)
	for i in range(1, maxLevel+1):
		recs = BRLevel(i, graph)
		localMax = max(recs)
		if localMax > maxRec:
			maxRec = localMax
	print("MAX REC IS:", maxRec)
	return maxRec

def BRLevel(level, graph):
	start, end = 0, 0
	recs = []
	curr = 0
	for i in range(len(graph)):
		print(i, level)
		if graph[i] >= level:
			curr += level
			end += 1
		else:
			if curr > 0:
				#want to append start and too
				recs.append(curr)
			start = i+1
			end = i+1
			curr = 0
	if curr > 0:
		recs.append(curr)
	print("RECS ARE:", recs)
	return recs

def DandConq(graph):
	pass

TESTS = [ ([1, 1, 2, 2, 1, 1, 1], 7),
	  ([1, 1, 2, 2, 2], 6),
	  ([2,2,6,]

for test in TESTS:
	assert BRBruteForce(test[0]) == test[1]


