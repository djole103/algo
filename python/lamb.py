def inc(n): return lambda x: x+n

f = inc(2)
for i in range(5):
	print(inc(i)(5))
