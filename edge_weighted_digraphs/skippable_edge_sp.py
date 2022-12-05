from sp_dijkstra import DijkstraSP

class SkippableEdgeSP:
    """time: O(E*log(V))"""

    @staticmethod
    def find(G, s, t):
        sp1 = DijkstraSP(G, s)
        sp2 = DijkstraSP(G.reverse(), t)

        p1 = None
        p2 = None
        min = float('inf')
        for e in G.edges():
            v = e.from_vertex()
            w = e.to_vertex()
            cost = sp1.cost_to(v) + sp2.cost_to(w)
            if cost < min:
                min = cost
                p1 = sp1.path_to(v)
                p2 = sp2.path_to(w)
        return list(p1) + list(reversed(p2))

if __name__ == '__main__':
    import sys
    from edge_weighted_digraph import EdgeWeightedDigraph
    G = EdgeWeightedDigraph.create(sys.stdin)
    s = int(sys.argv[1])
    t = int(sys.argv[2])
    print("The skippable-edge shortest path is:")
    print('  '.join(str(e) for e in SkippableEdgeSP.find(G, s, t)))
    