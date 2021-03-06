from itertools import groupby

class BNode:
        def __init__(self, val):
                self.val = val
                self.left = None
                self.right = None
        
def printTreeL(node):
        level = 0
        q = [[node, level]]
        levels = []
        while(q):
                n, l = q.pop()
                levels.append([n.val, l])
                if n.left:
                        q.append([n.left, l + 1])
                if n.right:
                        q.append([n.right, l + 1])
        
        g = group(levels)
        for x in g:
                print(x)
        #group = [[ ] ]
        #lsort = sorted(levels, key=lambda x: x[1])
        #final = groupby(lsort, key=lambda x: x[1])
        #print(list(final))`o

def insertBT(root, val):
        if root == None:
                return BNode(val)
        if val <= root.val:
                root.left = insertBT(root.left, val)
        else:
                root.right = insertBT(root.right, val)
        return root

def group(l):
        d = {}
        result = []
        for e in l:
                if e[1] in d:
                        d[e[1]].append(e[0])
                else:
                        d[e[1]] = [e[0]]
        l2 = list(d.items())
        l2.sort(key= lambda x: x[0])
        return l2

