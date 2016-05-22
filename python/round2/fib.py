def fib(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	a, b = 0,1
	for i in range(3, n+1):
		a, b = b, a+b
	return b
	
TEST = [0,1,1,2,3,5,8,13,21]
for i,t in enumerate(TEST):
	try:
		assert fib(i+1) == t
	except:
		print("Oh no D:",i, fib(i+1))
