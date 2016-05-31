def maxSubArray(nums):
        mxToHere = 0
        mxOverall = 0
        for i in range(len(nums)):
                mxToHere = max(0, mxToHere + nums[i])
                mxOverall = max(mxToHere, mxOverall)
        return mxOverall

TESTS = [([3,4,-20], 7), ([-2,3,4,-8,10,-9,10], 11) ]

count = 1
for t in TESTS:
        if maxSubArray(t[0]) == t[1]:
                print("%i: Passed")
        else:
                print("%i: Failed")
                print("Got: %i" % (maxSubArray(t[0])))
        count += 1
