class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def printTree(root):
  queue = [root]
  tree = []
  while(queue):
    node = queue.pop(0)
    tree.append(node.data)
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  print(tree)

def insertBalanced(root, data):
  if root == None:
    return Node(data)
  if data <= root.data:
    root.left = insertBalanced(root.left, data)
  if data > root.data:
    root.right = insertBalanced(root.right, data)
  return root


#assumes they are in the tree
def LCABalanced(root, a, b):
  if root.data == a:
    return a
  if root.data == b:
    return b
  if a < root.data and b < root.data:
    return LCABalanced(root.left, a, b)
  if a > root.data and b > root.data:
    return LCABalanced(root.right, a, b)
  return root.data

root = Node(10)
insertBalanced(root, 3)
insertBalanced(root, 20)
insertBalanced(root, 2)
insertBalanced(root, 4)
insertBalanced(root, 16)
printTree(root)
print(LCABalanced(root, 2, 4))

def LCA(root, a, b):
  pass

def heightDF(root, a):
  pass
