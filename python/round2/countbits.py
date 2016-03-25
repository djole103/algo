#for all numbers 1 to NUM count the number of bits in it

NUM = 5

for i in range(1,NUM+1):
  count = 0
  while i:
    i = i & (i-1)
    count+=1
  print(count)
