# start from top right corner
# time:  O(n + m)
# space: O(1)
def sorted_matrix_search1(matrix, x):
    m = len(matrix)
    n = len(matrix[0])
    row = 0
    col = n - 1
    while row < m and col >= 0:
        if x == matrix[row][col]:
            return (row, col)
        elif x > matrix[row][col]:
            row += 1
        else:
            col -= 1
    return None

# start from bottom left corner
# time:  O(n + m)
# space: O(1)
def sorted_matrix_search2(matrix, x):
    m = len(matrix)
    n = len(matrix[0])
    row = m - 1
    col = 0
    while row >= 0 and col < n:
        if x == matrix[row][col]:
            return (row, col)
        elif x > matrix[row][col]:
            col += 1
        else:
            row -= 1
    return None

# quarter search
def sorted_matrix_search3(matrix, x):
    m = len(matrix)
    n = len(matrix[0])
    return search(matrix, x, 0, m - 1, 0, n - 1)

def search(matrix, x, minrow, maxrow, mincol, maxcol):
    if minrow > maxrow or mincol > maxcol:
        return None
    row = (minrow + maxrow) // 2
    col = (mincol + maxcol) // 2

    if x == matrix[row][col]:
        return (row, col)
    elif x < matrix[row][col]:
        res1 = search(matrix, x, minrow, row - 1, mincol, col - 1)
        if res1 is not None: return res1
        res2 = search(matrix, x, minrow, row - 1, col, maxcol)
        if res2 is not None: return res2
        return search(matrix, x, row, maxrow, mincol, col - 1)
    else:
        res1 = search(matrix, x, row + 1, maxrow, col + 1, maxcol)
        if res1 is not None: return res1
        res2 = search(matrix, x, row + 1, maxrow, mincol, col)
        if res2 is not None: return res2
        return search(matrix, x, minrow, row, col + 1, maxcol)

# nested binary search
# time: O(log(m*n) * log(m+n)) at most
def sorted_matrix_search4(matrix, x):
    m = len(matrix)
    n = len(matrix[0])
    return search(matrix, x, 0, m - 1, 0, n - 1)

def search(matrix, x, minrow, maxrow, mincol, maxcol):
    if minrow > maxrow or mincol > maxcol:
        return None

    # do binary search along the diagonal
    row, col = minrow, mincol
    # find diagonal end since the matrix may not be square
    dist = min(maxrow - minrow, maxcol - mincol) 
    endrow = minrow + dist
    endcol = mincol + dist
    while row <= endrow and col <= endcol:
        midrow = (row + endrow) // 2
        midcol = (col + endcol) // 2
        if x == matrix[midrow][midcol]:
            return (midrow, midcol)
        elif x < matrix[midrow][midcol]:
            endrow = midrow - 1
            endcol = midcol - 1
        else:
            row = midrow + 1
            col = midcol + 1

    # if not found, search lower left and upper right quadrants
    loc = search(matrix, x, row, maxrow, mincol, col - 1)
    if loc is not None: return loc
    return search(matrix, x, minrow, row - 1, col, maxcol)

matrix = [
    [15, 20, 40, 85],
    [20, 35, 80, 95],
    [30, 55, 95, 105],
    [40, 80, 100, 120]
]
print(sorted_matrix_search1(matrix, 80))
print(sorted_matrix_search2(matrix, 80))
print(sorted_matrix_search3(matrix, 80))
print(sorted_matrix_search4(matrix, 80))
