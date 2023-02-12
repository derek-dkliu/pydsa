"""Inplace rotate matrix"""
def rotate_matrix1(matrix):
    n = len(matrix)
    for i in range((n - 1) // 2 + 1):
        for j in range(i, n-1-i):
            temp = matrix[i][j]
            r = i
            c = j 
            while True:
                row = n - 1 - c
                col = r
                if (row == i and col == j):
                    matrix[r][c] = temp
                    break
                else:
                    matrix[r][c] = matrix[row][col]
                    r = row
                    c = col
    return matrix

import math
def rotate_matrix2(matrix):
    n = len(matrix)
    for i in range(math.ceil(n / 2)):
        first = i
        last = n - 1 - i
        for j in range(first, last):
            offset = j - first
            # top -> temp
            temp = matrix[first][j]
            # left -> top
            matrix[first][j] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[j][last]
            # temp -> right
            matrix[j][last] = temp
    return matrix

# rotate 90 clockwise = transpose + horizontal flip
def rotate_matrix3(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        for j in range(math.ceil(n / 2)):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
    return matrix

# same as above in a more pythonic way but not inplace
def rotate_matrix4(matrix):
    return [list(reversed(row)) for row in zip(*matrix)]

from matrix import Matrix
cases = [
    Matrix.create(0),
    Matrix.create(1),
    Matrix.create(2),
    Matrix.create(3),
    Matrix.create(4)
]
for i, matrix in enumerate(cases):
    print(f"Case {i+1}:")
    print(Matrix.format(matrix))
    print('-' * 4 * len(matrix))
    print(Matrix.format(rotate_matrix2(matrix)))
