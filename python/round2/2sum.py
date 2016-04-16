TEST = [2, 4, 5, 10, 30, 32]

def twosum(nums, goal):
  nums.sort()
  left = 0
  right = len(nums) -1
  while left < right:
    curr_sum = nums[left] + nums[right]
    if curr_sum == goal:
      return nums[left], nums[right]
    if curr_sum < goal:
      left += 1
    else:
      right -= 1

print(twosum(TEST, 15))
