class BST:
	def __init__(self,root):
		self.root = root
		self.history = [root.value()]

	def __str__(self,root):
		lvls = self.levels()
		if len(lvls)==0: return "It's empty dude!!!"
		maxHeight = lvls[-1][0]
		tree = [[] for i in range(maxHeight)]
		for elem in lvls:
			tree[elem[0]].append(elem[1])
		stringResult = "".join(str(height)+'\n' for height in tree)
		return stringResult	
		
	def history(self,node):
		return self.history

	def root(self):
		return root

	def insert(self,new):
		if self.root:
			if new.value() <= self.root.value() : __insert(self,root.left,new)
			else                                : __insert(self,root.right,new)
		else: 
			self.root = new
			#todo: consider pops
			self.history.append(new.value())

	def __insert(self,curr,new):
		if curr is None:
			curr = new
			self.history.append(new.value())
		elif new.value() <= curr.value() : __insert(self,curr.left,new)
		else                             : __insert(self,curr.right,new)

	def levels(self):
		height = 0
		lvls = []
		if self.root:
			lvls.append((height,root.value())
			lvls 
			
	def __levels(self,lvls,height):
		lvls.append(

	def breadthfirst(self)
		queue = []
		bfs = []
		if self.root: 
			queue.append(self.root)
			while(queue):
				node = queue.pop()
				bfs.append(node)
				if node.left: queue.append(node.left)
				if node.right: queue.append(node.right)
		return bfs

	def levels(self)
		height = 0
		queue = []
		lvls = []
		if self.root: 
			queue.append((height,self.root))
			while(queue):
				node = queue.pop()
				lvls.append((node[0],node[1].value()))
				if node[1].left: queue.append((node[0]+1,node[1].left))
				if node[1].right: queue.append((node[0]+1,node[1].right))
		return lvls

	def depth(self):
		d = []
		if self.root: 
			d.append(root)
			d = __depth(d,root.left)
			return __depth(d,root.right)
		else: return d

	def __depth(self,d,curr):
		if curr:
			d.append(curr)
			d = __depth(d,curr.left)
			return __depth(d,curr.right)
		else: return d

class Node:
	def __init__(self,value,left=None,right=None):
		self.value = value
		self.left  = left
		self.right = right

	def leaf(self):
		if self.right == None and self.left == None: return True
		else: return False
	
