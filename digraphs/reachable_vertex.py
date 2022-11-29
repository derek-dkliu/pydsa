from collections import deque

class ReachableVertex:
    def __init__(self, G):
        self.vertex = None
        self.marked = [False] * G.V
        RG = G.reverse()
        # get reverse postorder of the reverse graph
        self.reverse_post = deque()
        for v in range(RG.V):
            if not self.marked[v]:
                self._dfs(RG, v)

        # check if the first vertex in reverse postorder can
        # reach all other vertices in the reverse graph, if so,
        # this is the vertex reachable from every other vertex in original graph
        s = self.reverse_post[0]
        self.marked = [False] * G.V
        self._dfs(RG, s)
        if all(self.marked):
            self.vertex = s

    def _dfs(self, G, v):
        self.marked[v] = True
        for w in G.adj[v]:
            if not self.marked[w]:
                self._dfs(G, w)
        self.reverse_post.appendleft(v)
        

if __name__ == '__main__':
    import sys
    from digraph import Digraph
    G = Digraph.create(sys.stdin)
    r = ReachableVertex(G)
    if r.vertex:
        print(f"Vertex {r.vertex} is reachable from every other vertex.")
    else:
        print(f"Graph have no vertex reachable from every other vertex.")