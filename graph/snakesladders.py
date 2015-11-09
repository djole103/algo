#limitations:
# -if ladders overlap it might not pick it up or itll take 2 loops to register
# -if taking a snake somehow benefits reaching the goal
# -if a ladder connects to a snake
# -doesn't dodge snakes at all lol
# -should probably sort ladders somewhere

def bestLadder(position,ladders):
    farthest = max(ladders, key= lambda x: x[1])
    best = farthest
    goal = farthest[1]
    fewestMoves = calcMoves(position,farthest[0])
    for ladder in ladders:
        moves = calcMoves(position, ladder[0]) + calcMoves(ladder[1],farthest[1])
        if moves < fewestMoves:
                fewestMoves = moves
                best = ladder
    return best        
        	
def calcMoves(position,goal):
    difference = goal - position
    remainder = difference % 6
    if remainder:
        return (difference - remainder)/6 + 1
    else: 
        return (difference - remainder)/6
   
numTests = int(input())

for i in range(numTests):
    numLadders = int(input())
    ladders = []
	#read ladders
    for n in range(numLadders):
        ladders.append(tuple(map(int, (i for i in input().split()))))
    numSnakes = int(input())
    snakes = []
    for s in range(numSnakes):
        snakes.append(tuple(map(int, (i for i in input().split()))))
    moves = 0
    position = 1
    while(position!=100):
        if ladders:
            ladder = bestLadder(position,ladders)
            moves += calcMoves(position,ladder[0])
            position = ladder[1]
            ladders = list(filter(lambda x: x[0] > position, ladders))
        else:
            moves += calcMoves(position,100)
            position = 100
    print(int(moves))
