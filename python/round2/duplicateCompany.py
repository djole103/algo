#both ids map to eachother
def insert_duplicate(graph, id1, id2):
  graph[id1].append(id2)
  graph[id2].append(id1)

def smallest_id(graph, id):
  if id in graph:
    small = graph[id][0]
  for otherID in graph[id]:
    if otherID < id:
      small = otherID
  return small

 
