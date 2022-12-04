from collections import deque

# time: O(V*(V+E))
class ShortestDirectedCycle:
    def __init__(self, G):
        self.cycle = None
        RG = G.reverse()
        self.min = G.V + 1
        for v in range(G.V):
            finder = ShortestLengthPath(RG, v)
            for w in G.adj[v]:
                if finder.has_path_to(w) and (finder.dist_to(w) + 1) < self.min:
                    self.min = finder.dist_to(w) + 1
                    self.cycle = deque()
                    for x in finder.path_to(w):
                        self.cycle.appendleft(x)
                    self.cycle.appendleft(v)

    def has_cycle(self):
        return self.cycle != None
    
    def get_cycle(self):
        return self.cycle


class ShortestLengthPath:
    def __init__(self, G, s):
        self.marked = [False] * G.V
        self.parent = [-1] * G.V
        self.dist = [0] * G.V
        self.s = s
        q = deque()
        q.append(s)
        self.marked[s] = True
        while q:
            v = q.popleft()
            for w in G.adj[v]:
                if not self.marked[w]:
                    self.marked[w] = True
                    self.parent[w] = v
                    self.dist[w] = self.dist[v] + 1
                    q.append(w)

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not self.has_path_to(v): return []
        path = deque()
        x = v
        while x != self.s:
            path.appendleft(x)
            x = self.parent[x]
        path.appendleft(self.s)
        return path

    def dist_to(self, v):
        return self.dist[v]


if __name__ == '__main__':
    import sys
    from digraph import Digraph
    G = Digraph.create(sys.stdin)
    c = ShortestDirectedCycle(G)
    if c.has_cycle():
        print(f"Graph has shortest directed cycle:")
        print('-'.join(str(v) for v in c.get_cycle()))
    else:
        print(f"Graph is acyclic")