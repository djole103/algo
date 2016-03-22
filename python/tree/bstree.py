class BST:
	def __init__(self,root=None):
		if root: self.root = Node(root)
		else   : self.root = root

	def __str__(self):
		lvls = self.levels()
		print(lvls)
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
				node = queue.pop(0)
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
				tup = queue.pop(0)
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

	def common_ancestor(self,a,b):
		if self.root: return self.root.common_ancestor(a,b)
		else        : return None

	def LCA(self,a,b):
		if self.root: return self.root.LCA(a,b)
		else        : return None

	def checkBalancedTop(self):
		return self.root.checkBalancedTop()

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

	def common_ancestor(self,a,b):
		if self.value() == a or self.value() == b: return self
		if self.left:
			left = self.left.common_ancestor(a,b)
		else: left = None
		if self.right:
			right = self.right.common_ancestor(a,b)
		else: right = None
		if(left and right): return self
		elif left: return left
		else: return right

	def LCA(self,a,b):
		if self.value() == a or self.vlaue() == b:
			return self
		if a < self.value() and b < self.value():
			self.left.LCA(a,b)
		if a > self.value() and b > self.value():
			self.right.LCA(a,b)
		return self 
	
	def checkBalancedTop(self):
		if self.leaf(): return True
		height_left = self.left.height()
		height_right = self.right.height()
		if abs(heigh_left - height_right) > 1:
			return False
		return self.left.checkBalanced and self.right.checkBalanced
		
		if self.left and self.right: return  (self.left.checkBalancedTop() and self.right.checkBalancedTop())
		if self.left:
			return not (self.left.left or self.left.right)
		else:
			return not (self.right.left or self.right.right)


bst = BST()
#bst.insert(5)
#bst.insert(3)
#bst.insert(10)
#bst.insert(4)
#bst.insert(6)
#bst.insert(1)
#bst.insert(14)
#bst.insert(100)
bst.insert(5)
bst.insert(4)
bst.insert(3)
bst.insert(6)
bst.insert(1)
#		5
#	  /  \
#     4	 6
#	/	  \
#	3	  3
#   /
#   1
#bst.insert(101)
print(bst.checkBalancedTop())
#print(bst)
#com = bst.common_ancestor(14,6)
#print(com.value())
