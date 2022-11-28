from collections import deque

class EulerianPath:
    def __init__(self, G):
        self.path = deque()

        s = self._non_isolated_vertex(G)
        odd_degree_vertices = 0
        for v in range(G.V):
            if G.degree(v) % 2 != 0:
                odd_degree_vertices += 1
                # start from any vertex with odd degree
                s = v
        
        # necessary condition: exactly only two vertices with odd degree
        if odd_degree_vertices > 2: return

        # special case for graph with zero edges (has a degenerate Eulerian path)
        if s == -1: s = 0

        self.visited = set()
        self._dfs(G, s)

    def _dfs(self, G, v):
        for w in G.adj[v]:
            e1 = f"{v}-{w}"
            e2 = f"{w}-{v}"
            if e1 not in self.visited and e2 not in self.visited:
                self.visited.add(e1)
                self._dfs(G, w)
        self.path.appendleft(v)

    def _non_isolated_vertex(self, G):
        for v in range(G.V):
            if G.degree(v) > 0:
                return v
        return -1

    def haspath(self):
        return len(self.path) > 0

    def getpath(self):
        return self.path


if __name__ == '__main__':
    import sys
    from graph import Graph
    G = Graph.create(sys.stdin)
    e = EulerianPath(G)
    if e.haspath():
        print(f"Graph has eulerian path:")
        print('-'.join(str(v) for v in e.getpath()))
    else:
        print(f"Graph has no eulerian path")

    