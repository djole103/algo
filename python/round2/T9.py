d = {   1 : ['A','B','C'],
        2 : ['D','E','F'],
        3 : ['G','H','I'],
        4 : ['J','K','L'],
        5 : ['M','N','O','P'],
        6 : ['Q','R','S'],
        7 : ['T','U','V'],
        8 : ['X','Y','Z']}

def T9conversion(numsRemaining, word = "", results = []):
        global d
        if len(numsRemaining) == 0:
                return results + [word]
        n = numsRemaining[0]
        for l in d[n]:
                word += l
                results = T9conversion(numsRemaining[1:], word, results)
                print("DEBUG", word, results)
                word = word[:-1]
        print(results)
        return results

#TEST = [1,2]
#print(T9conversion(TEST))

def allStr(lRem, word = "", results = []):
        if len(lRem) == 0:
                return results + [word]
        for i in range(len(lRem)):
                word += lRem[i]
                results = allStr(lRem[:i] + lRem[i+1:], word, results)
                word = word[:-1]
        return results
        
TEST = ['a', 'b', 'c']
print(allStr(TEST))
