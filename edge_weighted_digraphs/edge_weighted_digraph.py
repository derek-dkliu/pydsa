from directed_edge import DirectedEdge

class EdgeWeightedDigraph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
        self._indegree = [0] * V

    @staticmethod
    def create(stdin):
        V = int(stdin.readline())
        E = int(stdin.readline())
        G = EdgeWeightedDigraph(V)
        for _ in range(E):
            v, w, weight = stdin.readline().split()
            G.add_edge(DirectedEdge(v, w, weight))
        return G

    def add_edge(self, edge):
        v = edge.from_vertex()
        w = edge.to_vertex()
        self.adj[v].append(edge)
        self._indegree[w] += 1
        self.E += 1

    def outdegree(self, v):
        return len(self.adj[v])

    def indegree(self, v):
        return self._indegree[v]

    def reverse(self):
        G = EdgeWeightedDigraph(self.V)
        for v in range(self.V):
            for e in self.adj[v]:
                G.add_edge(DirectedEdge(e.to_vertex(), e.from_vertex(), e.weight))
        return G

    def edges(self):
        return [e for v in range(self.V) for e in self.adj[v]]

    def __str__(self):
        s = f"{self.V} vertices, {self.E} edges\n"
        s += "\n".join(f"{v}: {'  '.join(str(w) for w in self.adj[v])}" for v in range(self.V))
        return s


if __name__ == '__main__':
    from sys import stdin
    G = EdgeWeightedDigraph.create(stdin)
    print(G)
    print(G.reverse())