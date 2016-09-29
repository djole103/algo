import heapq
def maximumAmount(scalpers, k):
        tot = 0
        for i in range(k):
                heapq._heapify_max(scalpers)
                tot += scalpers[0]
                scalpers[0] -= 1

        return tot

TEST = [4,2,3]
#assert maximumAmount(TEST, 3) == 4+3+3

try :
        assert maximumAmount(TEST, 5) == 4+3+3+2+2
except:
        print(maximumAmount(TEST, 5))
