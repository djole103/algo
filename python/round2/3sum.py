TEST = [2,5,8,10,22,32]
def threesum(nums, goal):
  for i in range(len(nums)-2):
    mid = i+1
    end = len(nums)-1
    while mid<end:
      s = sum([nums[i], nums[mid], nums[end]])
      if s == goal:
        return nums[i], nums[mid], nums[end]
      elif s < goal:
        mid += 1
      else:
        end -= 1

print(threesum(TEST, 34))
