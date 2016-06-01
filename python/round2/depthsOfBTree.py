from createMinTree import *
def depths(node, level = 0, ds = []):
        if level == len(ds):
                ds.append([node.val])
        else:
                ds[level].append(node.val)
        if node.left:
                depths(node.left, level+1, ds)
        if node.right:
                depths(node.right, level+1, ds)
        return ds

vals = [i for i in range(1,14)]
tree = minTree(vals, 0, len(vals)-1)
ds = depths(tree)
print(ds)

