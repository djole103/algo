class BST:
	def __init__(self,root=None):
		if root: 
			self.root = Node(root)
			self.history = [root]
		else:
			self.root = root
			self.history = []

	def __str__(self):
		lvls = self.levels()
		print(lvls)
		if len(lvls)==0: return "It's empty dude!!!"
		maxHeight = lvls[-1][0]+1
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
			if new <= self.root.value() : self.__insert(self.root.left,new)
			else                        : self.__insert(self.root.right,new)
		else: 
			self.root = Node(new)
			#todo: consider pops
			self.history.append(new)

	def __insert(self,curr,new):
		if curr is None:
			curr = Node(new)
			self.history.append(new)
		elif new <= curr.value() : self.__insert(curr.left,new)
		else                     : self.__insert(curr.right,new)

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
				if node[1].left: queue.append((node[0]+1,node[1].left))
				if node[1].right: queue.append((node[0]+1,node[1].right))
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
		self.val = val
		self.left  = left
		self.right = right

	def leaf(self):
		if self.right == None and self.left == None: return True
		else: return False

	def value(self):
		return self.val
print("made it")
bst = BST()
bst.insert(5)
bst.insert(3)
#print(bst.root.left.value())
bst.insert(6)
print(bst)
