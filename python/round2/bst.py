class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root == None:
        root = Node(data)
        return root
    if data <= root.data:
        root.left = insert(root.left, data)
        return root
    else:
        root.right = insert(root.right, data)
        return root
    
def in_order_traversal(root, results):
    if root == None:
        return
    stack = [root]
    while stack:
        node = stack.pop(0)
        results.append(node.data)
        if node.left!= None:
            stack.append(node.left)
        if node.right!= None:
            stack.append(node.right)
    
def PrintNode(node):
    print(node.data)
    print(node.left.data)
    print(node.right.data)

def calcDepth(node):
    if node == None:
        return 0
    return 1 + max(calcDepth(node.left), calcDepth(node.right))

def 

results = []
root = Node(5)
insert(root, 2)
insert(root, 8)
insert(root, 1)
insert(root, 3)
in_order_traversal(root, results)
print(results)
print(calcDepth(root))
print(calcDepth(root.left))
print(calcDepth(root.right))
