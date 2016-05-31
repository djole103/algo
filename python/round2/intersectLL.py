def getLengthiAndTail(n):
        length = 0
        while(n.next != None):
                length += 1
                n = n.next
        return length+1, tail

def advance(n, k):
        for i in range(k):
                k = k.next
        return k

def intersect(h1, h2):
        l1, t1 = getLength(h1)
        l2, t2 = getLength(h2)
        if t1 != t2:
                return False
        if l1 > l2:
                h1 = advance(h1, l1-l2)
        if l2 > l1:
                h2 = advance(h2, l2 - l1)
        while(h1 != None and h1 != h2):
                h1 = h1.next
                h2 = h2.next
        return h1
                

