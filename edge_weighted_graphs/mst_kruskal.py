import heapq
import sys, os
sys.path.insert(0, os.getcwd())
from fundamentals.union_find import UnionFind

class KruskalMST:
    """time: O(E*log(E))"""

    def __init__(self, G):
        self.mst = []
        pq = G.edges()
        heapq.heapify(pq)

        uf = UnionFind(G.V)
        while pq and len(self.mst) < G.V - 1:
            e = heapq.heappop(pq)
            v = e.either()
            w = e.other(v)
            if not uf.connected(v, w):
                uf.union(v, w)
                self.mst.append(e)

    def edges(self):
        return self.mst


if __name__ == '__main__':
    from sys import stdin
    from edge_weighted_graph import EdgeWeightedGraph
    G = EdgeWeightedGraph.create(stdin)
    k = KruskalMST(G)
    print("Graph has MST:")
    print('\n'.join(str(e) for e in k.edges()))