import random, math

class Matrix:
    @staticmethod
    def create(n, m):
        return [[i*m + j + 1 for j in range(m)] for i in range(n)]

    @staticmethod
    def square(n):
        return [[i*n + j + 1 for j in range(n)] for i in range(n)]

    @staticmethod
    def zero(n, prob=1):
        return [[0 if random.random() < prob else i*n + j + 1 for j in range(n)] for i in range(n)]

    @staticmethod
    def format(matrix):
        return '\n'.join(' '.join(f"{i:2}" for i in row) for row in matrix) + '\n'

    @staticmethod
    def clone(matrix):
        n = len(matrix)
        m = len(matrix[0])
        copy = [[None] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                copy[i][j] = matrix[i][j]
        return copy

    @staticmethod
    def transpose(matrix):
        n = len(matrix)
        m = len(matrix[0])
        if n != m:
            raise Exception('Not a square matrix')
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    @staticmethod
    def hflip(matrix):
        n = len(matrix)
        m = len(matrix[0])
        half_cols = math.ceil((m - 1) / 2)
        for i in range(n):
            for j in range(half_cols):
                matrix[i][j], matrix[i][m-1-j] = matrix[i][m-1-j], matrix[i][j]


if __name__ == '__main__':
    m = Matrix.square(5)
    print(Matrix.format(m))
    Matrix.transpose(m)
    print(Matrix.format(m))
    Matrix.hflip(m)
    print(Matrix.format(m))

    m = Matrix.square(5)
    print(Matrix.format(m))
    Matrix.hflip(m)
    print(Matrix.format(m))
    Matrix.transpose(m)
    print(Matrix.format(m))
