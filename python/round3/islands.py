
MOVES = [ [1, 0],
          [-1, 0],
          [0, 1],
          [0, -1],
          [1, 1],
          [-1, -1],
          [1, -1],
          [-1, 1]
]

visited = {} 

#in: tuple
#out: tuple
def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

#in: [[]], ()
def valid_coord(grid, p):
    max_y = len(grid) -1 
    max_x = len(grid[0]) -1
    return not (p[0] < 0 or p[0] > max_x or p[1] < 0 or p[1] > max_y)

#[[]], int, int
def neighbours(grid, x, y):
    for move in MOVES:
        if valid_coord(grid, add((x,y), move)):
           yield add((x,y), move)

#[[]], int, int
def identify_island(grid, x1, y1):
    global visited
    if not grid[y1][x1]:
        return []
    island = []
    points = [(x1,y1)]
    while(points):
        x, y = points.pop() 
        if grid[y][x] and (x, y) not in visited:
            island.append( (x,y) )
            visited[(x,y)] = True
            for n in neighbours(grid, x, y):
                if n not in points and n not in visited:
                    points.append(n) 
    return island
    
#[[]]
def find_islands(grid):
    global visited
    islands = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x,y) in visited:
                continue
            island = identify_island(grid, x, y)
            visited[(x, y)] = True
            if island:
                islands.append(island)
    return islands

TEST = [ 
            [1, 1, 1, 0, 0, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0] 
] 
#   [ [ (0,0), (0, 1), (0,2) , (1,0), (1,1), (2, 0) ],
#   [ (4, 1), (3, 2), (4,2), (5, 2), (4, 3)]

TEST2 = [
            [1,1],
            [1,0]
]


TEST3 = [
            [1,0,0],
            [1,0,1],
            [0,0,1]
]

for island in find_islands(TEST):
    print(island)
