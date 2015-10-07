def sel_iter(lst, start):
	for i in range(start,len(lst)):
		yield lst[i]
	for i in range(start):
		yield lst[i]

lst = list(range(10))
for item in sel_iter(lst, 3):
	print(item)
	print(lst)
