from flow_edge import FlowEdge

class FlowNetwork:
    def __init__(self, V):
        self.V = V
        self.E = 1
        self.adj = [[] for _ in range(V)]

    @staticmethod
    def create(stdin):
        V = int(stdin.readline())
        E = int(stdin.readline())
        G = FlowNetwork(V)
        for _ in range(E):
            v, w, capacity = stdin.readline().split()
            G.add_edge(FlowEdge(v, w, capacity))
        return G

    def add_edge(self, edge):
        v = edge.from_vertex()
        w = edge.to_vertex()
        self.adj[v].append(edge)
        self.adj[w].append(edge)
        self.E += 1

    def __str__(self):
        s = f"{self.V} vertices, {self.E} edges\n"
        s += "\n".join(f"{v}: {'  '.join(str(e) for e in self.adj[v])}" for v in range(self.V))
        return s


if __name__ == '__main__':
    from sys import stdin
    G = FlowNetwork.create(stdin)
    print(G)

    