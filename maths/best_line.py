class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    PRECISION = 4

    def __init__(self, p1, p2):
        if Line.equal(p1.x, p2.x):
            self.slope = float('inf')
            self.intercept = Line.round(p1.x)
        else:
            self.slope = Line.round((p1.y - p2.y) / (p1.x - p2.x))
            self.intercept = Line.round(p1.y - p1.x * self.slope)

    def __eq__(self, line):
        return (self.slope, line.slope) == (self.intercept, line.intercept)

    def __hash__(self):
        return hash((self.slope, self.intercept))

    @staticmethod
    def round(val):
        return round(val, Line.PRECISION)

    @staticmethod
    def equal(a, b):
        return Line.round(a) == Line.round(b)

def search_line(points):
    count = {}
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1 = points[i]
            p2 = points[j]
            line = Line(p1, p2)
            if line not in count:
                count[line] = 0
            count[line] += 1

    max_count = 0
    best_line = None
    for line, c in count.items():
        if c > max_count:
            max_count = c
            best_line = line
    return best_line