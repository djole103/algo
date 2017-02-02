def max_volume(hist):
    l = 0
    r = len(hist) - 1
    high2 = 0
    volume = 0
    while(l < r):
        if(hist[l] >= hist[r]):
            high2 = max(high2, hist[r])
            volume += high2 - hist[r]
            r -= 1
        else:
            high2 = max(high2, hist[l])
            volume += high2 - hist[l]
            l += 1

    return volume

TESTS = [ 
        [ [5,2,5] , 3 ],
        [ [1,5, 2, 5, 7] , 3 ],
        [ [ 3,2,4,6,3,8,4,6], 6 ] 
]

for test, answ in TESTS:
    print(max_volume(test))
    assert max_volume(test) == answ
