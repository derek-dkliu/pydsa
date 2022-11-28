class Bridge:
    def __init__(self, G):
        self.pre = [-1] * G.V   # preorder in which dfs examine v
        self.low = [-1] * G.V   # lowest preorder of any verterx connected to v
        self.index = 0          # index counter
        self.bridges = []
        for v in range(G.V):
            if self.pre[v] == -1:
                self._dfs(G, v, v)

    def _dfs(self, G, v, u):
        self.pre[v] = self.index
        self.low[v] = self.index
        self.index += 1
        for w in G.adj[v]:
            if self.pre[w] == -1:
                self._dfs(G, w, v)
                # propagate descendant's low number to v
                self.low[v] = min(self.low[v], self.low[w])
                # add v-w to bridges if no back edges from subtree rooted at w point to v or its ancesters
                if self.low[w] > self.pre[v]:
                    self.bridges.append(f"{v}-{w}")
            elif w != u:    # ignore reverse edge leading to v
                # update low number 
                self.low[v] = min(self.low[v], self.pre[w])

if __name__ == '__main__':
    import sys
    from graph import Graph
    G = Graph.create(sys.stdin)
    b = Bridge(G)
    if b.bridges:
        print(f"Graph has {len(b.bridges)} bridges:")
        print(b.bridges)
    else:
        print(f"Graph has no bridges")

