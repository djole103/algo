def threesum(lst,goal):
	results = []
	if len(lst) <= 2 : return False
	lst = sorted(lst)
	print(lst)
	for sep in range(len(lst)-3):
		start = sep+1
		end = len(lst)-1
		a = lst[sep]
		while(start<end ):
			if a+lst[start]+lst[end] > goal: end-=1
			elif a+lst[start]+lst[end] < goal: start+=1
			else: 
				results.append((a,lst[start],lst[end]))
				if(lst[start+1] - lst[start] < lst[end] - lst[end-1]):
					start+=1
				else: end-=1
	return results

test = [5,4,10,20,3,7,9,12,0]
print(threesum(test,19))
