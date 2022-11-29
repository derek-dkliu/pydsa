from topological import Topological

"""
Find the topological order of the DAG and check if there is an edge between
each consecutive pair of vertices in the order.
"""
class HamiltonianPathInDAG:
    @classmethod
    def find(cls, G):
        t = Topological(G)
        if not t.isdag(): 
            raise Exception("Graph is not a DAG")

        path = t.getorder()
        for i in range(len(path) - 1):
            v = path[i]
            w = path[i + 1]
            if w not in G.adj[v]: return None
        return path


if __name__ == '__main__':
    import sys
    from digraph import Digraph
    G = Digraph.create(sys.stdin)
    path = HamiltonianPathInDAG.find(G)
    if path:
        print(f"Graph has hamiltonian path:")
        print('-'.join(str(v) for v in path))
    else:
        print(f"Graph does not have hamiltonian path")
