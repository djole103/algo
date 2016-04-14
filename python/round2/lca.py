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

def LCAmemory(root, a, b):
  if root.data == a:
    return a
  if root.data == b:
    return b
  parentsA = findParents(root, a)
  if b in parentsA:
    return b
  parentsB = findParents(root, b)
  if a in parentsB:
    return a
  if parentsA == parentsB:
    return parentsA[-1]
  for i in range(min(len(parentsA),len(parentsB))):
    if parentsA[i] != parentsB[i]:
      return parentsA[i-1]

def findParents(root, a, parents=[]):
  if root.data == a:
    return parents
  if root.left == None and root.right == None:
    return None
  if root.left:
    #print(root.left.data)
    tryParents = findParents(root.left, a, parents+[root.data])
    if tryParents:
      return tryParents
  if root.right:
    tryParents = findParents(root.right, a, parents+[root.data])
    if tryParents:
      return tryParents

print(LCAmemory(root, 2, 4))

def depthTraversal(root, order=[]):
  order.append(root.data)
  if root.left:
    depthTraversal(root.left, order)
  if root.right:
    depthTraversal(root.right, order)
  return order

def breadthFirstTraversal(root):
  queue = [root]
  order = []
  while(queue):
    node = queue.pop(0)
    order.append(node.data)
    if node.left:
      queue.append(node.left)
    if node.right:
      queue.append(node.right)
  return order


def heightDF(root, a):
  pass
