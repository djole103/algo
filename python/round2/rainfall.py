def Volume(graph):
	left = [graph[0] for i in range(len(graph))]
	right = [graph[-1] for i in range(len(graph))]
	
	for i in range(1, len(graph)):
		left[i] = max(left[i-1], graph[i])

	for i in range(len(graph)-2, -1, -1):
		right[i] = max(graph[i], right[i+1])

	volume = 0
	for i in range(len(graph)):
		volume += min(left[i], right[i]) - graph[i]
	return volume

def Volume2(graph):
	volume = 0
	lowlevel = 0
	left = 0
	right = len(graph) -1
	while(left < right):
		if graph[left] < graph[right]:
			lowlevel = max(lowlevel, graph[left])
			volume += lowlevel - graph[left] 
			left += 1
		else:
			lowlevel = max(lowlevel, graph[right])
			volume += lowlevel - graph[right]
			right -= 1
	return volume

TEST = [2,6,4,4,6] 
TEST2 = [2,6,4,4,6,2,8,2,9,1]
assert Volume2(TEST) == 4
assert Volume2(TEST2) == 14
