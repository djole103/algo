class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def conv_to_num(l):
    s = ""
    while(l.next != None):
        s += string(l.val)
    return float(s[-1::])

def addTwo(l1, l2):
    return conv_to_num(l1) + conv_to_num(l2)
