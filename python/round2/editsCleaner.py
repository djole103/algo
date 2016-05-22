def oneAway(s1, s2):
        if abs(len(s2) - len(s1)) > 1:
                return False

        if len(s1) > len(s2):
                s1, s2 = s2, s1

        idx1 = 0
        idx2 = 0
        mismatch = False
        while (idx1 < len(s1) and idx2 < len(s2)):
                if s1[idx1] != s2[idx2]:
                        if mismatch:
                                return False
                        mismatch = True
                        if len(s1) == len(s2):
                                idx1 += 1
                else:
                        idx1 += 1
                idx2 += 1
        return True

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

