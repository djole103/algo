def maxSubArray(nums):
  maxSub = -99999999
  subarray = None
  for left in range(len(nums)):
    right = len(nums)
    while(right-1 > left):
      if sum(nums[left:right]) >= maxSub:
        maxSub = sum(nums[left:right])
        subarray = (left, right-1)
      right -=1
    if nums[left] > maxSub:
      maxSub = left
      subarray = (left, left)
  return maxSub, subarray

def printAllSubArrays(nums):
  for left in range(len(nums)):
    right = len(nums)
    while(right-1 > left):
      print(nums[left:right])
      right -=1
    print nums[left]

#printAllSubArrays([1,2,3,4,5])
#print(maxSubArray([1,2,3,-4,2]))

def smarterSubArray(nums):
  if not nums: return 0
  max_ending_here = nums[0]
  rng_here = [0,0]
  max_overall = nums[0]
  rng_overall = [0,0]

  for i in range(1, len(nums)):
    if nums[i] + max_ending_here > nums[i]:
      max_ending_here = nums[i] + max_ending_here
      rng_here[1] = i
    else:
      max_ending_here = nums[i]
      rng_here = [i,i]
    if max_ending_here > max_overall:
      max_overall = max_ending_here
      rng_overall[:] = rng_here[:]
  return max_overall, rng_overall

print(smarterSubArray([1,2,3,-4,2]))
