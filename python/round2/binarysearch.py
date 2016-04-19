def bsearch(arr, val):
  mid = len(arr)/2
  while(arr[mid] != val):
    if arr[mid] < val:
      mid = mid + mid/2
    else:
      mid = mid - mid/2
  print(mid)

TEST = [2,5,10,22,30,33,34,35]

bsearch(TEST, 30)

