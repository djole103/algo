X = 6

def lessThanX(y):
    return y < X

def findX():
    i = 0
    if lessThanX(i):
        while(lessThanX(i)):
            i+=1
        return i
    else:
        while(not lessThanX(i)):
            i-=1
        return i+1

def findXbinary():
    i = 1 
    if (lessThanX(i)):
        while(lessThanX(i*2)):
            i*=2
        MIN = i
        MAX = i*2
        MID = MAX//2
        
        while(MIN!=MAX):
            while(lessThanX(MID)):
                print("MIN: %d\nMID: %d\nMAX:%d\n\n" % (MIN,MID,MAX))
                MIN = MID
                MID = MID + MID//2
            while(not lessThanX(MID)):
                MAX = MID
                MID = MID//2
        return MIN
findXbinary()
