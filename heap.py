import math

class Heap:
	def __init__(self,root):
		self.heap = [root]

	def insert(self,val):
		self.heap.append(val)
		parentIdx = math.floor(len(self.heap)/2) -1
		newIdx = -1
		while(val < self.heap[parentIdx]):
			self.heap[parentIdx],self.heap[newIdx] = self.heap[newIdx],self.heap[parentIdx]
			newIdx    = parentIdx
			parentIdx = math.floor(parentIdx/2)


hehe = Heap(6)
hehe.insert(29)
hehe.insert(19)
hehe.insert(40)
hehe.insert(44)
hehe.insert(30)
hehe.insert(22)
print(hehe.heap)

hehe.insert(12)
print(hehe.heap)
