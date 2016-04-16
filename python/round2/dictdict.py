from collections import defaultdict

TEST = [ {'a': 1, 'b': 2}, {'a':2, 'c':5}, {'a':1, 'b': 5} ]

def mergeDicts(dicts):
  result = defaultdict(list)
  for d in dicts:
    for k,v in d.iteritems():
      if k in result and v in result[k]:
        pass
      else:
        result[k].append(v)
  return result

print(mergeDicts(TEST))

    
