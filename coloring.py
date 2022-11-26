class Coloring:
    def __init__(self, G, colors):
        self.assigned = [None] * G.V
        for v in range(G.V):
            if not self.assigned[v]:
                if not self._dfs(G, v, colors):
                    self.assigned = None
                    break

    def _dfs(self, G, v, colors):
        opt = []
        if v == 0:
            opt.append(colors[0])
        else:
            used = set()
            for w in G.adj[v]:
                if self.assigned[w]:
                    used.add(self.assigned[w])
            for c in colors:
                if c not in used:
                    opt.append(c)

        for c in opt:
            self.assigned[v] = c
            success = True
            for w in G.adj[v]:
                if not self.assigned[w]:
                    if not self._dfs(G, w, colors):
                        success = False
                        break
            if not success: 
                self.assigned[v] = None
            else:
                return True
        return False

if __name__ == '__main__':
    import sys
    from graphs.graph import Graph
    G = Graph.create(sys.stdin)
    c = Coloring(G, ['R', 'G', 'B'])
    if c.assigned:
        print(f"Graph has following color assignment:")
        print(c.assigned)
    else:
        print(f"Graph has no feasible coloring assignment")

        
