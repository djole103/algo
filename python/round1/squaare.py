# Complete the function below.
import math

def  count_Squares( arr):
    for test in arr:
        rng = test.split()
        A = int(rng[0])
        B = int(rng[1])
        count = 0
        for num in range(A,B+1):
            sq = math.sqrt(num)
            if sq == math.floor(sq): count+=1
        print(count)
