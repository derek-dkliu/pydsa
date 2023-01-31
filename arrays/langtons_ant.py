import random
from enum import Enum

class Orientation(Enum):
    Right = 0
    Down = 1
    Left = 2
    Up = 3

    def turn(self, clockwise):
        orientations = list(Orientation)
        index = (self.value + (1 if clockwise else -1)) % len(orientations)
        return orientations[index]
    
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.color = 0 if random.random() < 0.5 else 1
        # next cell based on orientation order: right, down, left, up
        self.direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def flip(self):
        self.color = 1 - self.color

    def iswhite(self):
        return self.color == 0

    def get_loc(self):
        return (self.row, self.col)

    def next_loc(self, orientation):
        r, c = self.direction[orientation.value]
        return (self.row + r, self.col + c)

    def __str__(self):
        return f"({self.row}, {self.col}) {self.color}"

class Ant:
    def __init__(self):
        self.cell = Cell(0, 0)
        self.orientation = Orientation.Right
        self.traces = {}
        self.traces[self.cell.get_loc()] = self.cell
        self.bounds = [0, 0, 0, 0]      # top, bottom, left, right

    def move(self):
        self.turn_orientation()
        print(self.cell, self.orientation.name)
        self.update_cell()

    def turn_orientation(self):
        clockwise = self.cell.iswhite()
        self.orientation = self.orientation.turn(clockwise)

    def update_cell(self):
        self.cell.flip()
        loc = self.cell.next_loc(self.orientation)
        if loc not in self.traces:
            self.traces[loc] = Cell(loc[0], loc[1])
        self.cell = self.traces[loc]
        self.update_bounds(loc)

    def update_bounds(self, loc):
        r, c = loc
        if r < self.bounds[0]:
            self.bounds[0] = r
        elif r > self.bounds[1]:
            self.bounds[1] = r
        if c < self.bounds[2]:
            self.bounds[2] = c
        elif c > self.bounds[3]:
            self.bounds[3] = c

    def print_board(self):
        top, bottom, left, right = self.bounds
        board = []
        for i in range(top, bottom + 1):
            row = []
            for j in range(left, right + 1):
                cell = self.traces.get((i, j), Cell(i, j))
                row.append(str(cell.color))
            board.append(' '.join(row))
        print('\n'.join(board))


def langtons_ant(k):
    ant = Ant()
    for _ in range(k):
        ant.move()
    print(ant.cell)
    ant.print_board()

langtons_ant(6)
