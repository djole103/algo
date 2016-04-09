import heapq

TEST = [2,3,1,5,3,80,30,23,10,2,43,100,32,45,54,30,99]
stream = TEST  #constantly filling in real scenario
top5 = []
while len(top5) < 5:
  if stream:
    heapq.heappush(top5, stream.pop(0))
    print(top5)
#while 1:
while stream:
  new = stream.pop(0)
  if new > top5[0]:
    heapq.heappushpop(top5, new)
    print(top5)
