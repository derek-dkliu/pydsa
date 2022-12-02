import sys, os
sys.path.insert(0, os.getcwd())
from fundamentals.min_pq_index import IndexMinPQ

class MinFeedbackEdges:
    def __init__(self, G):
        self.feedback = []
        self.mst = set()
        self.marked = [False] * G.V
        self.pq = IndexMinPQ(G.V)
        # negate all edges so as to facilitate to use minPQ
        for e in G.edges():
            e.weight *= -1
        for v in range(G.V):
            if not self.marked[v]:
                self._prim(G, v)
        # select edges not in the mst
        for e in G.edges():
            e.weight *= -1
            if e not in self.mst:
                self.feedback.append(e)

    def _prim(self, G, s):
        self._visit(G, s)
        while self.pq:
            self.mst.add(self.pq.min_key())
            self._visit(G, self.pq.pop())

    def _visit(self, G, v):
        self.marked[v] = True
        for e in G.adj[v]:
            w = e.other(v)
            if not self.marked[w]:
                if not self.pq.contains(w):
                    self.pq.push(w, e)
                elif e < self.pq.get_key(w):
                    self.pq.decrease_key(w, e)

    def edges(self):
        return self.feedback

if __name__ == '__main__':
    from sys import stdin
    from edge_weighted_graph import EdgeWeightedGraph
    G = EdgeWeightedGraph.create(stdin)
    f = MinFeedbackEdges(G)
    print("Graph has minimum feedback edge set:")
    print('\n'.join(str(e) for e in f.edges()))