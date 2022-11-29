from collections import deque

"""
    Use DFS to determine whether an undirected graph has a cycle, if so find such a cycle
"""
class Cycle:
    def __init__(self, G):
        if self.has_parallel_edges(G): return

        self.marked = [False] * G.V
        self.edge_to = [0] * G.V
        self.cycle = None
        for v in range(G.V):
            if not self.marked[v]:
                self._dfs(G, v)

    def _dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if self.cycle: return

            elif not self.marked[w]:
                self.edge_to[w] = v
                self._dfs(G, w)
            elif w != self.edge_to[v]:    # ignore reverse edge leading to v
                self.cycle = deque()
                self.cycle.appendleft(w)
                x = v
                while x != w:
                    self.cycle.appendleft(x)
                    x = self.edge_to[x]
                self.cycle.appendleft(w)
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
    c = Cycle(G)
    if c.hascycle():
        print(f"Graph has cycle:")
        print('-'.join(str(v) for v in c.getcycle()))
    else:
        print(f"Graph is acyclic")
