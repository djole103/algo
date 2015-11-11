FIBONACCI = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368]

TRIBONACCI = [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415, 223317, 410744]

lst = [0,0,1]
def tribonacci(n):
    global lst
    if n<0: return 0
    if n == 0: return 0
    if n == 1: return 0
    if n == 2: return 1
    if len(lst)-1 >= n: return lst[n]
    idx = len(lst) -1
    for i in range(idx,n):
        lst.append(lst[i] + lst[i-1] + lst[i-2])
    return lst[n]
    
#for n in range(len(TRIBONACCI)):
#    print(tribonacci(n))
#    assert tribonacci(n) == TRIBONACCI[n]
   

def kbonacci(k,n):
    print(k, n)
    if n < k-1: return 0
    if n == k-1: return 1
    lstK = [0 for i in range(k-1)]
    lstK.append(1)
    for i in range(k-1,n):
        lstK.append(sum(lstK[i-(k-1):i+1]))
    return lstK[n]
    
for n in range(len(TRIBONACCI)):
    assert kbonacci(3, n) == TRIBONACCI[n]
    
