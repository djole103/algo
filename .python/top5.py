
top = [None for _ in range(5)]


def insert(num):
	global top
	for idx in range(5):
		if top[idx]:
			if num > top[idx]:
				top = top[:idx] + [num] + top[idx+1:-1]
				return
		else: top[idx] = num

insert(1)
insert(2)
insert(4)
insert(6)
insert(3)
insert(20)
insert(7)
