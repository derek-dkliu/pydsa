from collections import deque

class EdgeWeightedDirectedCycle:
    def __init__(self, G):
        self.marked = [False] * G.V
        self.onstack = [False] * G.V
        self.edge_to = [None] * G.V
        self.cycle = None
        for v in range(G.V):
            if not self.marked[v] and not self.cycle:
                self._dfs(G, v)

    def _dfs(self, G, v):
        self.marked[v] = True
        self.onstack[v] = True
        for e in G.adj[v]:
            w = e.to_vertex()
            if self.cycle: return
            elif not self.marked[w]:
                self.edge_to[w] = e
                self._dfs(G, w)
            elif self.onstack[w]:
                self.cycle = deque()
                f = e
                while f.from_vertex() != w:
                    self.cycle.appendleft(f)
                    f = self.edge_to[f.from_vertex()]
                self.cycle.appendleft(f)
                return
        self.onstack[v] = False

    def has_cycle(self):
        return self.cycle is not None

    def get_cycle(self):
        return self.cycle


if __name__ == '__main__':
    import sys
    from edge_weighted_digraph import EdgeWeightedDigraph
    G = EdgeWeightedDigraph.create(sys.stdin)
    c = EdgeWeightedDirectedCycle(G)
    if c.has_cycle():
        print("Graph has a directed cycle:")
        print("  ".join(str(e) for e in c.get_cycle()))
    else:
        print("Graph is a DAG")