import sys, os
sys.path.insert(0, os.getcwd())
from heaps.min_pq_index import IndexMinPQ

class EagerPrimMST:
    """time: O(E*log(V))"""

    def __init__(self, G):
        self.mst = []
        self.marked = [False] * G.V
        self.pq = IndexMinPQ(G.V)
        for v in range(G.V):
            if not self.marked[v]:
                self._prim(G, v)

    def _prim(self, G, s):
        self._visit(G, s)
        while self.pq:
            self.mst.append(self.pq.min_key())
            self._visit(G, self.pq.pop())

    def _visit(self, G, v):
        self.marked[v] = True
        for e in G.adj[v]:
            w = e.other(v)
            if not self.marked[w]:
                if not self.pq.contains(w):
                    self.pq.push(w, e)
                elif e < self.pq.get_key(w):
                    self.pq.decrease_key(w, e)

    def edges(self):
        return self.mst


if __name__ == '__main__':
    from sys import stdin
    from edge_weighted_graph import EdgeWeightedGraph
    G = EdgeWeightedGraph.create(stdin)
    p = EagerPrimMST(G)
    print("Graph has MST:")
    print('\n'.join(str(e) for e in p.edges()))