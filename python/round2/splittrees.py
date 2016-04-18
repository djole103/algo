
from collections import defaultdict
from copy import deepcopy

N, M = raw_input()
nodes = []
adj_list = defaultdict(list)
for i in range(M):
    x,y = map(raw_input().split(),int)
    if x not in nodes:
        nodes.append(x)
    if y not in nodes:
        nodes.append(y)
    adj_list[x].append(y)
    adj_list[y].append(x)
   
def delete_edge(edge, graph):
    graph[edge[0]].remove(edge[1])
    graph[edge[1]].remove(edge[0])
    return graph

def find_disjoint(graph, nodes):
    trees = []
    for i in range len(nodes):
        if i in in_a_tree:
            continue
        i_nodes = edge_traversal(nodes[i], graph)
        
        for j in range(i+1,len(nodes)):
             if j not in i_nodes:
        
def edge_traversal(start, graph):
    visited = {}
    ns_nodes = []
    queue = [start]
    while queue:
        current = queue.pop(0)
        visited[current] = True
        for n in graph[current]:
            if n in visited: continue
            queue.append(n)
    return visited

for k,v in adj_list.iteritems():
    if len(v)%2 != 0:
