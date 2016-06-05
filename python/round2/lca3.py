def lca(g, a, b):
        ancestor = None
        count = 0
        def lcaHelper(node):
                nonlocal ancestor, count
                if node is None or ancestor is not None:
                        return
                count_entering = count
                if node.val in (a,b):
                        count += 1
                lcaHelper(node.left)
                lcaHelper(node.right)
                if count_entering == 0 and count == 2 and ancestor is None:
                        ancestor = node
        lcaHelper(g)
        return ancestor

                        
