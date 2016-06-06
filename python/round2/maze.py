from queue import PriorityQueue
import math

def findPath(maze, start, end):
        if (maze is None or len(maze) == 0):
                return None
        finalPath = []
        failedPoints = set()
        width = len(maze[0]) -1
        height = len(maze) -1

        def validPoint(row, col):
                if ((col < 0 or col > width) or (row < 0 or row > height) or (not maze[row][col])):
                        return False
                if (row, col) in failedPoints:
                        return False
                return True

        def nextVisits(path, p):
                visits = [(p[0] -1, p[1]),
                          (p[0]+1, p[1]),
                          (p[0], p[1]-1),
                          (p[0], p[1]+1)]
                return [v for v in visits if v not in path and validPoint(v[1], v[0])]

        def heur(p):
                return math.sqrt((p[0] - start[0])**2 + (p[1] - start[1])**2)
 
        def getPathDF(row, col):
                if not validPoint(row, col):
                        return False
                p = (row, col)
                atStart = p == start
                if atStart or getPathDF(row, col -1) or getPathDF(row -1, col) or getPathDF(row, col+1) or getPathDF(row+1, col):
                        finalPath.append(p)
                        return True
                failedPoints.add(p)
                return False

        def getPathBF(row, col):
                nonlocal finalPath
                e = (row, col)
                path = [e]
                q = [path]
                while(q):
                        path = q.pop()
                        p = path[-1]
                        col, row = p
                        if p == start:
                                finalPath = path
                                return True
                        nextPoints = nextVisits(path, p)
                        for v in nextPoints:
                                q.append(path + [v]) 
                return None

        def getPathA(row, col):
                nonlocal finalPath
                s = (row, col)
                if not validPoint(row, col):
                        return False
                path = [s]
                q = PriorityQueue()
                q.put((heur(s) + 1, path))
                while(q):
                        score, path = q.get()
                        p = path[-1]
                        if p == start:
                                finalPath = path
                                return True
                        #col, row = p
                        nextPoints = nextVisits(path, p)
                        nextPaths = [(heur(x) + len(path), path + [x]) for x in nextPoints]
                        for np in nextPaths:
                                q.put(np)
                return False

        #Choose Depth First (DF), Breadth First (BF) or A* (A) for which path calc algo to use
        if(getPathA(end[1], end[0])):
                return finalPath
        return None

T1 = [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]
S1 =  (0,0)
E1 = (2,2)

print(findPath(T1, S1, E1))
