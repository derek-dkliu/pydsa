from enum import Enum
import random

class EdgeType(Enum):
    Inner = 0
    Outer = 1
    Flat = 2

    @staticmethod
    def random():
        return random.choice([EdgeType.Inner, EdgeType.Outer])

    def opposite(self):
        if self is EdgeType.Inner: return EdgeType.Outer
        elif self is EdgeType.Outer: return EdgeType.Inner
        else: return None

class Orientation(Enum):
    Top = 0
    Right = 1
    Bottom = 2
    Left = 3

    def next(self, shift = 1):
        orientations = list(Orientation)
        return orientations[(self.value + shift) % len(orientations)]

    def opposite(self):
        if self is Orientation.Top: return Orientation.Bottom
        elif self is Orientation.Right: return Orientation.Left
        elif self is Orientation.Bottom: return Orientation.Top
        elif self is Orientation.Left: return Orientation.Right
        else: return None

class Puzzle:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.pieces = [None] * (n * m)
        self.create_pieces()

    def solve(self):
        n = self.n
        m = self.m
        solution = [[None] * m for _ in range(n)]
        corners, borders, insides = self.classify_pieces()
        for i in range(n):
            for j in range(m):
                pieces = self.get_pieces_group(i, j, corners, borders, insides)
                for piece in pieces:
                    if piece.fits_in(i, j, solution):
                        solution[i][j] = piece
                        pieces.remove(piece)
                        break
                if solution[i][j] is None:
                    for row in solution:
                        print(*row)
                    raise Exception("Cannot solve!")
        return solution

    def classify_pieces(self):
        corners = set()
        borders = set()
        insides = set()
        for piece in self.pieces:
            if piece.is_corner():
                corners.add(piece)
            elif piece.is_border():
                borders.add(piece)
            else:
                insides.add(piece)
        return corners, borders, insides

    def get_pieces_group(self, row, col, corners, borders, insides):
        if self.is_row_border(row) and self.is_col_border(col):
            return corners
        elif self.is_row_border(row) or self.is_col_border(col):
            return borders
        else:
            return insides

    def is_row_border(self, row):
        return row == 0 or row == self.n - 1

    def is_col_border(self, col):
        return col == 0 or col == self.m - 1

    def get_row(self, id):
        return id // self.m

    def get_col(self, id):
        return id % self.m

    def get_rows_num(self):
        return self.n

    def get_cols_num(self):
        return self.m

    def get_piece(self, row, col):
        if row < 0 or row >= self.n or col < 0 or col >= self.m:
            return None
        return self.pieces[row * self.m + col]

    def create_pieces(self):
        for i in range(self.n * self.m):
            self.pieces[i] = Piece(i, self)
        for piece in self.pieces:
            piece.rotate(random.randint(0, 3))
        random.shuffle(self.pieces)

    def show_pieces(self):
        rows = []
        for i, piece in enumerate(self.pieces):
            if i % self.m == 0:
                rows.append([])
            rows[-1].append(str(piece))
        print('\n'.join(' '.join(map(str, row)) for row in rows))

class Piece:
    def __init__(self, id, puzzle):
        self.id = id
        self.puzzle = puzzle
        self.edges = {}
        self.create_edges()

    def create_edges(self):
        row = self.puzzle.get_row(self.id)
        col = self.puzzle.get_col(self.id)
        last_row = self.puzzle.get_rows_num() - 1
        last_col = self.puzzle.get_cols_num() - 1
        remaining_edge_type = EdgeType.random()

        # create boder edges
        if row == 0:
            self.edges[Orientation.Top] = Edge(EdgeType.Flat)
        if row == last_row:
            self.edges[Orientation.Bottom] = Edge(EdgeType.Flat)
        if col == 0:
            self.edges[Orientation.Left] = Edge(EdgeType.Flat)
        if col == last_col:
            self.edges[Orientation.Right] = Edge(EdgeType.Flat)

        # create edges by existing matched edges
        if row > 0:
            last_piece = self.puzzle.get_piece(row - 1, col)
            if last_piece is not None:
                top_edge = last_piece.get_edge(Orientation.Bottom).create_matched()
                self.edges[Orientation.Top] = top_edge
                # ensure opposite non-flat edge has same type
                if Orientation.Bottom not in self.edges:
                    self.edges[Orientation.Bottom] = Edge(top_edge.type, self.id)
                    remaining_edge_type = top_edge.type.opposite()
        if col > 0:
            last_piece = self.puzzle.get_piece(row, col - 1)
            if last_piece is not None:
                left_edge = last_piece.get_edge(Orientation.Right).create_matched()
                self.edges[Orientation.Left] = left_edge
                # ensure opposite non-flat edge has same type
                if Orientation.Right not in self.edges:
                    self.edges[Orientation.Right] = Edge(left_edge.type, self.id)
                    remaining_edge_type = left_edge.type.opposite()
        # create remaining edges
        if len(self.edges) < len(Orientation):
            for orientation in Orientation:
                if orientation not in self.edges:
                    self.edges[orientation] = Edge(remaining_edge_type, self.id)
                    remaining_edge_type = remaining_edge_type.opposite()

    def fits_in(self, row, col, solution):
        if row == 0 and col == 0:
            for i in range(len(Orientation)):
                if i > 0: self.rotate()
                if self.is_top_left_corner():
                    return True
            return False

        last_row = self.puzzle.get_rows_num() - 1
        last_col = self.puzzle.get_cols_num() - 1
        for i in range(len(Orientation)):
            if i > 0: self.rotate()
            if row - 1 >= 0 and not self.matches_with(solution[row - 1][col], Orientation.Top):
                continue
            if row + 1 <= last_row and not self.matches_with(solution[row + 1][col], Orientation.Bottom):
                continue
            if col - 1 >= 0 and not self.matches_with(solution[row][col - 1], Orientation.Left):
                continue
            if col + 1 <= last_col and not self.matches_with(solution[row][col + 1], Orientation.Right):
                continue
            return True
        return False

    def matches_with(self, other, orientation):
        if other is None: return True
        return self.get_edge(orientation).matches_with(other.get_edge(orientation.opposite()))

    def get_edge(self, orientation):
        return self.edges[orientation]

    def rotate(self, time = 1):
        rotated = {}
        for orientation in Orientation:
            rotated[orientation] = self.edges[orientation.next(time)]
        self.edges = rotated
        return self

    def is_top_left_corner(self):
        return self.edges[Orientation.Top].is_flat() and self.edges[Orientation.Left].is_flat()

    def is_corner(self):
        for orientation in Orientation:
            curr = self.edges[orientation]
            next = self.edges[orientation.next()]
            if curr.is_flat() and next.is_flat():
                return True
        return False

    def is_border(self):        
        for orientation in Orientation:
            if self.edges[orientation].is_flat():
                return True
        return False

    def __str__(self):
        edges = []
        for orientation in Orientation:
             edges.append(str(self.edges[orientation]))
        return f"{self.id:<3}({' '.join(edges)})" 

class Edge:
    def __init__(self, type, code = None):
        self.type = type
        self.code = code

    def create_matched(self):
        return Edge(self.type.opposite(), self.code)
    
    def matches_with(self, other):
        return self.code == other.code and self.type.opposite() is other.type

    def is_flat(self):
        return self.type is EdgeType.Flat

    def __str__(self):
        code = '' if self.code is None else self.code
        return f"{self.type.name[0]}{code:<2}"

n = 3
m = 3
puzzle = Puzzle(n, m)
puzzle.show_pieces()
print('-' * 20 * m)

solution = puzzle.solve()
for row in solution:
    print(*row)
