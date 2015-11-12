class Node:
	def __init__(self,children,value):
		self.children = children
		self.value = value

def lcaARB(node,a,b):
	parent = {}
	nextVisit = [node]
	#nodeA = None
	#nodeB = None
	while(nextVisit):
		node = nextVisit.pop()
		#if node.value == a: nodeA = node
		#if node.value == b: nodeB = node
		for child in node.children:
			parent[child] = node
			nextVisit.append(child)
	#ancestorA = parent[nodeA] ect if a,b args are values not nodes
	ancestorA = a
	ancestorB = b
	ancestorsA = {}
	while(ancestorA in parent):
		ancestorsA[ancestorA] = True
		ancestorA = parent[ancestorA]
	while(ancestorB in parent):
		if ancestorB in ancestorsA:
			return ancestorB 
		ancestorB = parent[ancestorB]
	return None

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
