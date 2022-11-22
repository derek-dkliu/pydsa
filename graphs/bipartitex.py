from collections import deque

"""
    Use BFS to determine whether an undirected graph is bipartite, and
    find either a bipartition or an odd-length cycle
"""
class BipartiteX:
    def __init__(self, G):
        self.marked = [False] * G.V
        self.color = [False] * G.V
        self.edge_to = [0] * G.V
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
                if not self.marked[w]:
                    q.append(w)
                    self.marked[w] = True
                    self.color[w] = not self.color[v]
                    self.edge_to[w] = v
                elif self.color[w] == self.color[v]:
                    self.cycle = deque()
                    stack = deque()
                    x, y = v, w
                    while x != y:
                        self.cycle.append(y)
                        stack.append(x)
                        x = self.edge_to[x]
                        y = self.edge_to[y]
                    stack.append(x)
                    while stack:
                        self.cycle.append(stack.pop())
                    self.cycle.append(w)
                    return

    def isbipartite(self):
        return self.cycle == None

    def getcycle(self):
        return self.cycle

    def getcolor(self, v):
        if self.isbipartite():
            return self.color[v]
        else:
            raise ValueError("graph is not bipartite")


if __name__ == '__main__':
    import sys
    from graph import Graph
    G = Graph.create(sys.stdin)
    b = BipartiteX(G)
    if b.isbipartite():
        for v in range(G.V):
            print(f"{v}: {b.getcolor(v)}")
    else:
        print("Graph has an odd-length cycle:")
        print("-".join(str(v) for v in b.getcycle()))
