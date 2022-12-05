class FlowEdge:
    def __init__(self, v, w, capacity):
        self.v = int(v)
        self.w = int(w)
        self.capacity = float(capacity)
        self.flow = 0

    def from_vertex(self):
        return self.v

    def to_vertex(self):
        return self.w

    def other(self, v):
        if v == self.v: return self.w
        elif v == self.w: return self.v
        else: raise Exception("Invalid endpoint")

    def residual_capacity_to(self, v):
        if v == self.w: return self.capacity - self.flow
        elif v == self.v: return self.flow
        else: raise Exception("Invalid endpoint")

    def add_residual_flow_to(self, v, delta):
        if v == self.w: self.flow += delta
        elif v == self.v: self.flow -= delta
        else: raise Exception("Invalid endpoint")

    def __str__(self):
        return f"{self.v}->{self.w} {self.flow:.2f}/{self.capacity:.2f}"