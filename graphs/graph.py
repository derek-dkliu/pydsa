class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(self.V)]

    @classmethod
    def create(cls, stdin):          
        V = int(stdin.readline())
        E = int(stdin.readline())
        G = cls(V)
        for _ in range(E):
            v, w = stdin.readline().split()
            G.add_edge(v, w)
        return G

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def __str__(self):
        s = "%d vertices, %d edges\n" % (self.V, self.E)
        s += "\n".join("%d: %s" % (v, " ".join(str(w) for w in self.adj[v])) for v in range(self.V))
        return s

if __name__ == '__main__':
    from sys import stdin
    G = Graph.create(stdin)
    print(G)