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
 
        def getPathDF(row, col, path = []):
                if not validPoint(row, col):
                        return False
                p = (row, col)
                if p in path:
                        return False
                path += [p]
                atStart = p == start
                if atStart or getPathDF(row, col -1, path) or getPathDF(row -1, col, path) or getPathDF(row, col+1, path) or getPathDF(row+1, col, path):
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
        if(getPathDF(end[1], end[0])):
                return finalPath
        return None

T1 = [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]
S1 =  (0,0)
E1 = (2,2)

T2 = [ [1 for i in range (30)] for x in range(30) ]
S2 = (0,0)
E2 = (29,29)

T1 = [[1 for _ in range(25)] for _ in range(25)]
#print(findPath(T2, S2, E2))
blocked = [(19, 1), (18, 1), (19, 2), (18, 2), (12, 2), (11, 2), (10, 2), (19, 3), (18, 3), (12, 3), (11, 3), (10, 3), (7, 3), (6, 3), (19, 4), (18, 4), (12, 4), (11, 4), (10, 4), (7, 4), (6, 4), (2, 4), (1, 4), (0, 4), (21, 5), (20, 5), (19, 5), (18, 5), (12, 5), (11, 5), (10, 5), (7, 5), (6, 5), (2, 5), (1, 5), (0, 5), (23, 6), (22, 6), (21, 6), (20, 6), (19, 6), (18, 6), (12, 6), (11, 6), (10, 6), (7, 6), (6, 6), (2, 6), (18, 7), (12, 7), (11, 7), (10, 7), (7, 7), (6, 7), (4, 7), (3, 7), (2, 7), (21, 8), (18, 8), (4, 8), (3, 8), (2, 8), (21, 9), (18, 9), (21, 10), (18, 10), (16, 10), (15, 10), (21, 11), (18, 11), (16, 11), (15, 11), (4, 11), (24, 12), (21, 12), (18, 12), (16, 12), (15, 12), (10, 12), (24, 13), (23, 13), (22, 13), (21, 13), (16, 13), (15, 13), (10, 13), (24, 14), (23, 14), (22, 14), (16, 14), (15, 14), (12, 14), (11, 14), (10, 14), (9, 14), (8, 14), (24, 15), (23, 15), (10, 15), (24, 16), (10, 16), (8, 17), (6, 17), (5, 17), (4, 17), (3, 17), (2, 17), (1, 17), (0, 17), (20, 18), (19, 18), (18, 18), (17, 18), (16, 18), (15, 18), (14, 18), (10, 18), (9, 18), (8, 18), (10, 19), (9, 19), (8, 19), (20, 20), (19, 20), (18, 20), (17, 20), (16, 20), (15, 20), (14, 20), (10, 20), (9, 20), (8, 20), (5, 20), (4, 20), (3, 20), (20, 21), (19, 21), (18, 21), (17, 21), (16, 21), (15, 21), (14, 21), (8, 21), (5, 21), (4, 21), (3, 21), (20, 22), (19, 22), (18, 22), (17, 22), (16, 22), (15, 22), (14, 22), (8, 22), (4, 22), (3, 22), (2, 22), (1, 22), (0, 22), (9, 23), (8, 23), (7, 23), (6, 23), (5, 23), (4, 23), (3, 23), (2, 23), (1, 23), (0, 23), (18, 24), (17, 24), (5, 24), (4, 24)]


for (x, y) in blocked:
    T1[y][x] = 0

S1 =  (2,11)
E1 = (23,19)

for x in range(24, -1, -1):
    line = map(lambda i: str(i), T1[x])
    print(" ".join(line))

print(findPath(T1, S1, E1))

