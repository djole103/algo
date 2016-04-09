import collections 

#O(n) storage
def isPermutation(str1, str2):
    if str1 == None or str2 == None: return False
    d = collections.defaultdict(int)
    for l in str1:
        d[l] +=1
    for l in str2:
        if l not in d:
            return False
        d[l] -= 1
        if d[l] < 0:
            return False
    return True

def isPermutationLol(str1, str2):
  return sorted(str1) == sorted(str2)

def allPermutations(str):
  if len(str) <= 1: return str
  perms = []
  for i in range(len(str)):
    perms += [ str[i]+x for x in allPermutations(str[:i] + str[i+1:])]
  return perms

print(allPermutations("abc"))

def swapPermute(xs, low=0):
  if low+1 >= len(xs):
    yield xs
  else:  
    for p in swapPermute(xs, low+1):
      yield p
    for i in range(low+1,len(xs)):
      xs[low], xs[i] = xs[i], xs[low]
      for p in swapPermute(xs, low+1):
        yield p
      xs[low], xs[i] = xs[i], xs[low]

for i in swapPermute(['a','b','c']):
  print(i) 
