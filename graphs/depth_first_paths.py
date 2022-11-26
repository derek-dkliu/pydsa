from collections import deque

class DepthFirstPaths:
    def __init__(self, G, s):
        self.marked = [False] * G.V
        self.edge_to = [0] * G.V
        self.s = s
        self._dfs(G, s)

    def _dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self._dfs(G, w)
                self.edge_to[w] = v

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not self.has_path_to(v): return []
        path = deque()
        x = v
        while x != self.s:
            path.appendleft(x)
            x = self.edge_to[x]
        path.appendleft(self.s)
        return path
    
    
if __name__ == '__main__':
    import sys
    from graph import Graph
    G = Graph.create(sys.stdin)
    s = int(sys.argv[1])
    dfs = DepthFirstPaths(G, s)
    for v in range(G.V):
        if dfs.has_path_to(v):
            print(f"{s} to {v}: {'-'.join(str(w) for w in dfs.path_to(v))}")
        else:
            print(f"{s} to {v}: not connnected")
    