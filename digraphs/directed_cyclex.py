from collections import deque

class DirectedCycleX:
    def __init__(self, G):
        self.cycle = None
        self.indegree = [G.indegree(v) for v in range(G.V)]

        # queue to have vertices with zero indgree
        q = deque()
        for v in range(G.V):
            if self.indegree[v] == 0:
                q.append(v)
        
        while q:
            v = q.popleft()
            for w in G.adj[v]:
                self.indegree[w] -= 1
                if self.indegree[w] == 0:
                    q.append(w)

        root = -1   # any vertex with indegree > 0
        edge_to = [0] * G.V
        for v in range(G.V):
            if self.indegree[v] > 0:
                root = v
                for w in G.adj[v]:
                    if self.indegree[w] > 0:
                        edge_to[w] = v

        # create the cycle if any
        if root != -1:
            # set root to be any vertex on cycle
            visited = [False] * G.V
            while not visited[root]:
                visited[root] = True
                root = edge_to[root]

            # form the cycle
            self.cycle = deque()
            x = root
            while True:
                self.cycle.appendleft(x)
                x = edge_to[x]
                if x == root:
                    break
            self.cycle.appendleft(root)

    def hascycle(self):
        return self.cycle != None

    def getcycle(self):
        return list(self.cycle)


if __name__ == '__main__':
    from sys import stdin
    from digraph import Digraph
    G = Digraph.create(stdin)
    c = DirectedCycleX(G)
    if c.hascycle():
        print("Graph has a directed cycle:")
        print(c.getcycle())
    else:
        print("Graph is a DAG")