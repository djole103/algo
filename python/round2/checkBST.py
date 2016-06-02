from createMinTree import *
from treeutils import *

#this is wrong just checks left/right but not if it's insertion order right
def isBST(node):
        if node == None:
                return True
        if node.left:
                if node.left.val > node.val:
                        return False
        if node.right:
                if node.right.val < node.val:
                        return False
        return isBST(node.left) and isBST(node.right)

#TEST = [i for i in range(1,14)]
#tree = minTree(TEST,0,len(TEST)-1)

#print(isBST(tree))

#tree2 = BNode(2)
#tree2.left = BNode(6)

#print(isBST(tree2))

def inOrder(node, a = []):
        if node == None:
                return
        inOrder(node.left, a)
        a.append(node.val)
        inOrder(node.right, a)
        return a

def checkBST(node):
        l = inOrder(node)
        for i in range (1, len(node)):
                if l[i] < l[i-1]:
                        return False
        return True

def isBST2(node, m = None, mx = None):
        if node == None:
                return True
        if ((mx != None) and (node.val > mx)):
                        return False
        if ((m != None) and (node.val <=  m)):
                        return False
        return isBST2(node.left, m, node.val) and isBST2(node.right, node.val, mx)
 
tree3 = BNode(20)
tree3.right = BNode(30)
tree3.left = BNode(10)
tree3.left.right = BNode(25)
print(isBST2(tree3,tree3.val,tree3.val))
