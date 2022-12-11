"""space: O(n)"""
def zero_matrix1(matrix):
    if len(matrix) == 0: return matrix
    m = len(matrix)
    n = len(matrix[0])
    rows = [False] * m
    cols = [False] * n
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(m):
        for j in range(n):
            if rows[i] or cols[j]:
                matrix[i][j] = 0
    return matrix

"""space: O(1)"""
def zero_matrix2(matrix):
    if len(matrix) == 0: return matrix
    m = len(matrix)
    n = len(matrix[0])
    row_zero = False
    col_zero = False
    for j in range(n):
        if matrix[0][j] == 0:
            row_zero = True
            break
    for i in range(m):
        if matrix[i][0] == 0:
            col_zero = True
            break
    # use first row to store cols to be zeroed out
    # use first col to store rows to be zeroed out
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    if row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if col_zero:
        for i in range(m):
            matrix[i][0] = 0
    return matrix


from matrix import Matrix
cases = [
    Matrix.zero(0, 0.3),
    Matrix.zero(1, 0.3),
    Matrix.zero(2, 0.3),
    Matrix.zero(3, 0.3),
    Matrix.zero(4, 0.3)
]
for i, matrix in enumerate(cases):
    print(f"Case {i+1}:")
    print(Matrix.format(matrix))
    print('-' * 4 * len(matrix))
    print(Matrix.format(zero_matrix2(matrix)))