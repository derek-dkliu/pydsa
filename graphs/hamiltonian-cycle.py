class HamiltonianCycle:
    def __init__(self, G):
        self.cycle = []
        self.marked = [False] * G.V
        if G.V == 1:
            self.cycle.append(0)
            return
        self.s = 0
        self._dfs(G, self.s)
            
    def _dfs(self, G, v):
        self.marked[v] = True
        self.cycle.append(v)
        if len(self.cycle) == G.V and self.s in G.adj[v]:
            self.cycle.append(self.s)
            return True

        for w in G.adj[v]:
            if not self.marked[w]:
                if self._dfs(G, w): return True

        self.marked[v] = False
        self.cycle.pop()

    def hascycle(self):
        return len(self.cycle) > 0

    def getcycle(self):
        return self.cycle

if __name__ == '__main__':
    import sys
    from graph import Graph
    G = Graph.create(sys.stdin)
    h = HamiltonianCycle(G)
    if h.hascycle():
        print(f"Graph has hamiltonian cycle:")
        print('-'.join(str(v) for v in h.getcycle()))
    else:
        print(f"Graph has no hamiltonian cycle")