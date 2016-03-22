def threesum(lst,goal):
	if len(lst) <= 2: return False
	lst = sorted(lst)
	print(lst)
	start = 0
	mid = len(lst)-2 
	end = len(lst)-1
	while (start<mid and mid<end): 
		print(start,mid,end)
		if lst[start]+lst[mid]+lst[end] > goal:
			if mid< end -1: #not beside eachother
				if lst[mid]-lst[mid] <= lst[end]-lst[end -1]:
					mid-=1
				else:
					end-=1
			else:
				mid-=1
		elif lst[start]+lst[mid]+lst[end] < goal: 
			start+=1
		else:
			return (lst[start],lst[mid],lst[end])
	return False

print(threesum([2,5,3,7,10,8,20,4],18))
