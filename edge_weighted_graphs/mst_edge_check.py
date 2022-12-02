def is_edge_in_mst(G, e):
    s = e.either()
    t = e.other(s)
    marked = [False] * G.V
    return dfs(G, s, t, e.weight, marked)

def dfs(G, v, t, weight, marked):
    if v == t: return False
    marked[v] = True
    for e in G.adj[v]:
        w = e.other(v)
        if not marked[w] and e.weight < weight:
            if not dfs(G, w, t, weight, marked):
                return False
    return True


if __name__ == '__main__':
    from sys import stdin
    from edge_weighted_graph import EdgeWeightedGraph
    G = EdgeWeightedGraph.create(stdin)
    for e in G.edges():
        print(f"Edge {e} in MST? {is_edge_in_mst(G, e)}")