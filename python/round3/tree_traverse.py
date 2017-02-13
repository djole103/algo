# traverse to ith index of inorder ordering btree

from tree_utils import *

def ith(node, idx):
    if not node:
        return None, idx
    if idx == 0:
        return node.val, idx
    ret = None
    ret, idx = ith(node.left, idx)
    if ret:
        return ret, idx
    if idx - 1 == 0:
        return node.val, 0
    return ith(node.right, idx - 1)

def ith2(node, idx):
    stack = []
    while(stack or node):
        while(node):
            stack.append(node)
            node = node.left
        node = stack.pop()
        idx -= 1
        if idx == 0:
            return node.val
        node = node.right
    #tree doesn't have that many elements
    return -1

def in_order(node, order = []):
    if node == None:
        return order
    in_order(node.left, order)
    order.append(node.val)
    in_order(node.right, order)
    return order

def in_order2(node):
    stack = []
    order = []
    while(stack or node):
        while(node):
            stack.append(node)
            node = node.left
        node = stack.pop()
        order.append(node.val)
        node = node.right
    return order

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

print(in_order2(root))
print(ith2(root, 6))
