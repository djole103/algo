from Queue import PriorityQueue

def heuristic(a, b):
  x1, x2 = a, b
  y1, y2 = a, b
  return abs(x1 - y1) + abs(y1 - y2)

def Astar(start, goal):
  visited = {}
  notVisited = [start]
  cameFrom = {}
  cameFrom[start] = None
  #from start to node
  gScore = {}
  gScore[start] = 0
  #from start to this node and to goal
  fScore = {}
  fScore[start] = 0

  while notVisited:
    current = notVisited.pop(0)
    if current == goal: break
    vistied[current] = True

    for nxt in neighbours(current):
      new_cost = gScore[current] + cost(nxt)
      if nxt not in gScore or new_cost <  gScore[nxt]:
        gScore
  

