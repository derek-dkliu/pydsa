class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, point):
        return self.x == point.x and self.y == point.y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Square:
    def __init__(self, x, y, length):
        self.point = Point(x, y)
        self.length = length

    def center(self):
        x = self.point.x + self.length / 2
        y = self.point.y + self.length / 2
        return Point(x, y)

def bisect_squares(sq1, sq2):
    c1 = sq1.center()
    c2 = sq2.center()
    h1 = sq1.length / 2
    h2 = sq2.length / 2
    if c1 == c2:
        h = max(h1, h2)
        p1 = Point(c1.x - h, c1.y - h)
        p2 = Point(c1.x + h, c1.y + h)
        return (p1, p2)
        
    slope = (c1.y - c2.y) / (c1.x - c2.x)
    if abs(slope) <= 1:
        p1 = Point(c1.x - h1, c1.y - h1 * slope)
        p2 = Point(c2.x + h2, c2.y + h2 * slope)
        return (p1, p2)
    else:
        p1 = Point(c1.x - h1 / slope, c1.y - h1)
        p2 = Point(c2.x + h2 / slope, c2.y + h2)
        return (p1, p2)

cases = [
    ((2,2,1), (5,5,3)),
    ((2,2,2), (3,5,3)),
    ((2,2,2), (1,1,4))
]
for (a, b, c), (d, e, f) in cases:
    sq1 = Square(a, b, c)
    sq2 = Square(d, e, f)
    line = bisect_squares(sq1, sq2)
    print(*line)