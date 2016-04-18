#kid can do 1,2 or 3 steps at a time, how many diff ways
# to climb n steps

def combSteps(n, curr=[], combos=[]):
  if n >= 3:
    combSteps(n-3, curr+[3], combos)
  if n >= 2:
    combSteps(n-2, curr+[2], combos)
  if n>= 1:
    combSteps(n-1, curr+[1], combos)
  if n == 0:
    combos.append(curr)
  return combos

def combSteps2(n, count = 0):
  if n < 0:
    return 0
  if n == 0:
    return 1
  return count + combSteps2(n-1) + combSteps2(n-2) + combSteps2(n-3)

print(combSteps2(3))
