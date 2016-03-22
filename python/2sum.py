def twosum(lst, goal):
	if len(lst) <=1: return False
	end = len(lst) -1
	start = 0
	lst = sorted(lst)
	while(start<end):
		if lst[start] + lst[end] > goal:
			end-=1
		elif lst[start] + lst[end] < goal:
			start+=1
		else:
			return True
	return False

print(twosum([3,5,10,2,6,7],11))
