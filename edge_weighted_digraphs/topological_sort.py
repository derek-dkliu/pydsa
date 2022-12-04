from collections import deque

class TopologicalSort:
    def __init__(self, G):
        self.reverse_post = deque()
        # check directed cycle, return if any
        self.marked = [False] * G.V
        self.onstack = [False] * G.V
        for v in range(G.V):
            if not self.marked[v]:
                if self._check(G, v): return

        self.marked = [False] * G.V
        for v in range(G.V):
            if not self.marked[v]:
                self._dfs(G, v)

    def _dfs(self, G, v):
        self.marked[v] = True
        for e in G.adj[v]:
            w = e.to_vertex()
            if not self.marked[w]:
                self._dfs(G, w)
        self.reverse_post.appendleft(v)

    def _check(self, G, v):
        self.marked[v] = True
        self.onstack[v] = True
        for e in G.adj[v]:
            w = e.to_vertex()
            if not self.marked[w]:
                if self._check(G, w): return True
            elif self.onstack[w]:
                return True
        self.onstack[v] = False
        return False

    def has_cycle(self):
        return len(self.reverse_post) == 0

    def get_order(self):
        return self.reverse_post


if __name__ == '__main__':
    import sys
    from edge_weighted_digraph import EdgeWeightedDigraph
    G = EdgeWeightedDigraph.create(sys.stdin)
    t = TopologicalSort(G)
    if t.has_cycle():
        print("Graph is not a DAG")
    else:
        print("Graph has toplogical sort:")
        print(t.get_order())