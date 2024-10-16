graph = {
   "": [],
}

pc = {
    # ('Arad', 'Zerind'): 75,
}

locs = {
    # 'Arad': 366,
}

def DFS(g, v, goal, explored, path_so_far, m):
    explored.add(v)
    node = []
    if v == goal:
        return path_so_far + " -> " + v
    for w in g[v]:
        if w not in explored:
            f = locs.get(w) + pc.get((v, w))
            if m > f:
                m = f
                print("%i - %s - %s " % (m, v, w))
                node = w
                p = DFS(g, node, goal, explored, path_so_far + " -> " + v, m)
                if p:
                    return p
    return ""

print(DFS(graph, '', '', set(), "", 1000))
