def minSubArrayLen(s,nums):
	total = 0
	right = 0
	left = 0
	minLen = float('inf')

	while(right<len(nums):
		total+= nums[right]
		while(total >= s):
			if right-left+1 < minLen:
				minLen = right-left+1
			total -= nums[left]
			left+=1
		right+=1
	
	if minLen == float('inf'): return 0
	return minLen +1
