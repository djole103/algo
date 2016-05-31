def volume(graph):
	calc = 0
	left = 0
	volume = 0
	right = len(graph) -1
	while(left < right):
		if graph[left] < graph[right]:
			calc = max(calc, graph[left])
			volume += calc - graph[left]
			left += 1
		else:
			calc = max(calc, graph[right])
			volume += calc - graph[right]
			right -= 1
	return volume

def volume2(graph):
        calc = 0
        left = 0
        right = len(graph) - 1
        volume = 0
        while(left < right):
                if graph[left] < graph[right]:
                        calc = max(calc, graph[left])
                        volume += calc - graph[left]
                        left += 1
                else:
                        calc = max(calc, graph(right))
                        volume += calc - graph[right]
                        right -= 1
TEST = [3,1,3]

try:
	assert volume(TEST) == 2
except:
	print(volume(TEST))		
