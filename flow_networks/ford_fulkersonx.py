import sys, os
sys.path.insert(0, os.getcwd())
from heaps.min_pq_index import IndexMinPQ 

class FordFulkersonX:
    def __init__(self, G, s, t):
        self.value = 0
        while self._has_augmenting_path(G, s, t):
            bottle = float('inf')
            x = t
            while x != s:
                e = self.edge_to[x]
                bottle = min(bottle, e.residual_capacity_to(x))
                x = e.other(x)
            x = t
            while x != s:
                e = self.edge_to[x]
                e.add_residual_flow_to(x, bottle)
                x = e.other(x)
            self.value += bottle        

    def _has_augmenting_path(self, G, s, t):
        self.edge_to = [None] * G.V
        self.dist_to = [0] * G.V
        self.dist_to[s] = float('inf')
        self.pq = IndexMinPQ(G.V)
        self.pq.push(s, self.dist_to[s])
        while self.pq:
            v = self.pq.pop()
            self._relax(G, v)
        return self.dist_to[t] > 0

    def _relax(self, G, v):
        for e in G.adj[v]:
            w = e.other(v)
            capacity = e.residual_capacity_to(w)
            if capacity > 0 and self.dist_to[w] < min(self.dist_to[v], capacity):
                self.dist_to[w] = min(self.dist_to[v], capacity)
                self.edge_to[w] = e
                if self.pq.contains(w): self.pq.decrease_key(w, -self.dist_to[w])
                else: self.pq.push(w, -self.dist_to[w])

    def is_in_cut(self, v):
        return self.dist_to[v] > 0


if __name__ == '__main__':
    import sys
    from flow_network import FlowNetwork
    G = FlowNetwork.create(sys.stdin)
    s = 0
    t = G.V - 1
    ff = FordFulkersonX(G, s, t)

    print(f"Maxflow from {s} to {t}:")
    for v in range(G.V):
        for e in G.adj[v]:
            if e.from_vertex() == v and e.flow > 0:
                print(e)
    print("Mincut:")
    for v in range(G.V):
        if ff.is_in_cut(v):
            print(v, end=" ")
    print()
    print(f"Maxflow value is {ff.value}")