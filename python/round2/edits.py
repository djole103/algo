#how many edits away is a string
#you can insert, delete or swap

def oneAway(s1, s2):

        if len(s1) < len(s2):
                if testInsert(s1,s2):
                        return True
        elif len(s1) > len(s2):
                if testInsert(s2, s1):
                        return True
        else:
                if testSwap(s1, s2):
                        return True
        return False

def testInsert(s1, s2):
        if len(s2) - len(s1) > 1:
                return False

        idx = -1
        mismatch = 0
        for i in range(len(s1)):
                if s1[i] != s2[i + mismatch]:
                        if mismatch:
                                return False
                        if s1[i] != s2[i+1]:
                                return False
                        mismatch = 1
                        idx = i
        return True
        #append to end
        #this isn't even necessary we know we're good already
        if not mismatch:
                return s1 + s2[-1]
        else:
                return s1[:idx] + s2[idx] + s1[idx:]
        
#a delete can be checked as an insert into the other, if one works so does the other
#common code is to see how many mismatches

def testSwap(s1, s2):
        idx = -1
        mismatch = 0
        for i in range(len(s1)):
                if s1[i] != s2[i]:
                        if mismatch:
                                return False
                        mismatch = 1
                        idx = i
        return True
        #if you wanted to do the swap
        return s1[:idx] + s2[idx] + s1[idx+1:]

t1a = "ac"
t1b = "abc"
t2a = "acc"
t2b = "abb"
t3a = "abc"
t3b = "abcd"
t4a = "afc"
t4b = "abc"
t5a = "fjsdlkfj"
t5b = "asdfkjlks"

assert oneAway(t1a, t1b)
assert not oneAway(t2a, t2b)
assert oneAway(t3a, t3b)
assert oneAway(t4a, t4b)
assert not oneAway(t5a, t5b)
