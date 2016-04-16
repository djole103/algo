def fib(n):
  if n == 1: return 0
  if n == 2: return 1
  return fib(n-1) + fib(n-2)

fibs = {1: 0, 2: 1}
def fib2(n):
  global fibs
  if n in fibs:
    return fibs[n]
  if n-1 not in fibs:
    fibs[n-1] = fib2(n-1)
  if n-2 not in fibs:
    fibs[n-2] = fib2(n-2)
  return fibs[n-1] + fibs[n-2]
 
def fib3(n):
  if n == 1: return 0
  if n == 2: return 1

  cache = [0,1]
  for i in range(1,n-1):
    cache.append(cache[i] + cache[i-1])
  return cache[n-1]

print(fib(8))
print(fib2(8))
print(fib3(8))

