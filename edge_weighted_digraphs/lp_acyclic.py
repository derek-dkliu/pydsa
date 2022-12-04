from collections import deque
from topological_sort import TopologicalSort

class AcyclicLP:
    """time: O(V + E)"""

    def __init__(self, G, s):
        self.edge_to = [None] * G.V
        self.dist_to = [-float('inf')] * G.V
        self.dist_to[s] = 0

        ts = TopologicalSort(G)
        if ts.has_cycle(): raise Exception("Graph is not a DAG")

        for v in ts.get_order():
            self._relax(G, v)

    def _relax(self, G, v):
        for e in G.adj[v]:
            w = e.to_vertex()
            if self.dist_to[w] < self.dist_to[v] + e.weight:
                self.dist_to[w] = self.dist_to[v] + e.weight
                self.edge_to[w] = e

    def has_path_to(self, v):
        return self.dist_to[v] > -float('inf')

    def path_to(self, v):
        path = deque()
        e = self.edge_to[v]
        while e is not None:
            path.appendleft(e)
            e = self.edge_to[e.from_vertex()]
        return path

    def cost_to(self, v):
        return self.dist_to[v]

if __name__ == '__main__':
    import sys
    from edge_weighted_digraph import EdgeWeightedDigraph
    G = EdgeWeightedDigraph.create(sys.stdin)
    s = int(sys.argv[1])
    lp = AcyclicLP(G, s)
    print(f"Longest path from {s} to every other vertex:")
    for v in range(G.V):
        if lp.has_path_to(v):
            print(f"{v} ({lp.cost_to(v):.2f}): {'  '.join(str(e) for e in lp.path_to(v))}")
        else:
            print(f"no path to {v}")