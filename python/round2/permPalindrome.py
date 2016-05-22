from collections import defaultdict

def permPalindrome(s):
        match = defaultdict(int)
        for l in s:
                match[l] += 1
        if len(s) % 2 == 0:
                for v in match.values():
                        if v % 2 > 0:
                                return False
        else:
                count = 0
                for v in match.values():
                        if v % 2 > 0:
                                count += 1
                        if count > 1:
                                return False
        return True

assert permPalindrome("tacocat")
