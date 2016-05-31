def kUniq(nums):
        o_start = 0
        o_end = 0
        start = 0
        end = 0
        count = 0
        d = {}
        for i in range(len(nums)):
                if nums[i] not in d:
                        count += 1
                        d[nums[i]] = True 
                if count == 3:
                        pass

def BrF(nums):
        k = 0
        bestLength = 99999
        bestS = 0
        bestE = 0
        while(k+2 < len(nums)):
                d = {}
                start = -1
                end = -1
                count = 0
                for i in range(k, len(nums)):
                        if nums[i] not in d:
                                count += 1
                                d[nums[i]] = True
                                if start == -1:
                                        start = i
                                elif count == 3:
                                        end = i
                                        break
                if (end != -1) and (end - start < bestLength):
                        bestLength = end - start
                        bestS = start
                        bestE = end
                k += 1
        return bestLength + 1

def eachWind(nums, k):
        d = {}
        results = []
        distCount = 0
        cur = []
        for i in range(k):
                if nums[i] not in d:
                        d[nums[i]] = 1
                        distCount += 1
                else:
                        d[nums[i]] += 1
                cur.append(nums[i])
        results.append(distCount)

        for i in range(1, len(nums) - (k-1)):
                if cur[0] in d:
                        if d[cur[0]] == 1:
                                del d[cur[0]]
                                distCount -= 1
                cur = nums[i:i+k]
                if cur[-1] not in d:
                        d[cur[-1]] = 1
                        distCount += 1
                else:
                        d[cur[-1]] += 1
                results.append(distCount)
        return results

TESTS_1 = {4 : [1,2,2,3,3],
         3 : [1,1,1,2,3]}

TESTS_2 = [[3,2,2], [1,2,3,3,4]]

for answer, test in TESTS_1.items():
        result = BrF(test)
        try:
                assert result == answer
        except:
                print("wow i suck: %i" % result, answer)

print(eachWind([1,2,3,3,4], 3))
#assert countDistinctInSizeK(TESTS_2[1], 3) == TESTS_2[0]
