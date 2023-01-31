class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def lies_in(self, p1, p2):
        x1, x2 = min(p1.x, p2.x), max(p1.x, p2.x)
        y1, y2 = min(p1.y, p2.y), max(p1.y, p2.y)
        return self.x >= x1 and self.x <= x2 and self.y >= y1 and self.y <= y2

    def __str__(self):
        return f"({self.x}, {self.y})"

def segment_intersection(p1, p2, p3, p4):
    a1, b1 = slope_intercept(p1, p2)
    a2, b2 = slope_intercept(p3, p4)
    if a1 == a2 and b1 == b2:
        if p1.lies_in(p3, p4):
            return p1
        elif p2.lies_in(p3, p4):
            return p2
        elif p3.lies_in(p1, p2):
            return p3
        elif p4.lies_in(p1, p2):
            return p4
    elif a1 != a2:
        x = (b2 - b1) / (a1 - a2)
        y = (b1 * a2 - b2 * a1) / (a2 - a1)
        p = Point(x, y)
        if p.lies_in(p1, p2) and p.lies_in(p3, p4):
            return p
    return None

def slope_intercept(p1, p2):
    a = (p1.y - p2.y) / (p1.x - p2.x)
    b = p1.y - a * p1.x
    return a, b


p1 = Point(1, 4)
p2 = Point(4, 1)
p3 = Point(1, 1)
p4 = Point(3, 4)
print(segment_intersection(p1, p2, p3, p4))

p1 = Point(1, 1)
p2 = Point(3, 3)
p3 = Point(2, 2)
p4 = Point(2.5, 2.5)
print(segment_intersection(p1, p2, p3, p4))