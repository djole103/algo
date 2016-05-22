class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class Med:
	def __init__(self):
		self.head = None
		self.median = None
		self.length = None
	
	def insert(self, val):
		if self.head == None:
			self.head = Node(val)
			self.median = val
			self.length = 1
			return
		node = self.head
		inserted = False
		medianUpdated = False
		pos = 0
		newLength = self.length +1
		newMPos = newLength //2
		while(not medianUpdated or not inserted):
			pos += 1
			if(not inserted and (node.next == None or node.next.val >= val)):
				print("INSERTING", node.val, node.next)
				tmp = node.next
				node.next = Node(val)
				node.next.next = tmp
				self.length += 1
				inserted = True
				print("NEXT NODE: ", node.next)
			if(not medianUpdated and pos == newMPos):
				print("UPDATING. POS: %i MPOS: %i NODE: %i" % (pos, newMPos, node.val))
				if newLength % 2 == 0:
					self.median = float((node.val + node.next.val)) / 2
				else:
					self.median = node.val
				medianUpdated = True
			#if(medianUpdated and inserted):
			#	break
			node = node.next

	def printMed(self):
		node = self.head
		while(node != None):
			print(node.val)
			node = node.next
		

def tmed(med, exp):
	try:
		assert med.median == exp
	except:
		print("Expected: %f Got: %f" % (exp, med.median))
	

test = Med()
test.insert(1)
tmed(test, 1)
test.insert(3)
tmed(test, 2)
test.insert(2)
tmed(test, 2)

test.insert(30)
test.insert(50)
test.insert(35)
test.printMed()
tmed(test, 16.5)
