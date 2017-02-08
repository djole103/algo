class N:
    def __init__(self, val):
        self.v = val
        self.n = None


def contains_cycle(node):
    visited = {}
    while(node):
        if node in visited:
            return True
        visited[node] = True
        node = node.n
    return False

n1 = N(1)
n2 = N(2)
n3 = N(3)
n4 = N(4)

n1.n = n2
n2.n = n3
n3.n = n4
n4.n = n1

print(contains_cycle(n1))
