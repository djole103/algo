def merge_intervals(intervals):
    intervals = sorted(intervals)
    i = 0 
    while(i+1 < len(intervals)):
        if (intervals[i][1] >= intervals[i+1][0]):
            
            if (intervals[i][1] < intervals[i+1][1]):
                intervals[i][1] = intervals[i+1][1]

            intervals.pop(i+1)

        else:
            i += 1

    return intervals


TEST = [ [1,3], [4,5], [4,5], [5, 6], [9, 12], [10, 15] ]
ANSWER = [ [1,3], [4,6], [9, 15] ]

assert merge_intervals(TEST) == ANSWER
