import random
from collections import deque

# time:  O(n*m)
# space: O(n+m)
def robot_grid(grid):
    path = deque()
    dfs(grid, 0, 0, path, {})
    return list(path)

def dfs(grid, row, col, path, memo):
    rowmax = len(grid) - 1
    colmax = len(grid[0]) - 1
    if row > rowmax or col > colmax or grid[row][col] == 0:
        return False

    if (row, col) in memo: return memo[(row, col)]

    ans = False
    if (row == rowmax and col == colmax) or \
        dfs(grid, row + 1, col, path, memo) or \
        dfs(grid, row, col + 1, path, memo):
        path.appendleft((row, col))
        ans = True
    memo[(row, col)] = ans
    return ans

# time:  O(n*m)
# space: O(n*m)
def robot_grid2(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if grid[i][j] == 0: 
                dp[i][j] = False
            elif i == n - 1 and j == m - 1:
                dp[i][j] = True
            else:
                dp[i][j] = dp[i+1][j] or dp[i][j+1]

    # find out the path
    if not dp[0][0]: return []
    path = [(0, 0)]
    row, col = 0, 0
    while True:
        if row + 1 < n and dp[row + 1][col]:
            row += 1
            path.append((row, col))
        elif col + 1 < m and dp[row][col + 1]:
            col += 1
            path.append((row, col))
        else:
            break
        if row == n - 1 and col == m - 1:
            break
    return path

# time:  O(n*m)
# space: O(m)
def robot_grid3(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [False] * (m + 1)
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if grid[i][j] == 0:
                dp[j] = False
            elif i == n - 1 and j == m - 1: 
                dp[j] = True
            elif i == n - 1: 
                dp[j] = dp[j + 1]
            else: 
                dp[j] = dp[j] or dp[j + 1]
    return dp[0]

def init_grid(n, m, b):
    return [[0 if i * m + j < b and i * m + j > 0 else 1 for j in range(m)] for i in range(n)]

def shuffle_grid(grid, from_cell, to_cell):
    m = len(grid[0])
    for i in range(from_cell, to_cell):
        t = random.randint(i, to_cell)
        r1, c1 = i // m, i % m
        r2, c2 = t // m, t % m
        grid[r1][c1], grid[r2][c2] = grid[r2][c2], grid[r1][c1]

def print_grid(grid):
    for row in grid:
        print(*row)

# random.seed(1)
n = 5
m = 5
b = 5
grid = init_grid(n, m, b)
shuffle_grid(grid, 1, n * m - 2)
print_grid(grid)

print(robot_grid(grid))
print(robot_grid2(grid))
print(robot_grid3(grid))