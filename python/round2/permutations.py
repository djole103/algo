import collections 

#O(n) storage
def permutations(str1, str2):
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

def permutationsLol(str1, str2):
  return sorted(str1) == sorted(str2)
