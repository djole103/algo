from tree_utils import *
from collections import defaultdict

def get_levels(node):
    levels = defaultdict(list)
    levels[1] = [node.val]
    level(node.left, levels, 2)
    level(node.right, levels, 2)
    return levels.items()

def level(node, levels, lvl):
    if node:
        levels[lvl].append(node.val)
        level(node.left, levels, lvl +1)
        level(node.right, levels, lvl +1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(4)
print(get_levels(root))
