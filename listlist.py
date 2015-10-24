#list of lists of (id, string)
#group by id from all lists
from collections import defaultdict

def groupBy(lists):
	grouped = defaultdict(list)
	for lst in lists:
		for ID,string in lst:
			grouped[ID].append(string)
	return grouped

lst = [[(1,"a"),(2,'b'),(1,'aaa')],[(1,'aaa'),(3,'cccc'),(2,'bbb')]]
result = groupBy(lst)
for k,v in result.items():
	print(v)
