import random

class TicTacToe:
    def __init__(self, n):
        self.board = [[0] * n for _ in range(n)]
        self.rows = n
        self.cols = n
        self.random()

    def random(self):
        for i in range(self.rows):
            for j in range(self.cols):
                val = random.random()
                if val < .33:
                    self.board[i][j] = 1
                elif val < .66:
                    self.board[i][j] = 2

    def check_win(self):
        # check rows
        for i in range(self.rows):
            res = self.check_row(i)
            if res: return res
        for j in range(self.cols):
            res = self.check_col(j)
            if res: return res
        res = self.check_diag(True)
        if res: return res
        res = self.check_diag(False)
        if res: return res
        return False

    def check_row(self, row):
        first = self.board[row][0]
        if not first:
            return False
        for j in range(1, self.cols):
            if self.board[row][j] != first:
                return False
        return (True, first)

    def check_col(self, col):
        first = self.board[0][col]
        if not first:
            return False
        for i in range(1, self.rows):
            if self.board[i][col] != first:
                return False
        return (True, first)

    def check_diag(self, major):
        row, col = (0, 0) if major else (0, self.cols - 1)
        dr, dc = (1, 1) if major else (1, -1)
        first = self.board[row][col]
        if not first:
            return False
        for i in range(1, self.rows):
            r = row + dr * i
            c = col + dc * i
            if self.board[r][c] != first:
                return False
        return (True, first)
    
    def __str__(self):
        sb = []
        for row in self.board:
            sb.append(' '.join(map(lambda x: str(x) if x else '-', row)))
        return '\n'.join(sb)

tictactoe = TicTacToe(3)
print(tictactoe)
print(tictactoe.check_win())
