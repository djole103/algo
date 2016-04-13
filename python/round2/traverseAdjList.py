insertEdge(graph, e1, e2):
  graph[e1].append(e2)
  graph[e2].append(e1)

traverseGraph(graph, startNode):
  queue = []
  visited = {}
  if startNode not in graph:
    print("why not :(")
    return
  queue.append(startNode)
  while(queue):
    startNode = queue.pop(0)
    visited[startNode] = True
    for node in graph[startNode]:
      if node in visited:
        continue
      else:
        queue.append(node)

