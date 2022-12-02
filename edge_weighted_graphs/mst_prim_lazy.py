import sys, os
sys.path.insert(0, os.getcwd())
from fundamentals.min_pq import MinPQ

class LazyPrimMST:
    """time: O(E*log(E))"""
    
    def __init__(self, G):
        self.mst = []
        self.marked = [False] * G.V
        self.pq = MinPQ()
        for v in range(G.V):
            if not self.marked[v]:
                self._prim(G, v)

    def _prim(self, G, s):
        self._visit(G, s)
        while self.pq:
            e = self.pq.pop()
            v = e.either()
            w = e.other(v)
            if self.marked[v] and self.marked[w]: continue
            self.mst.append(e)
            if not self.marked[v]: self._visit(G, v)
            if not self.marked[w]: self._visit(G, w)

    def _visit(self, G, v):
        self.marked[v] = True
        for e in G.adj[v]:
            if not self.marked[e.other(v)]:
                self.pq.push(e)
        
    def edges(self):
        return self.mst


if __name__ == '__main__':
    from sys import stdin
    from edge_weighted_graph import EdgeWeightedGraph
    G = EdgeWeightedGraph.create(stdin)
    p = LazyPrimMST(G)
    print("Graph has MST:")
    print('\n'.join(str(e) for e in p.edges()))