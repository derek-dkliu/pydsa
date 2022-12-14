import sys, os
sys.path.insert(0, os.getcwd())
from heaps.min_pq_index import IndexMinPQ 
from collections import deque

class DijkstraSP:
    """time: O(E*log(V))"""

    def __init__(self, G, s):
        # ensure no negative weighted edges
        for e in G.edges():
            if e.weight < 0: raise Exception(f"Edge {e} has negative weight")

        self.edge_to = [None] * G.V
        self.dist_to = [float('inf')] * G.V
        self.dist_to[s] = 0
        self.pq = IndexMinPQ(G.V)
        self.pq.push(s, self.dist_to[s])
        while self.pq:
            v = self.pq.pop()
            self._relax(G, v)

    def _relax(self, G, v):
        for e in G.adj[v]:
            w = e.to_vertex()
            if self.dist_to[w] > self.dist_to[v] + e.weight:
                self.dist_to[w] = self.dist_to[v] + e.weight
                self.edge_to[w] = e
                if self.pq.contains(w): self.pq.decrease_key(w, self.dist_to[w])
                else: self.pq.push(w, self.dist_to[w])

    def has_path_to(self, v):
        return self.dist_to[v] < float('inf')

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
    sp = DijkstraSP(G, s)
    print(f"Shortest path from {s} to every other vertex:")
    for v in range(G.V):
        if sp.has_path_to(v):
            print(f"{v} ({sp.cost_to(v):.2f}): {'  '.join(str(e) for e in sp.path_to(v))}")
        else:
            print(f"no path to {v}")