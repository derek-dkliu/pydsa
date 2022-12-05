from collections import deque

class MonotonicSP:
    """A path is monotonic if the sequence of edge weights along the path are 
    either strictly increasing or strictly decreasing. time: O(E*log(E))"""

    def __init__(self, G, s):
        self.edge_to1 = [None] * G.V
        self.dist_to1 = [float('inf')] * G.V
        self.dist_to1[s] = 0
        edges = sorted(G.edges(), key=lambda e: e.weight)
        for e in edges:
            self._relax(e, self.edge_to1, self.dist_to1)

        self.edge_to2 = [None] * G.V
        self.dist_to2 = [float('inf')] * G.V
        self.dist_to2[s] = 0
        edges = sorted(G.edges(), key=lambda e: e.weight, reverse=True)
        for e in edges:
            self._relax(e, self.edge_to2, self.dist_to2)


    def _relax(self, e, edge_to, dist_to):
        v = e.from_vertex()
        w = e.to_vertex()
        if dist_to[w] > dist_to[v] + e.weight:
            dist_to[w] = dist_to[v] + e.weight
            edge_to[w] = e

    def has_path_to(self, v):
        return self.dist_to1[v] < float('inf') or self.dist_to2[v] < float('inf')

    def path_to(self, v):
        edge_to = self.edge_to1 if self.dist_to1[v] <= self.dist_to2[v] else self.edge_to2
        path = deque()
        e = edge_to[v]
        while e is not None:
            path.appendleft(e)
            e = edge_to[e.from_vertex()]
        return path

    def cost_to(self, v):
        return min(self.dist_to1[v], self.dist_to2[v])


if __name__ == '__main__':
    import sys
    from edge_weighted_digraph import EdgeWeightedDigraph
    G = EdgeWeightedDigraph.create(sys.stdin)
    s = int(sys.argv[1])
    m = MonotonicSP(G, s)
    print(f"Shortest path from {s} to every other vertex:")
    for v in range(G.V):
        if m.has_path_to(v):
            print(f"{v} ({m.cost_to(v):.2f}): {'  '.join(str(e) for e in m.path_to(v))}")
        else:
            print(f"no path to {v}")