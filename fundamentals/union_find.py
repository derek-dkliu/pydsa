class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def union(self, p, q):
        pid = self.find(p)
        qid = self.find(q)
        if pid == qid: return

        if self.rank[pid] < self.rank[qid]:
            self.parent[pid] = qid
        elif self.rank[pid] > self.rank[qid]:
            self.parent[qid] = pid
        else:
            self.parent[qid] = pid
            self.rank[pid] += 1
        self.count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while p != self.parent[p]:
            # make every other node in path point to its grandparent (thereby halving path length)
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p