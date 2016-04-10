TEST = [ [1,5], [8,10], [4,7], [9,10] , [45,100]]

def merge(intvs):
  intvs = sorted(intvs, key= lambda x: x[0])
  result = []
  tmp = intvs[0]
  for i in range(1, len(intvs)):
    if intvs[i][1] <= tmp[1] + 1:
      continue
    if intvs[i][0] <= tmp[1] + 1:
      tmp[1] = intvs[i][1]
    else:
      result.append(tmp)
      tmp = intvs[i]
  if len(result) == 0 or result[-1][1] < tmp[1]:
    result.append(tmp)
  return result

print(merge(TEST))
