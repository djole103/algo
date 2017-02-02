def lent(t):
    return t[1] - t[0]

def updmx(mx, t):
    if lent(t) > lent(mx):
        return t
    return mx

def lgst_intvl(tuples):
    tuples =  sorted(tuples)
    mx = [tuples[0][0], tuples[0][1]]
    mx_here = mx
    for i in range(1, len(tuples)):
        if tuples[i][0] > mx_here[1]:
            mx = updmx(mx, mx_here)
            mx_here = list(tuples[i])
        else:
            mx_here[1] = max(mx_here[1], tuples[i][1])
    mx = updmx(mx, mx_here)
    return mx

case1 = [(0,2), (4,5), (5,9)]
assert lgst_intvl(case1) == [4,9]
