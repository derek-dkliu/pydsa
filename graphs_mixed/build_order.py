from collections import deque

def build_order(projects, dependencies):
    graph = build_graph(projects, dependencies)
    order = order_projects(graph)
    return list(order)

def build_graph(projects, dependencies):
    graph = Graph(projects)
    for p1, p2 in dependencies:
        graph.add_edge(p1, p2)
    return graph

def order_projects(graph):
    marked = set()
    onstack = set()
    order = deque()
    for v in graph.get_nodes():
        if v not in marked:
            if not dfs(graph, v, marked, onstack, order):
                raise Exception("Cycle detected")
    return order

# cycle detection and topological sort are done at the same time
def dfs(graph, v, marked, onstack, order):
    marked.add(v)
    onstack.add(v)
    for w in graph.adjacencies(v):
        if w not in marked:
            if not dfs(graph, w, marked, onstack, order):
                return False
        elif w in onstack:
            return False
    onstack.remove(v)
    order.appendleft(v)
    return True

class Graph:
    def __init__(self, projects):
        self.adj = dict()
        self.indeg = dict()
        for v in projects:
            self.adj[v] = []
            self.indeg[v] = 0

    def __len__(self):
        return len(self.adj)

    def get_nodes(self):
        return self.adj.keys()

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.indeg[w] += 1

    def adjacencies(self, v):
        return self.adj.get(v, [])

    def indegree(self, v):
        return self.indeg.get(v, 0)


def build_order2(projects, dependencies):
    graph = build_graph(projects, dependencies)
    order = order_projects2(graph)
    return list(order)

def order_projects2(graph):
    indegrees = dict()
    for v in graph.get_nodes():
        indegrees[v] = graph.indegree(v)
    queue = deque()
    for v in indegrees:
        if indegrees[v] == 0:
            queue.append(v)
    order = []
    while queue:
        v = queue.popleft()
        order.append(v)
        for w in graph.adjacencies(v):
            indegrees[w] -= 1
            if indegrees[w] == 0:
                queue.append(w)
    if len(order) != len(indegrees):
        raise Exception("No available order")
    return order


projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
print(build_order(projects, dependencies))
print(build_order2(projects, dependencies))

# projects = ['a', 'b', 'c', 'd', 'e', 'f']
# dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), ('c', 'b')]
# print(build_order(projects, dependencies))
# print(build_order2(projects, dependencies))