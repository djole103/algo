#this is bad, you should insert from the shorter list to do less operations but whatever
def mergeSortedLists(l1, l2):
        if l2[0] < l1[0]:
                l1, l2 = l2, l1
        p1 = 0
        p2 = 0
        while(p2 < len(l2)):
                if p1 == len(l1):
                        l1 = l1 + l2[p2:]
                        return l1
                if l2[p2] <= l1[p1]:
                        l1 = l1[:p1] + [l2[p2]] + l1[p1:]
                        p1 += 1
                        p2 += 1
                else:
                        p1 += 1
        return l1

l1 = [1,5,8,20]
l2 = [3, 10]

print(mergeSortedLists(l1, l2))
