from collections import deque

class SccKosaraju:
    def __init__(self, G):
        self.marked = [False] * G.V
        self.scc = [0] * G.V
        self.size = [0] * G.V
        self.count = 0

        self._set_reverse_post(G.reverse())
        self.marked = [False] * G.V

        for v in self.reverse_post:
            if not self.marked[v]:
                self._dfs2(G, v)
                self.count += 1

    def _set_reverse_post(self, G):
        self.reverse_post = deque()
        for v in range(G.V):
            if not self.marked[v]:
                self._dfs1(G, v)

    def _dfs1(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self._dfs1(G, w)
        self.reverse_post.appendleft(v)

    def _dfs2(self, G, v):
        self.marked[v] = True
        self.scc[v] = self.count
        self.size[self.count] += 1
        for w in G.adj[v]:
            if not self.marked[w]:
                self._dfs2(G, w)

    def connected(self, v, w):
        return self.scc[v] == self.scc[w]

    def getid(self, v):
        return self.scc[v]

    def getsize(self, v):
        return self.size[self.scc[v]]

    def getcount(self):
        return self.count


if __name__ == '__main__':
    import sys
    from digraph import Digraph
    G = Digraph.create(sys.stdin)
    scc = SccKosaraju(G)
    components = [[] for _ in range(scc.getcount())]
    for v in range(G.V):
        components[scc.getid(v)].append(v)
    print(f"{len(components)} strong components")
    for index, component in enumerate(components):
        print(f"{index}: {component}")