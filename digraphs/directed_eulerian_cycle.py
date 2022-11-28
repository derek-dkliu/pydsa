from collections import deque

class DirectedEulerianCycle:
    def __init__(self, G):
        self.cycle = deque()

        # must have at least one edge
        if G.E == 0: return

        # necessary condition: indegree(v) = outdegree(v) for each vertex v
        for v in range(G.V):
            if G.indegree(v) != G.outdegree(v): return
        
        s = self._non_isolated_vertex(G)
        self.visited = set()
        self._dfs(G, s)

    def _dfs(self, G, v):
        for w in G.adj[v]:
            e = f"{v}-{w}"
            if e not in self.visited:
                self.visited.add(e)
                self._dfs(G, w)
        self.cycle.appendleft(v)

    def _non_isolated_vertex(self, G):
        for v in range(G.V):
            if G.outdegree(v) > 0:
                return v
        return -1

    def hascycle(self):
        return len(self.cycle) > 0

    def getcycle(self):
        return self.cycle


if __name__ == '__main__':
    import sys
    from digraph import Digraph
    G = Digraph.create(sys.stdin)
    e = DirectedEulerianCycle(G)
    if e.hascycle():
        print(f"Graph has directed eulerian cycle:")
        print('-'.join(str(v) for v in e.getcycle()))
    else:
        print(f"Graph has no directed eulerian cycle")