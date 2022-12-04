from edge import Edge

class EdgeWeightedGraph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]

    @staticmethod
    def create(stdin):
        V = int(stdin.readline())
        E = int(stdin.readline())
        G = EdgeWeightedGraph(V)
        for _ in range(E):
            v, w, weight = stdin.readline().split()
            G.add_edge(Edge(v, w, weight))
        return G

    def add_edge(self, edge):
        v = edge.either()
        w = edge.other(v)
        self.adj[v].append(edge)
        self.adj[w].append(edge)
        self.E += 1

    def degree(self, v):
        return len(self.adj[v])

    def edges(self):
        edges = []
        for v in range(self.V):
            self_loops = 0
            for e in self.adj[v]:
                if e.other(v) > v:
                    edges.append(e)
                elif e.other(v) is v:
                    if self_loops % 2 == 0:
                        edges.append(e)
                    self_loops += 1
        return edges

    def __str__(self):
        s = f"{self.V} vertices, {self.E} edges\n"
        s += "\n".join(f"{v}: {'  '.join(str(e) for e in self.adj[v])}" for v in range(self.V))
        return s


if __name__ == '__main__':
    from sys import stdin
    G = EdgeWeightedGraph.create(stdin)
    print(G)