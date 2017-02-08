class Node:
    def __init__(self, val):
        self.val = val
        left = None
        right = None

def in_order(node):
    stack = []
    ord = []
    while(node or stack):
        while(node):
            stack.append(node)
            node = node.left
        node = stack.pop()
        ord.append(node.val)
        node = node.right
    return ord
