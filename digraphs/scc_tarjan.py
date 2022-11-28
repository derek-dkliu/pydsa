from collections import deque

class SccTarjan:
    def __init__(self, G):
        self.pre = [-1] * G.V
        self.low = [-1] * G.V
        self.index = 0

        self.onstack = [False] * G.V
        self.stack = deque()
        self.scc = [0] * G.V
        self.size = [0] * G.V
        self.count = 0
        for v in range(G.V):
            if self.pre[v] == -1:
                self._dfs(G, v)

    def _dfs(self, G, v):
        self.pre[v] = self.index
        self.low[v] = self.index
        self.index += 1
        self.stack.append(v)
        self.onstack[v] = True
        for w in G.adj[v]:
            if self.pre[w] == -1:
                self._dfs(G, w)
                self.low[v] = min(self.low[v], self.low[w])
            elif self.onstack[w]:
                self.low[v] = min(self.low[v], self.pre[w])

        if self.low[v] == self.pre[v]:
            while True:
                x = self.stack.pop()
                self.onstack[x] = False
                self.scc[x] = self.count
                self.size[self.count] += 1
                if x == v: break
            self.count += 1

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
    scc = SccTarjan(G)
    components = [[] for _ in range(scc.getcount())]
    for v in range(G.V):
        components[scc.getid(v)].append(v)
    print(f"{len(components)} strong components")
    for index, component in enumerate(components):
        print(f"{index}: {component}")