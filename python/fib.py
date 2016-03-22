tribonacci = [0,0,1,1,2,4,7,13,24]

def fib1(n):
	a,b = 0,1
	for i in range(n-1):
		a,b = b, a+b
	return a

def fib2(n):
	if n==1 or n==2: return 1
	return fib(n-1) + fib(n-2)

a,b = 0,1
def fib3():
	global a,b
	while True:
		a,b = b, a+b
		yield a

def trib(n):
    a,b,c= 0,0,1
    for i in range(n-1):
        a,b,c = b,c,a+b+c
    return a

def kbin(n,k):
    base = [0 for i in range(k-1)]
    base.append(1)
    if n <= k:
        return base[n-1]
    for i in range(k,n):
        tmp = sum(base[i-k:i])
        base = [base[x+1] for x in range(i-k,i-1)]
        base.append(tmp)
    return base[-1]

for i in range(1,7):
    print(kbin(i,3))
    assert kbin(i,3) == tribonacci[i-1]
