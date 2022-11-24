class Binconnectivity:
    def __init__(self, G):
        self.pre = [-1] * G.V
        self.low = [-1] * G.V
        self.cnt = 0
        self.articulations = [False] * G.V
        for v in range(G.V):
            if self.pre[v] == -1:
                self._dfs(G, v, v)

    def _dfs(self, G, v, u):
        self.pre[v] = self.cnt
        self.low[v] = self.cnt
        self.cnt += 1
        children = 0
        for w in G.adj[v]:
            if self.pre[w] == -1:
                children += 1
                self._dfs(G, w, v)
                self.low[v] = min(self.low[v], self.low[w])
                # non-root of DFS is an articulation point if low[w] >= pre[v]
                if v != u and self.low[w] >= self.pre[v]:
                    self.articulations[v] = True
            elif w != u:
                self.low[v] = min(self.low[v], self.pre[w])
        # root of DFS is an articulation point if it has more than 1 child
        if v == u and children > 1:
            self.articulations[v] = True

    def get_articulations(self):
        ap = []
        for v, bool in enumerate(self.articulations):
            if bool: ap.append(v)
        return ap

if __name__ == '__main__':
    import sys
    from graph import Graph
    G = Graph.create(sys.stdin)
    b = Binconnectivity(G)
    articulations = b.get_articulations()
    if articulations:
        print(f"Graph has {len(articulations)} articulation points:")
        print(articulations)
    else:
        print(f"Graph is biconnected")    