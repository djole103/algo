#given list of edges find reciprocals

def reciprocals(edges):
    opposites = {}
    recips = []
    for (n1, n2) in edges:
        if (n2, n1) in opposites:
            recips.append((n2,n1))
        else:
            opposites[(n2,n1)] = True
    return recips
        

