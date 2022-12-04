class Digraph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]
        self._indegree = [0] * V

    @staticmethod
    def create(stdin):
        V = int(stdin.readline())
        E = int(stdin.readline())
        G = Digraph(V)
        for _ in range(E):
            v, w = stdin.readline().split()
            G.add_edge(v, w)
        return G

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].append(w)
        self._indegree[w] += 1
        self.E += 1

    def outdegree(self, v):
        return len(self.adj[v])

    def indegree(self, v):
        return self._indegree[v]

    def reverse(self):
        G = Digraph(self.V)
        for v in range(self.V):
            for w in self.adj[v]:
                G.add_edge(w, v)
        return G

    def __str__(self):
        s = f"{self.V} vertices, {self.E} edges\n"
        s += "\n".join(f"{v}: {' '.join(str(w) for w in self.adj[v])}" for v in range(self.V))
        return s


if __name__ == '__main__':
    from sys import stdin
    G = Digraph.create(stdin)
    print(G)
