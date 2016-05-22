CONDITIONS = [(1,0), (-1,0), (0,1), (0,-1)]

TEST_GRID = [ [1,1,0],
              [1,0,0],
              [0,0,1]]

def ValidNeighbours(grid, row, column):
    global CONDITIONS
    for condition in CONDITIONS:
        n_row, n_col = row+condition[0], column+condition[1]
        if n_row >= len(grid) or n_col >= len(grid[row]):
            continue
        yield n_row, n_col

def CheckNeighbours(grid, row, column):
    for row, column in ValidNeighbours(grid, row, column):
        if grid[row][column] == 1:
            yield row, column 


def FindIslands(grid):
    islands = []
    visited = {}
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if (row, column) not in visited:
                if grid[row][column] == 1:
                    islands.append(ExploreIsland(grid, visited, row, column))
                visited[(row, column)] = True
    return islands

def ExploreIsland(grid, visited, row, column):
    island = [(row,column)]
    toVisit = [(row, column)]
    while toVisit:
        row, column = toVisit.pop(0)
        if (row, column) in visited:
            continue
        for neighbour in CheckNeighbours(grid, row, column):
            toVisit.append(neighbour)
            island.append(neighbour)
        visited[(row, column)] = True
    return island

if __name__ == "__main__":
    print(FindIslands(TEST_GRID))
