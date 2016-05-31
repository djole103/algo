def twosum(nums, s):
        left = 0
        right = len(nums) -1
        nums.sort()
        while(left < right):
                n = nums[left] + nums[right]
                if n == s:
                        return True
                if n > s:
                        right -= 1
                else:
                        left += 1

TEST = [1,3,7,20]
assert twosum(TEST, 10)
