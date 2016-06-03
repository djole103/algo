def cycle(g):
        path = set()
        def cycleHelp(node):
                path.add(node)
                for n in g.get(node, ()):
                        if n in path or cycleHelp(n):
                                return True
                path.remove(node)
                return False
        return any(cycleHelp(v) for v in g)

TEST = {1 : [2],
        2 : [1,3,4],
        3 : [2],
        4 : [2,5],
        5 : [4]}

print(cycle(TEST))

