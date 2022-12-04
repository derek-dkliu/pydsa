import math
from edge_weighted_digraph import EdgeWeightedDigraph
from directed_edge import DirectedEdge
from sp_bellman_ford import BellmanFordSP

class Arbitrage:
    @staticmethod
    def find(stdin):
        V = int(stdin.readline())
        G = EdgeWeightedDigraph(V)
        name = [None] * V
        for v in range(V):
            col = stdin.readline().split()
            name[v] = col[0]
            for w in range(V):
                rate = float(col[w + 1])
                G.add_edge(DirectedEdge(v, w, -math.log(rate)))

        b = BellmanFordSP(G, 0)
        if b.has_negative_cycle():
            stake = 1000.0
            for e in b.get_negative_cycle():
                print(f"{stake:10.5f} {name[e.from_vertex()]}", end=' ')
                stake *= math.exp(-e.weight)
                print(f"= {stake:10.5f} {name[e.to_vertex()]}")
        else:
            print("No arbitrage opportunity")

if __name__ == '__main__':
    import sys
    Arbitrage.find(sys.stdin)
