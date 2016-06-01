def path(g, a, b):
        qa = [a]
        qb = [b]
        va = {}
        vb = {}
        while (qa or qb):
                if qa:
                        na = qa.pop()
                        for n in g[na.id]:
                                if n not in va:
                                        qa.append(n)
                        if na in vb or na in qb:
                                return True
                        va[na] = True

                if qb:
                        nb = qb.pop()
                        for n in g[na.id]:
                                if n not in vb:
                                        qb.append(n)

                        if nb in qa:
                                return True
                        vb[nb] = True
        return False
                        
