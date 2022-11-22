class CC:
    def __init__(self, G):
        self.marked = [False] * G.V
        self.id = [0] * G.V         # component id
        self.size = [0] * G.V       # component size
        self.count = 0              # number of components
        for v in range(G.V):
            if not self.marked[v]:
                self._dfs(G, v)
                self.count += 1
    
    def _dfs(self, G, v):
        self.marked[v] = True
        self.id[v] = self.count
        self.size[self.count] += 1
        for w in G.adj[v]:
            if not self.marked[w]:
                self._dfs(G, w)

    def connected(self, v, w):
        return self.id[v] == self.id[w]

    def getid(self, v):
        return self.id[v]

    def getsize(self, v):
        return self.size[self.id[v]]

    def getcount(self):
        return self.count


if __name__ == '__main__':
    import sys
    from graph import Graph
    G = Graph.create(sys.stdin)
    cc = CC(G)
    components = [[] for _ in range(cc.getcount())]
    for v in range(G.V):
        components[cc.getid(v)].append(v)
    print(f"{len(components)} components")
    for index, component in enumerate(components):
        print(f"{index}: {component}")

