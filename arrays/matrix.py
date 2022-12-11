import random

class Matrix:
    @staticmethod
    def create(n):
        return [[i*n + j + 1 for j in range(n)] for i in range(n)]

    @staticmethod
    def format(matrix):
        return '\n'.join(str(row) for row in matrix)

    @staticmethod
    def zero(n, prob=1):
        return [[0 if random.random() < prob else i*n + j + 1 for j in range(n)] for i in range(n)]