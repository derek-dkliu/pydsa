class Edge:
    def __init__(self, v, w, weight):
        self.v = int(v)
        self.w = int(w)
        self.weight = float(weight)

    def either(self):
        return self.v

    def other(self, v):
        if v == self.v: return self.w
        else: return self.v
    
    def __lt__(self, other): 
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __str__(self):
        return f"{self.v}-{self.w} {self.weight:.5f}"