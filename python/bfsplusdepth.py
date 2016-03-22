#def breadthfirst(adjlist):
#	qd = {}
#	q = []
#	for lst in adjlist:
#		for node in lst:
#			q.append(node)
#			qd[node] = True

#def depthfirst(adjlist):

#what if you have duplicates? how do i identify nodes
def lstparent(i,lst):
	#bfs for parent list
	qd = {i:True}
	q = [i]
	while(q):
		i = q.pop(0)
		print(i,end='')
		for child in lst[i]:
			if child not in qd:
				q.append(child)
				qd[child] = True
	
test = [ [1,3],
		 [5],
		 [],
		 [4],
		 [],
		 [] ]	

lstparent(0,test)		
