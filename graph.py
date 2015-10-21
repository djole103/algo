graph = {}

def insert_duplicate(id1,id2):
	if id1 in graph:
		graph[id1].append(id2)
	else: 
		graph[id1] = [id2]
	if id2 in graph:
		graph[id2].append(id1)
	else:
		graph[id2] = [id1]

def return_minDEPTH(bus_id,visited={},minVal=float('inf')):
	if bus_id < minVal: minVal = bus_id
	visited[bus_id] = True
	for bus in graph[bus_id]:
		if bus in visited: continue
		else: minVal = return_minDEPTH(bus,visited,minVal)
	return minVal

def return_minBFS(bus_id,q=[],minVal=float('inf'),queued={}):
	queued[bus_id] = True
	if bus_id < minVal: minVal = bus_id
	for bus in graph[bus_id]:
		if bus in queued: continue
		q.append(bus)
		queued[bus] = True
	while q:
		bus = q.pop(0)
		minVal = return_minBFS(bus,q,minVal,queued)
	return minVal

insert_duplicate(4,2)
insert_duplicate(4,1)
insert_duplicate(1,0)
insert_duplicate(0,5)
insert_duplicate(0,6)
insert_duplicate(0,7)
insert_duplicate(6,5)
insert_duplicate(5,11)
insert_duplicate(6,12)
insert_duplicate(2,11)
insert_duplicate(2,12)
for key,value in graph.items():
	print(key,value)
print(return_minDEPTH(2))
