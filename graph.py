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

def return_min(bus_id,stack=[],minVal=float('inf')):
	if bus_id < minVal: minVal = bus_id
	stack.append(bus_id)
	for bus in graph[bus_id]:
		if bus in stack: continue
		else: minVal = return_min(bus,stack,minVal)
	return minVal

insert_duplicate(4,2)
insert_duplicate(4,1)
for key,value in graph.items():
	print(key,value)
print(return_min(2))
