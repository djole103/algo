def isSubarray(main, sub):
        left = 0
        right = len(main) - 1
        while(left < right):
                if main[left] != sub[0]:
                        left += 1
                if main[right] != sub[-1]:
                        right -= 1
                if main[left] == sub[0] and main[right] == sub[-1]:
                        if right - left < len(sub):
                                pass

def isSubbary(main, sub):
        def subHelp(m):
                left = 0
                right = len(m) -1
                if main[left] != sub[0]:
                        left += 1
                if main[right]:
                        pass

def brF(main, sub):
        for i in range(len(main) - len(sub)):
                for j in range(len(sub)):
                        if main[i+j] != sub[j]:
                                break
                else:
                        return True

def good(main, sub):
        pass
