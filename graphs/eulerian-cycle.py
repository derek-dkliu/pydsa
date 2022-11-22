from collections import deque

class EulerianCycle:
    def __init__(self, G):
        self.cycle = deque()

        # must have at least one edge
        if G.E == 0: return

        # necessary condition: all vertices have even degree
        for v in range(G.V):
            if G.degree(v) % 2 != 0: return

        s = self._non_isolated_vertex(G)
        self.visited = set()
        self._dfs(G, s)

    def _dfs(self, G, v):
        for w in G.adj[v]:
            e1 = f"{v}-{w}"
            e2 = f"{w}-{v}"
            if (e1 not in self.visited) and (e2 not in self.visited):
                self.visited.add(e1)
                self._dfs(G, w)
        self.cycle.appendleft(v)

    def _non_isolated_vertex(self, G):
        for v in range(G.V):
            if G.degree(v) > 0:
                return v
        return -1

    def hascycle(self):
        return len(self.cycle) > 0

    def getcycle(self):
        return self.cycle


if __name__ == '__main__':
    import sys
    from graph import Graph
    G = Graph.create(sys.stdin)
    e = EulerianCycle(G)
    if e.hascycle():
        print(f"Graph has eulerian cycle:")
        print('-'.join(str(v) for v in e.getcycle()))
    else:
        print(f"Graph has no eulerian cycle")