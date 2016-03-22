class Node:
    def __init__(self,value):
        self.value = value
        self.nxt = None

class Linkedlist:
    def __init__(self,rootNode = None):
        self.root = rootNode

    def insert(self,value):
        tmp = self.root
        while (tmp.nxt!=None):
            tmp = tmp.nxt
        tmp.nxt = Node(value)

ll = Linkedlist(5)
ll.insert(4)
ll.insert(3)
ll.insert(2)
ll.insert(1)


