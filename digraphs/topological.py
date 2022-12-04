from collections import deque
from directed_cycle import DirectedCycle

class Topological:
    def __init__(self, G):
        self.marked = [False] * G.V
        self.reverse_post = deque()
        # check if G is a DAG
        if DirectedCycle(G).has_cycle(): return

        for v in range(G.V):
            if not self.marked[v]:
                self._dfs(G, v)

    def _dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self._dfs(G, w)
        self.reverse_post.appendleft(v)

    def isdag(self):
        return len(self.reverse_post) > 0

    def getorder(self):
        return list(self.reverse_post)


if __name__ == '__main__':
    from sys import stdin
    from digraph import Digraph
    G = Digraph.create(stdin)
    t = Topological(G)
    if t.isdag():
        print("Graph has toplogical sort:")
        print(t.getorder())
    else:
        print("Graph is not a DAG")