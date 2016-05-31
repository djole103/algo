def maxProfit(nums):
        if len(nums) < 2:
                return 0
        m = nums[0]
        profit = 0
        for i in range(1, len(nums)):
                if nums[i] < m:
                        m = nums[i]
                if nums[i] - m > profit:
                        profit = nums[i] - m
        return profit

def multipleBuys(nums):
        if len(nums) < 2:
                return 0
        profit = 0
        mx = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
                if nums[i] > mx:
                        mx = nums[i]
                if nums[i] < mx:
                        profit += mx - nums[i]
        return profit

def Kbuys(nums, k):
        pass

TEST = [4,5,2,10,20,5]
assert maxProfit(TEST) == 18
