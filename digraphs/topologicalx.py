from collections import deque

class TopologicalX:
    def __init__(self, G):
        self.order = []
        self.indegree = [G.indegree(v) for v in range(G.V)]

        q = deque()
        for v in range(G.V):
            if self.indegree[v] == 0:
                q.append(v)

        while q:
            v = q.popleft()
            self.order.append(v)
            for w in G.adj[v]:
                self.indegree[w] -= 1
                if self.indegree[w] == 0:
                    q.append(w)

        if len(self.order) != G.V:
            self.order = None

    def isdag(self):
        return self.order != None

    def getorder(self):
        return self.order

if __name__ == '__main__':
    from sys import stdin
    from digraph import Digraph
    G = Digraph.create(stdin)
    t = TopologicalX(G)
    if t.isdag():
        print("Graph has toplogical sort:")
        print(t.getorder())
    else:
        print("Graph is not a DAG")
