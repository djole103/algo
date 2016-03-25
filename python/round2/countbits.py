#for all numbers 1 to NUM count the number of bits in it

NUM = 5

results = [0 for _ in range(NUM+1)]
for i in range(NUM+1):
  results[i] = results[i >> 1] + (i & 1)
print(results)

#for i in range(1,NUM+1):
#  count = 0
#  while i:
#    i = i & (i-1)
#    count+=1
#  print(count)
