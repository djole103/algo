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

results = []
def allPermutations(str):
  if str == "": return str
  perms = []
  for i in range(len(str)):
    perms += [ str[i]+x for x in allPermutations(str[:i] + str[i+1:])]
  return perms

print(allPermutations("abc"))
