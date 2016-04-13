TEST = [1, 4, 6, 7, 9, 20, 26, 29, 30, 33] 
TEST_DIFF = 3

def difference(nums, diff):
  left = 0
  right = len(nums) - 1

  while(left < right):
    if nums[right] - nums[left] == diff:
      print(nums[right], nums[left])
#    elif nums[right] - nums[left] < diff:
      

def differenceBrute(nums, diff):
  for i in range(len(nums)-1):
    for j in range(i, len(nums)):
      curr_diff = nums[j] - nums[i]
      if curr_diff > diff:
        break
      if curr_diff == diff:
        print(i,j,nums[j], nums[i])


differenceBrute(TEST, TEST_DIFF)
