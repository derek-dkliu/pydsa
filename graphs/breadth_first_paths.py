from collections import deque

class BreadthFirstPaths:
    def __init__(self, G, s):
        self.marked = [False] * G.V
        self.edge_to = [0] * G.V
        self.dist_to = [0] * G.V
        self.s = s
        self._bfs(G, s)

    def _bfs(self, G, s):
        q = deque()
        q.append(s)
        self.marked[s] = True
        while q:
            v = q.popleft()
            for w in G.adj[v]:
                if not self.marked[w]:
                    q.append(w)
                    self.marked[w] = True
                    self.edge_to[w] = v
                    self.dist_to[w] = self.dist_to[v] + 1

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
    bfs = BreadthFirstPaths(G, s)
    for v in range(G.V):
        if bfs.has_path_to(v):
            print(f"{s} to {v}: {'-'.join(str(w) for w in bfs.path_to(v))}")
        else:
            print(f"{s} to {v}: not connnected")