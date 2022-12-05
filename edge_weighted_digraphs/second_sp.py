from sp_dijkstra import DijkstraSP
from directed_edge import DirectedEdge

class SecondSP:
    """time: O(E*log(V))"""
    
    @staticmethod
    def find(G, s, t):
        sp1 = DijkstraSP(G, s)
        sp2 = DijkstraSP(G.reverse(), t)

        used = set()
        for e in sp1.path_to(t):
            used.add(e.from_vertex())
        used.add(t)

        p1 = None
        p2 = None
        min = float('inf')
        for v in range(G.V):
            if v not in used:
                cost = sp1.cost_to(v) + sp2.cost_to(v)
                if cost < min:
                    min = cost
                    p1 = sp1.path_to(v)
                    p2 = sp2.path_to(v)

        for e in reversed(p2):
            p1.append(DirectedEdge(e.to_vertex(), e.from_vertex(), e.weight))
        return p1


if __name__ == '__main__':
    import sys
    from edge_weighted_digraph import EdgeWeightedDigraph
    G = EdgeWeightedDigraph.create(sys.stdin)
    s = int(sys.argv[1])
    t = int(sys.argv[2])
    print("The second shortest path is:")
    print('  '.join(str(e) for e in SecondSP.find(G, s, t)))