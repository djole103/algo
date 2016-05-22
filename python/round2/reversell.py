class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

def insert(val, node = None):
	if node == None:
		return Node(val)
	head = node
	while(node.next != None):
		node = node.next
	node.next = Node(val)
	return head

def printLL(node):
	while(node != None):
		print("Node val: %i" % node.val)
		node = node.next

def reverse(head):
	prev = None
	cur = head
	nxt = cur.next

	while (nxt != None):
		cur.next = prev
		prev = cur
		cur = nxt
		nxt = nxt.next
	cur.next = prev
	return cur



ll = insert(1)
insert(2, ll)
insert(3, ll)
insert(4, ll)
printLL(ll)
ll = reverse(ll)
printLL(ll)


	
