def maxSum(nums):
        s = 0
        for i in range(0, len(nums)):
                s = max(s, s+nums[i])
        if s == 0:
                s = min(nums)
        return s

TEST = [i for i in range (6)]
print(maxSum(TEST))

