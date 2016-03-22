import sys
TEST = [2,4,1,10,7]
SUM = 5
start = 0
finish = len(TEST) -1
s = sorted(TEST)
while start < finish:
  if s[start] + s[finish] > SUM:
    finish -=1
    continue
  if s[start] + s[finish] < SUM:
    start +=1
    continue
  print("The sum can be made with: (%d, %d)" % (s[start], s[finish]))
  sys.exit()
print("Can't make the sum :(")
