from collections import deque

# time: O(V*(V+E))
class ShortestCycle:
    def __init__(self, G):
        self.min = G.V + 1
        self.cycle = None
        for v in range(G.V):
            self._bfs(G, v)

    def _bfs(self, G, s):
        self.marked = [False] * G.V
        self.parent = [-1] * G.V
        self.dist = [0] * G.V
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
                elif w != self.parent[v]:
                    length = self.dist[w] + self.dist[v] + 1
                    if length < self.min:
                        self.min = length
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
                        
    def hascycle(self):
        return self.cycle != None
    
    def getcycle(self):
        return self.cycle


if __name__ == '__main__':
    import sys
    from graph import Graph
    G = Graph.create(sys.stdin)
    c = ShortestCycle(G)
    if c.hascycle():
        print(f"Graph has shortest cycle:")
        print('-'.join(str(v) for v in c.getcycle()))
    else:
        print(f"Graph is acyclic")