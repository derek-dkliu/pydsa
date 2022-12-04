class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = int(v)
        self.w = int(w)
        self.weight = float(weight)

    def from_vertex(self):
        return self.v

    def to_vertex(self):
        return self.w

    def __lt__(self, other): 
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __str__(self):
        return f"{self.v}->{self.w} {self.weight:.2f}"
