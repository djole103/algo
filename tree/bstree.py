class BST:
	def __init__(self,root):
		self.root = root
		self.history = [root.value()]

	def __str__(self,root):
		pass
		
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
	
