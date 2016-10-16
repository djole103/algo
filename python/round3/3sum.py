def s(nums, i, l, r):
    return nums[i] + nums[l] + nums[r]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while(l < r):
                sm = s(nums, i, l, r)
                if sm == 0:
                    if [nums[i], nums[l], nums[r]] not in result:
                        result.append([nums[i], nums[l], nums[r]])
                    r -= 1
                elif sm < 0:
                    l += 1
                else:
                    r -= 1
        return result
