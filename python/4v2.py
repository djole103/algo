a, b, c, d = int(input()), int(input()), int(input()), int(input())

def checkTransform(a, b, c):
        if a == c:
                return True
        if (a > 0 and b > 0 ) ^ (c > 0):
                return False

        origDiff = c - a
        if origDiff % b == 0 and ( (origDiff > 0) ^ (b < 0) ):
                return True
        newNum = a + (a+b)
        newDiff = c - newNum
        while( abs(newDiff) <= abs(origDiff) ):
                if newNum == c: 
                        return True
                if newDiff % b == 0 and ( (newDiff > 0) ^ (b < 0) ):
                        return True
                newNum = newNum + (a+b)
                newDiff = c - newNum
        return False

assert checkTransform(a, b, c) and checkTransform(b, a, d)

try:
        assert checkTransform(a, b, c)
except:
        print(a,b,c)
        print(checkTransform(a,b,c))
try:
        assert checkTransform(b, a, d)
except:
        print(b, a, d)
        print(checkTransform(b, a, d))
