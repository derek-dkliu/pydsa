from edge_weighted_digraph import EdgeWeightedDigraph
from directed_edge import DirectedEdge
from lp_acyclic import AcyclicLP 

class CPM:
    @staticmethod
    def run(stdin):
        n = int(stdin.readline())
        source = n * 2
        sink = n * 2 + 1
        G = EdgeWeightedDigraph(n * 2 + 2)
        for i in range(n):
            col = stdin.readline().split()
            duration = float(col[0])
            G.add_edge(DirectedEdge(i, i+n, duration))
            G.add_edge(DirectedEdge(source, i, 0))
            G.add_edge(DirectedEdge(i+n, sink, 0))

            m = int(col[1])
            for j in range(m):
                v = int(col[2 + j])
                G.add_edge(DirectedEdge(i+n, v, 0))

        lp = AcyclicLP(G, source)
        print("Job\tStart\tFinish")
        for i in range(n):
            print(f"{i}\t{lp.cost_to(i)}\t{lp.cost_to(i+n)}")
        print(f"Finish time: {lp.cost_to(sink)}")

    @staticmethod
    def run2(stdin):
        n = int(stdin.readline())
        duration = [0] * n
        source = n
        sink = n + 1
        G = EdgeWeightedDigraph(n + 2)
        for v in range(n):
            col = stdin.readline().split()
            duration[v] = float(col[0])
            G.add_edge(DirectedEdge(source, v, 0))
            G.add_edge(DirectedEdge(v, sink, duration[v]))
            m = int(col[1])
            for i in range(m):
                w = int(col[2 + i])
                G.add_edge(DirectedEdge(v, w, duration[v]))

        lp = AcyclicLP(G, source)
        print("Job\tStart\tFinish")
        for v in range(n):
            start = lp.cost_to(v)
            end = start + duration[v]
            print(f"{v}\t{start}\t{end}")
        print(f"Finish time: {lp.cost_to(sink)}")

if __name__ == '__main__':
    import sys
    CPM.run(sys.stdin)
    # CPM.run2(sys.stdin)
