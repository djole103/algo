def inter(l1, l2):
        results = []
        d = {}
        for i in l1:
                d[i] = True
        for i in l2:
                if i in d:
                        results.append(i)
        return results

def interNoExtra(l1, l2):
        l1.sort()
        l2.sort()
        p1 = 0
        p2 = 0
        results =[]
        while(p1 < len(l1) and p2 < len(l2)):
                if l1[p1] == l2[p2]:
                        results.append(l1[p1])
                        p1 += 1
                        p2 += 1
                elif l1[p1] < l2[p2]:
                        p1 += 1
                else:
                        p2 += 1
        return results
