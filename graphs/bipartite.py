from collections import deque

"""
    Use DFS to determine whether an undirected graph is bipartite, and
    find either a bipartition or an odd-length cycle
"""
class Bipartite:
    def __init__(self, G):
        self.marked = [False] * G.V
        self.color = [False] * G.V
        self.edge_to = [0] * G.V
        self.cycle = None
        for v in range(G.V):
            if not self.marked[v]:
                self._dfs(G, v)

    def _dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if self.cycle: return

            if not self.marked[w]:
                self.color[w] = not self.color[v]
                self.edge_to[w] = v
                self._dfs(G, w)
            elif self.color[w] == self.color[v]:
                self.cycle = deque()
                self.cycle.appendleft(w)
                x = v
                while x != w:
                    self.cycle.appendleft(x)
                    x = self.edge_to[x]
                self.cycle.appendleft(w)
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
    b = Bipartite(G)
    if b.isbipartite():
        for v in range(G.V):
            print(f"{v}: {b.getcolor(v)}")
    else:
        print("Graph has an odd-length cycle:")
        print("-".join(str(v) for v in b.getcycle()))