from collections import deque

class DirectedCycle:
    def __init__(self, G):
        self.marked = [False] * G.V
        self.onstack = [False] * G.V
        self.edge_to = [0] * G.V
        self.cycle = None

        for v in range(G.V):
            if not self.marked[v] and not self.cycle:
                self._dfs(G, v)
    
    def _dfs(self, G, v):
        self.marked[v] = True
        self.onstack[v] = True
        for w in G.adj[v]:
            if self.cycle: return
            
            if not self.marked[w]:
                self.edge_to[w] = v
                self._dfs(G, w)
            elif self.onstack[w]:
                self.cycle = deque()
                self.cycle.appendleft(w)
                x = v
                while x != w:
                    self.cycle.appendleft(x)
                    x = self.edge_to[x]
                self.cycle.appendleft(w)
                return
        self.onstack[v] = False

    def hascycle(self):
        return self.cycle != None

    def getcycle(self):
        return list(self.cycle)


if __name__ == '__main__':
    from sys import stdin
    from digraph import Digraph
    G = Digraph.create(stdin)
    c = DirectedCycle(G)
    if c.hascycle():
        print("Graph has a directed cycle:")
        print(c.getcycle())
    else:
        print("Graph is a DAG")