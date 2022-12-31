from enum import Enum
import random

class Game:
    def __init__(self, n, b):
        self.board = Board(n, n, b)

    def run(self):
        self.welcome()
        bombed = False
        while not self.board.finished():
            row, col, marked = self.prompt()
            try:
                if marked:
                    self.board.mark_cell(row, col)
                    print(self)
                else:
                    bombed = self.board.uncover_cell(row, col)
                    print(self)
                    if bombed: break
            except Exception as e:
                print(e)
                continue
        if bombed:
            print("You lost 😵")
        else:
            print("You win 😎")

    def prompt(self):
        mark = ''
        token = input("\nSelect a cell: ").lower()
        if ':' in token:
            mark, token = token.split(':')
        loc = token.split(',')
        if len(loc) != 2 or loc[0] == '' or loc[1] == '' or (mark != '' and mark != 'm'):
            print("Invalid Input.\n1. Uncover a cell in format x,y\n2. Mark or unmark a cell in format m:x,y")
            return self.prompt()
        row, col = map(int, loc)
        return row-1, col-1, mark == 'm'

    def welcome(self):
        title =  "***********************************\n"
        title += "*     Welcome to Mine Sweeper     *\n"
        title += "***********************************"
        n = self.board.get_rows()
        m = self.board.get_cols()
        hint = "* HOW TO PLAY\n"
        hint += f"1. Uncover a cell, e.g. top-left cell, by its location 1,1\n"
        hint += f"2. Mark as a bomb, e.g. bottom-right cell, with a command m:{n},{m}"
        print(f"{title}\n\n{self}\n\n{hint}")

    def __str__(self):
        return str(self.board)

class Board:
    def __init__(self, n, m, b):
        self.n = n
        self.m = m
        self.b = b
        if b >= n * m:
            raise Exception("The number of bombs should be less than the number of cells")
        self.board = [[Cell(i, j) for j in range(m)] for i in range(n)]
        self.init_bomb_cells()
        self.init_number_cells()
        
    def init_bomb_cells(self):
        # set first b cells as bomb cells
        for i in range(self.b):
            self.board[i // self.m][i % self.m].set_bomb()
        # shuffle all cells of the board
        total = self.n * self.m
        for i in range(total):
            j = random.randint(i, total - 1)
            r1, c1 = i // self.m, i % self.m
            r2, c2 = j // self.m, j % self.m
            self.board[r1][c1], self.board[r2][c2] = self.board[r2][c2], self.board[r1][c1]
                
    def init_number_cells(self):
        for i in range(self.n):
            for j in range(self.m):
                cell = self.board[i][j]
                if cell.is_bomb(): continue
                bomb_count = 0
                for neighbour in self.neighbours(i, j):
                    if neighbour.is_bomb():
                        bomb_count += 1
                if bomb_count > 0:
                    cell.set_number(bomb_count)

    def finished(self):
        for i in range(self.n):
            for j in range(self.m):
                cell = self.board[i][j]
                if cell.is_covered() and not cell.is_bomb():
                    return False
        return True

    def mark_cell(self, row, col):
        if not self.is_valid(row, col):
            raise Exception(f"Location {row+1},{col+1} is out of bounds of the board!")
        cell = self.board[row][col]
        if not cell.is_covered():
            raise Exception(f"Cell {row+1},{col+1} was uncovered already.")
        cell.flag()
            

    def uncover_cell(self, row, col):
        if not self.is_valid(row, col):
            raise Exception(f"Location {row+1},{col+1} is out of bounds of the board!")
        cell = self.board[row][col]
        if not cell.is_covered():
            raise Exception(f"Cell {row+1},{col+1} was uncovered already.")
        elif cell.is_flagged():
            raise Exception(f"Cannot uncover cell {row+1},{col+1}. Please unmarked it first with m:{row+1},{col+1}.")
        elif cell.is_bomb():
            cell.uncover()
            return True
        else:
            cell.uncover()
            if cell.is_blank():
                self.expand_cell(row, col)
            return False

    def expand_cell(self, row, col):
        for neighbour in self.neighbours(row, col):
            if neighbour.is_covered() and not neighbour.is_bomb():
                neighbour.uncover()
                if neighbour.is_blank():
                    self.expand_cell(neighbour.row, neighbour.col)

    def neighbours(self, row, col):
        cells = []
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for d in directions:
            r = row + d[0]
            c = col + d[1]
            if self.is_valid(r, c):
                cells.append(self.board[r][c])
        return cells

    def is_valid(self, row, col):
        return row >= 0 and row < self.n and col >= 0 and col < self.m

    def get_rows(self):
        return self.n
    
    def get_cols(self):
        return self.m

    def __str__(self):
        rows = []
        for row in self.board:
            rows.append('|'.join(map(str, row)))
        return '\n'.join(rows)

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.type = CellType.Blank
        self.value = None
        self.covered = True
        self.flagged = False
    
    def set_bomb(self):
        self.type = CellType.Bomb

    def set_number(self, value):
        self.value = value
        self.type = CellType.Number

    def uncover(self):
        self.covered = False

    def flag(self):
        if self.is_covered():
            self.flagged = not self.flagged
            return True
        return False

    def is_covered(self):
        return self.covered

    def is_flagged(self):
        return self.flagged

    def is_blank(self):
        return self.type is CellType.Blank

    def is_bomb(self):
        return self.type is CellType.Bomb

    def is_number(self):
        return self.type is CellType.Number

    def __str__(self):
        if self.is_covered():
            return ' *' if self.is_flagged() else ' ?'
        elif self.is_blank():
            return '  '
        elif self.is_bomb():
            return '💣'
        else:
            return f"{self.value:2}"

class CellType(Enum):
    Blank = 0
    Bomb = 1
    Number = 2

Game(6, 4).run()
