from treeutils import printTreeL

class Node:
        def __init__(self, val):
                self.val = val
                self.left = None
                self.right = None

def printTree(root):
        q = [root]
        l = []
        while(q):
                n = q.pop()
                if n.left:
                        q.append(n.left)
                if n.right:
                        q.append(n.right)
                l.append(n.val)
        print(l)

def printR(node, level = 0):
        print("val: %i, height: %i" % (node.val, level))
        if node.left:
                printR(node.left, level+1)
        if node.right:
                printR(node.right, level+1)



def minTree(nums, start, end):
        if start > end:
                return None
        mid = (end + start) / 2
        node = Node(nums[mid])
        #print(node.val)
        node.left = minTree(nums, start, mid - 1)
        node.right = minTree(nums, mid + 1, end)
        return node

TEST = [1,2,3,4,5,6,7,8,9,10,11,12,13]
tree = minTree(TEST, 0, len(TEST) -1)
#printR(tree)
printTreeL(tree)
