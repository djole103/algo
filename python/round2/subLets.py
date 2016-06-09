from collections import defaultdict
#given lets find smallest subarray that has them
def sub(arr, nums):
        count = 0
        d = defaultdict(int)
        for i in range(len(arr)):
                if arr[i] in nums:
                        if count == 0:
                                start = i
                        if d[arr[i]] == 0:
                                count += 1
                        d[arr[i]] += 1
                        if count == 3
                        

