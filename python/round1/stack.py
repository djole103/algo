numOps = int(input())

def push(move,stack):
	print(move[1])
	stack.append(int(move[1])

def pop(move,stack):
	if stack.empty(): print("EMPTY")
	else: 
		print(stack[-2])
		stack[-1] = None
	
def inc(move,stack):
	stack[-1:-move[1]] += move[2]
	print(stack[-1])

for op in range(numOps):
	move = input().split()
	move[0](move,stack)
