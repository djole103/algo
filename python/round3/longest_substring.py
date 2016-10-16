from collections import defaultdict

def clean_cache(s, cache, l, repeated):
    for i in range(l, cache[repeated]):
        del cache[s[i]]

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        maxL = 1
        curL = 1
        l = 0
        r = 1
        cache = {s[l] : l}
        
        while(r < len(s) and l < r):
            if(s[r] in cache):
                clean_cache(s, cache, l, s[r])
                l = cache[s[r]] + 1
                cache[s[r]] = r
                curL = r - l +1
            else:
                curL += 1
                maxL = max(maxL, curL)
                cache[s[r]] = r
            r += 1
                
        return maxL


def longest_substring(s):
    index = defaultdict(int)
    maxL = 0
    i = 0
    for j in range(len(s)):
        i = max(index[s[j]], i)
        maxL = max(maxL, j - i + 1)
        index[s[j]] = j + 1

    return maxL

TEST = "abcdang"
print(longest_substring(TEST))
assert longest_substring(TEST) == 6

TEST2 = "abcdcn"
print(longest_substring(TEST2))
assert longest_substring(TEST2) == 4

TEST3 = "aba"
print(longest_substring(TEST3))
assert longest_substring(TEST3) == 2
