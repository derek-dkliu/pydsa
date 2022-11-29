from collections import deque

"""
    Use BFS to determine whether an undirected graph has a cycle, if so find such a cycle
"""
class CycleX:
    def __init__(self, G):
        if self.has_parallel_edges(G): return

        self.marked = [False] * G.V
        self.parent = [-1] * G.V
        self.cycle = None
        for v in range(G.V):
            if not self.marked[v]:
                self._bfs(G, v)

    def _bfs(self, G, s):
        q = deque()
        q.append(s)
        self.marked[s] = True
        while q:
            v = q.popleft()
            for w in G.adj[v]:
                if self.cycle: return

                elif not self.marked[w]:
                    self.marked[w] = True
                    self.parent[w] = v
                    q.append(w)
                elif w != self.parent[v]:
                    self.cycle = deque()
                    self.cycle.appendleft(w)
                    x = v
                    while True:
                        self.cycle.appendleft(x)
                        if self.parent[x] == -1: break
                        x = self.parent[x]
                    stack = deque()
                    while w != x and w != -1:
                        stack.append(w)
                        w = self.parent[w]
                    while stack:
                        self.cycle.appendleft(stack.pop())
                    return

    def has_parallel_edges(self, G):
        self.marked = [False] * G.V
        for v in range(G.V):
            for w in G.adj[v]:
                if self.marked[w]:
                    self.cycle = deque()
                    self.cycle.append(v)
                    self.cycle.append(w)
                    self.cycle.append(v)
                    return True
                self.marked[w] = True
            for w in G.adj[v]:
                self.marked[w] = False
        return False

    def hascycle(self):
        return self.cycle != None
    
    def getcycle(self):
        return self.cycle


if __name__ == '__main__':
    import sys
    from graph import Graph
    G = Graph.create(sys.stdin)
    c = CycleX(G)
    if c.hascycle():
        print(f"Graph has cycle:")
        print('-'.join(str(v) for v in c.getcycle()))
    else:
        print(f"Graph is acyclic")