from collections import deque

class DirectedEulerianPath:
    def __init__(self, G):
        self.path = deque()

        s = self._non_isolated_vertex(G)
        deficit = 0
        for v in range(G.V):
            if G.outdegree(v) > G.indegree(v):
                deficit += (G.outdegree(v) - G.indegree(v))
                s = v

        if deficit > 1: return

        if s == -1: s = 0

        self.visited = set()
        self._dfs(G, s)

    def _dfs(self, G, v):
        for w in G.adj[v]:
            e = f"{v}-{w}"
            if e not in self.visited:
                self.visited.add(e)
                self._dfs(G, w)
        self.path.appendleft(v)

    def _non_isolated_vertex(self, G):
        for v in range(G.V):
            if G.outdegree(v) > 0:
                return v
        return -1

    def haspath(self):
        return len(self.path) > 0

    def getpath(self):
        return self.path


if __name__ == '__main__':
    import sys
    from digraph import Digraph
    G = Digraph.create(sys.stdin)
    e = DirectedEulerianPath(G)
    if e.haspath():
        print(f"Graph has directed eulerian path:")
        print('-'.join(str(v) for v in e.getpath()))
    else:
        print(f"Graph has no directed eulerian path")
