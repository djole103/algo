def solution(S):
    max_sum = 0
    current_sum = 0
    positive = False
    n = len(S)
    for i in xrange(n):
        item = S[i]
        if item < 0:
            if max_sum < current_sum:
                max_sum = current_sum
                current_sum = 0
        else:
            positive = True
            current_sum += item
    if (current_sum > max_sum):
        max_sum = current_sum
    if (positive):
        return max_sum
    return -1

print(solution([1000 for i in range(1000)]))
