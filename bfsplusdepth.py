def breadthfirst(adjlist):
	qd = {}
	q = []
	for lst in adjlist:
		for node in lst:
			q.append(node)
			qd[node] = True

def depthfirst(adjlist):
	
