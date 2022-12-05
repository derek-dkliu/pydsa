from collections import deque

class FordFulkerson:
    def __init__(self, G, s, t):
        self.value = 0
        while self._has_augmenting_path(G, s, t):
            bottle = float('inf')
            x = t
            while x != s:
                e = self.edge_to[x]
                bottle = min(bottle, e.residual_capacity_to(x))
                x = e.other(x)
            x = t
            while x != s:
                e = self.edge_to[x]
                e.add_residual_flow_to(x, bottle)
                x = e.other(x)
            self.value += bottle        

    def _has_augmenting_path(self, G, s, t):
        self.marked = [False] * G.V
        self.edge_to = [None] * G.V
        q = deque()
        q.append(s)
        self.marked[s] = True
        while q:
            v = q.popleft()
            for e in G.adj[v]:
                w = e.other(v)
                if not self.marked[w] and e.residual_capacity_to(w) > 0:
                    q.append(w)
                    self.marked[w] = True
                    self.edge_to[w] = e
        return self.marked[t]

    def is_in_cut(self, v):
        return self.marked[v]


if __name__ == '__main__':
    import sys
    from flow_network import FlowNetwork
    G = FlowNetwork.create(sys.stdin)
    s = 0
    t = G.V - 1
    ff = FordFulkerson(G, s, t)

    print(f"Maxflow from {s} to {t}:")
    for v in range(G.V):
        for e in G.adj[v]:
            if e.from_vertex() == v and e.flow > 0:
                print(e)
    print("Mincut:")
    for v in range(G.V):
        if ff.is_in_cut(v):
            print(v, end=" ")
    print()
    print(f"Maxflow value is {ff.value}")