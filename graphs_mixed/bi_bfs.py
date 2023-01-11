from collections import deque

class BiBFS:
    def __init__(self, G, s, t):
        self.marked1 = [False] * G.V
        self.marked2 = [False] * G.V
        self.parent1 = [None] * G.V
        self.parent2 = [None] * G.V
        self.path = None
        self._bibfs(G, s, t)

    def _bibfs(self, G, s, t):
        if s == t:
            self.path = deque([s])
            return
        q1 = deque()
        q2 = deque()
        q1.append(s)
        q2.append(t)
        self.marked1[s] = True
        self.marked2[t] = True
        while q1 and q2:
            # v = q1.popleft()
            # for w in G.adj[v]:
            #     if not self.marked1[w]:
            #         self.marked1[w] = True
            #         self.parent1[w] = v
            #         if self.marked2[w]:
            #             self._build_path(w, s, t)
            #             return
            #         q1.append(w)
            # v = q2.popleft()
            # for w in G.adj[v]:
            #     if not self.marked2[w]:
            #         self.marked2[w] = True
            #         self.parent2[w] = v
            #         if self.marked1[w]:
            #             self._build_path(w, s, t)
            #             return
            #         q2.append(w)
            if self._visit_by_level(G, s, t, q1, self.marked1, self.parent1, self.marked2) or \
                self._visit_by_level(G, s, t, q2, self.marked2, self.parent2, self.marked1):
                break
            
    def _visit_by_level(self, G, s, t, q, marked, parent, visited):
        v = q.popleft()
        for w in G.adj[v]:
            if not marked[w]:
                marked[w] = True
                parent[w] = v
                q.append(w)
                if visited[w]:
                    self._build_path(w, s, t)
                    return True
        return False

    def _build_path(self, w, s, t):
        self.path = deque()
        x = w
        while x != s:
            self.path.appendleft(x)
            x = self.parent1[x]
        self.path.appendleft(s)

        self.path.pop()
        x = w
        while x != t:
            self.path.append(x)
            x = self.parent2[x]
        self.path.append(t)

    def has_path(self):
        return self.path is not None

    def get_path(self):
        return list(self.path)

if __name__ == '__main__':
    import sys, os
    sys.path.insert(0, os.getcwd())
    from graphs.graph import Graph
    G = Graph.create(sys.stdin)
    s = int(sys.argv[1])
    t = int(sys.argv[2])
    bibfs = BiBFS(G, s, t)
    print(bibfs.get_path())