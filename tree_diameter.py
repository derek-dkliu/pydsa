from collections import deque

"""
The diameter of n-ary tree is the longest path between two leaf nodes.
"""
class TreeDiameter:
    def __init__(self, G):
        # find one of the endpoints of the diameter
        s = self._bfs(G, 0)[0]

        # find the other endpoint
        t, edge_to = self._bfs(G, s)

        # form path from edge_to
        self.path = deque()
        x = t
        while x != s:
            self.path.appendleft(x)
            x = edge_to[x]
        self.path.appendleft(s)

    def _bfs(self, G, s):
        marked = [False] * G.V
        edge_to = [0] * G.V
        last_node = None
        q = deque()
        q.append(s)
        marked[s] = True
        while q:
            v = q.popleft()
            last_node = v
            for w in G.adj[v]:
                if not marked[w]:
                    marked[w] = True
                    edge_to[w] = v
                    q.append(w)
        return (last_node, edge_to)


if __name__ == '__main__':
    import sys
    from graphs.graph import Graph
    G = Graph.create(sys.stdin)
    d = TreeDiameter(G)
    print(f"Tree graph with diameter:")
    print('-'.join(str(v) for v in d.path))
