numTestCases = int(input())

def sel_iter(lst,start):
	for i in range(start,len(lst)):
		yield lst[i]
	for i in range(start):
		yield lst[i]

def findDist(lst, start):

for test in range(numTestCases):
    numNodes,numEdges = tuple(map(int,input().split()))
    adj = [[] for node in range(numNodes)]
    for edge in range(numEdges):
        node1,node2 = tuple(map(int,input().split()))
        adj[node1].append(node2)
        adj[node2].append(node1)
	start = int(input())
	dist = {i:-1 for i in range(numNodes)}
	for node in range(numNodes):
		if node+1 in adj[start-1]:
			dist[node+1] = 6
		else:
			distNode = float('inf')
			for link in adj[start-1]:
				tempDist = findDist(link,node+1)
				if tempDist < distNode: distNode = tempDist
			if distNode == float('inf'): break
			else: dist[node+1] = distNode
