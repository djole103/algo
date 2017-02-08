from tree_utils import *

def max_depth(node):
    stack = [node]
    depth = 0
    while(stack):
        num_elems = len(stack)
        for i in range(num_elems):
            n = stack.pop(0)
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
        depth += 1
    return depth

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.right = Node(2)

print(max_depth(root))
