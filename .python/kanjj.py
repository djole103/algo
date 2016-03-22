 # [{"apple": 10, "cats": 3, "cat": 2}, {"cat": 2}], 4
# ["apple", "cats"]
stem(apple), apple
stem(cat),cats
(totalfreq,variant,variantFreq)
def aggregateDicts(dicts):
  resultDict = []
  for d in dicts:
    for k,v in d:
      totalFreq[stem(k)][0]+=v
      if v > totalFreq[stem(k)][2]:
        totalFreq[stem(k)][1] = k
        totalFreq[stem(k)][2] = v
  results =[]
 for k,v in totalFreq:
    if v[0]>treshold:
      results.append(v[1])
  return results
  def aggregateDicts(dicts):
   resultDicts = defaultdict(0)
   for d in dicts:
      for k,v in d:
        resultDicts[k]+=v
   return resultDicts  
