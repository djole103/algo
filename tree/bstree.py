class BST:
	def __init__(self,root=None):
		if root: self.root = Node(root)
		else   : self.root = root

	def __str__(self):
		lvls = self.levels()
		if len(lvls)==0: return "It's empty dude!!!"
		maxHeight = lvls[-1][0]+1
		tree = [[] for i in range(maxHeight)]
		for elem in lvls:
			tree[elem[0]].append(elem[1])
		stringResult = "".join('\n'+str(height) for height in tree)
		return stringResult	
		
	def history(self,node):
		return self.history

	def root(self):
		return root

	def insert(self,new):
		if self.root: self.root.insert(new)
		else        : self.root = Node(new)


	def breadthfirst(self):
		queue = []
		bfs = []
		if self.root: 
			queue.append(self.root)
			while(len(queue)!=0):
				node = queue.pop()
				bfs.append(node)
				if node.left: queue.append(node.left)
				if node.right: queue.append(node.right)
		return bfs

	def levels(self):
		height = 0
		queue = []
		lvls = []
		if self.root: 
			queue.append((height,self.root))
			while(queue):
				#(height,node)
				tup = queue.pop()
				lvls.append((tup[0],tup[1].value()))
				if tup[1].left: queue.append((tup[0]+1,tup[1].left))
				if tup[1].right: queue.append((tup[0]+1,tup[1].right))
		return lvls

	def depth(self):
		d = []
		if self.root: 
			d.append(self.root)
			d = self.__depth(d,self.root.left)
			return self.__depth(d,self.root.right)
		else: return d

	def __depth(self,d,curr):
		if curr:
			d.append(curr)
			d = self.__depth(d,curr.left)
			return self.__depth(d,curr.right)
		else: return d

class Node:
	def __init__(self,val,left=None,right=None):
		self.val   = val
		self.left  = left
		self.right = right

	def leaf(self):
		if self.right == None and self.left == None: return True
		else: return False

	def value(self):
		return self.val

	def insert(self,new):
		if new <= self.val:
			if self.left: self.left.insert(new)
			else        : self.left = Node(new)
		else:
			if self.right: self.right.insert(new)
			else         : self.right = Node(new)

bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(6)
bst.insert(4)
bst.insert(10)
bst.insert(1)
bst.insert(6)
print(bst)
