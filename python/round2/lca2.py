from treeutils import *

def lcaBS(r, a , b):
        if r.val == a:
                return a
        if r.val == b:
                return b
        if a < r.val and b < r.val:
                return lca(r.left, a, b)
        if a > r.val and b > r.val:
                return lca(r.right, a, b)
        return r

def lca(r, a, b):
        d = {"ancestor" : None,
             "count"    : 0}
        def travel(node):
                if node is None or d["ancestor"] is not None:
                        return
                count_at_entry = d["count"]
                if node.val == a:
                        d["count"] += 1
                if node.val == b:
                        d["count"] += 1
                travel(node.left)
                travel(node.right)
                if count_at_entry == 0 and d["count"] == 2 and d["ancestor"] == None:
                        d["ancestor"] = node
        travel(r)
        return d["ancestor"].val

def getDepth(r, n):
        if r == None:
                return -1
        if r.val == n:
                return 1
        dl = getDepth(r.left, n)
        dr = getDepth(r.right, n)
        if dl != -1 or dr != -1:
                return max(dl,dr) + 1
        else:
                return - 1

tree = BNode(10)
tree = insertBT(tree, 5)
tree = insertBT(tree, 20)
tree = insertBT(tree, 14)
tree = insertBT(tree, 4)

printTreeL(tree)
print(tree.left.val)
print(lca(tree, 5, 4))
print(getDepth(tree, 5))
