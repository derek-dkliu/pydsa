from collections import deque
from edge_weighted_digraph import EdgeWeightedDigraph
from edge_weighted_directed_cycle import EdgeWeightedDirectedCycle

class BellmanFordSP:
    """time: O(V * E)"""

    def __init__(self, G, s):
        self.edge_to = [None] * G.V
        self.dist_to = [float('inf')] * G.V
        self.dist_to[s] = 0

        # for _ in range(G.V):
        #     for v in range(G.V):
        #         self._relax(G, v)

        self.cost = 0       # number of edges visted
        self.cycle = None   # negative cycle if any

        self.onqueue = [False] * G.V    # avoid duplicate vertices on queue
        self.queue = deque()            # queue of vertices to relax
        self.queue.append(s)
        self.onqueue[s] = True
        while self.queue and not self.cycle:
            v = self.queue.popleft()
            self.onqueue[v] = False
            self._relax(G, v)

    def _relax(self, G, v):
        for e in G.adj[v]:
            w = e.to_vertex()
            if self.dist_to[w] > self.dist_to[v] + e.weight:
                self.dist_to[w] = self.dist_to[v] + e.weight
                self.edge_to[w] = e
                if not self.onqueue[w]:
                    self.onqueue[w] = True
                    self.queue.append(w)
            # check negative cycle    
            self.cost += 1
            if self.cost % G.V == 0:
                self.find_negative_cycle()
                if self.cycle: return

    def find_negative_cycle(self):
        V = len(self.edge_to)
        T = EdgeWeightedDigraph(V)
        for v in range(V):
            if self.edge_to[v]:
                T.add_edge(self.edge_to[v])
        self.cycle = EdgeWeightedDirectedCycle(T).get_cycle()

    def has_negative_cycle(self):
        return self.cycle is not None

    def get_negative_cycle(self):
        return self.cycle

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
    G = EdgeWeightedDigraph.create(sys.stdin)
    s = int(sys.argv[1])
    sp = BellmanFordSP(G, s)
    print(f"Shortest path from {s} to every other vertex:")
    for v in range(G.V):
        if sp.has_path_to(v):
            print(f"{v} ({sp.cost_to(v):.2f}): {'  '.join(str(e) for e in sp.path_to(v))}")
        else:
            print(f"no path to {v}")