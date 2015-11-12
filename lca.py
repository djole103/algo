#binary 
def lca(node,a,b):
	if node == a or node == b: return node
	if a < node and b < node: return lca(node.left,a,b)
	if a > node and b > node: return lca(node.right,a,b)
	return node


#non binary
def lcaDepth(a,b):
	while(a.depth() > b.depth()):
		a = a.parent()
	while(a.depth() < b.depth()):
		b = b.parent()
	while a != b:
		a = a.parent()
		b = b.parent()


#non binary tree
#def lcaNB(a,b,list)
