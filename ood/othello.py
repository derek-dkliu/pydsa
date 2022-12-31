from enum import Enum

class Game:
    def __init__(self, n):
        self.board = Board(n, n)
        self.players = [
            Player(Color.Black, self.board),
            Player(Color.White, self.board)
        ]
        self.round = 0

    def run(self, verbose = False):
        while not self.finished():
            self.get_player().move()
            self.round += 1
            if verbose:
                print(self)
        return self.board.get_winner()

    def finished(self):
        return self.board.finished(self.get_player().color)

    def get_player(self):
        return self.players[self.round % 2]

    def __str__(self):
        return f"{self.board}\nround={self.round}, score={self.board.get_score()}, next={self.get_player()}\n"

class Player:
    def __init__(self, color, board):
        self.color = color
        self.board = board

    def move(self):
        loc, pieces = self.get_greedy_move()
        if loc is None: return False
        # place a piece and flip peices
        row, col = loc
        self.board.place_piece(row, col, self.color)
        self.board.flip_pieces(pieces)
        return True

    # greedy strategy: choose a move which captures the most pieces at each turn
    def get_greedy_move(self):
        best_loc = None
        best_pieces = []
        for i in range(self.board.get_rows()): 
            for j in range(self.board.get_cols()):
                if self.board.is_taken(i, j): continue
                pieces = self.board.capture(i, j, self.color)
                if len(pieces) > len(best_pieces):
                    best_pieces = pieces
                    best_loc = (i, j)
        return best_loc, best_pieces

    def __str__(self):
        return self.color.name

class Board:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.board = [[None] * m for _ in range(n)]
        # setup board with 4 pieces in the center
        row = (n-1) // 2
        col = (m-1) // 2
        self.board[row][col] = Piece(Color.Black)
        self.board[row][col+1] = Piece(Color.White)
        self.board[row+1][col] = Piece(Color.White)
        self.board[row+1][col+1] = Piece(Color.Black)
        # init piece count for black and white
        self.black_count = 2
        self.white_count = 2

    def finished(self, color):
        for i in range(self.n):
            for j in range(self.m):
                if self.is_taken(i, j): continue
                elif self.capture(i, j, color):
                    return False
        return True
    
    def get_winner(self):
        if self.black_count > self.white_count:
            return Color.Black.name
        elif self.black_count < self.white_count:
            return Color.White.name
        else:
            return None

    def flip_pieces(self, pieces):
        total = len(pieces)
        if total > 0:
            # update piece counts
            if pieces[0].isblack():
                self.black_count -= total
                self.white_count += total
            else:
                self.black_count += total
                self.white_count -= total
        # flip pieces
        for piece in pieces:
            piece.flip()

    def place_piece(self, row, col, color):
        piece = Piece(color)
        self.board[row][col] = piece
        # increase piece count by one
        if piece.isblack():
            self.black_count += 1
        else:
            self.white_count += 1

    def capture(self, row, col, color):
        if not self.is_loc_valid(row, col):
            raise Exception(f"Location ({row},{col}) out of index")
        if self.is_taken(row, col):
            raise Exception(f"Location ({row},{col}) has a piece already")

        # A move is valid if it can capture at least one opponent's pieces in any one of eight directions
        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        pieces = []
        for direction in directions:
            pieces.extend(self.check_pieces_in_direction(row, col, color, direction))
        return pieces

    def check_pieces_in_direction(self, row, col, color, direction):
        pieces = []
        row += direction[0]
        col += direction[1]
        while self.is_loc_valid(row, col) and self.is_taken(row, col) \
              and not self.board[row][col].iscolor(color):
            pieces.append(self.board[row][col])
            row += direction[0]
            col += direction[1]
        if self.is_loc_valid(row, col) and self.is_taken(row, col):
            return pieces
        else:
            return []

    def is_taken(self, row, col):
        return self.board[row][col] is not None

    def is_loc_valid(self, row, col):
        return row >= 0 and row < self.n and col >= 0 and col < self.m

    def get_rows(self):
        return self.n
    
    def get_cols(self):
        return self.m

    def get_score(self):
        return self.black_count, self.white_count 

    def __str__(self):
        rows = []
        for row in self.board:
            rows.append('|'.join(map(lambda x: str(x) if x else ' ', row)))
        return '\n'.join(rows)

class Piece:
    def __init__(self, color):
        self.color = color

    def iscolor(self, color):
        return self.color is color

    def isblack(self):
        return self.color is Color.Black

    def flip(self):
        self.color = self.color.flip()

    def __str__(self):
        return '●' if self.isblack() else '○'

class Color(Enum):
    Black = True
    White = False

    def flip(self):
        return Color.White if self.value else Color.Black

game = Game(6)
print(game)
winner = game.run(True)
print(f"{winner} wins" if winner else "TIE") 
