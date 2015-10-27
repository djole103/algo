def fib1(num):
	a,b = 1,1
	for i in range(n-1):
		a,b = b, a+b
	return a

def fib2(num):
	if n==1 or n==2: return 1
	return fib(n-1) + fib(n-2)

a,b = 0,1
def fib3():
	global a,b
	while True:
		a,b = b, a+b
		yield a
