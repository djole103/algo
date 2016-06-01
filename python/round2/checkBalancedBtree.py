from createMinTree import *

def balanced(node):
        if node == None:
                return True
        if node.left == None:
                if node.right != None and (node.right.left != None or node.right.right != None):
                        return False
        if node.right == None:
                if node.left != None and (node.left.left != None or node.left.right != None):
                        return False
        
        return balanced(node.left) and balanced(node.right)

def balanced2(node):
        return balanced2Helper(node) != -2

def balanced2Helper(node):
        if node == None:
                return -1
        dl = balanced2Helper(node.left) 
        dr = balanced2Helper(node.right)
        if (dl == -2 or dr == -2):
                return -2
        diff = abs(dl - dr)
        if diff > 1:
                return -2
        return max(dl, dr) + 1

vals = [i for i in range(1,14)]
tree = minTree(vals, 0, len(vals) -1)

print(balanced2(tree))

tree.right = None
print(balanced2(tree))
