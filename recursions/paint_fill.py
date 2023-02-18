def paint_fill(screen, row, col, color):
    rows = len(screen)
    cols = len(screen[0])
    if row < 0 or row >= rows or col < 0 or col >= cols:
        raise Exception('Invalid row or col input')
    target = screen[row][col]
    if target == color:
        return
    dfs(screen, row, col, color, target)

def dfs(screen, row, col, color, target):
    screen[row][col] = color
    rows = len(screen)
    cols = len(screen[0])
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for d in directions:
        r = row + d[0]
        c = col + d[1]
        if r >= 0 and r < rows and c >= 0 and c < cols and screen[r][c] == target:
            dfs(screen, r, c, color, target)

# same method but a bit more concise
def paint_fill2(A, i, j, t):
    c = A[i][j]
    fill(A, i, j, c, t)

def fill(A, i, j, c, t):
    rows = len(A)
    cols = len(A[0])
    if i < 0 or i >= rows or j < 0 or j >= cols or A[i][j] != c: return

    A[i][j] = t
    fill(A, i+1, j, c, t)
    fill(A, i-1, j, c, t)
    fill(A, i, j+1, c, t)
    fill(A, i, j-1, c, t)
    # fill(A, i+1, j+1, c, t)
    # fill(A, i+1, j-1, c, t)
    # fill(A, i-1, j+1, c, t)
    # fill(A, i-1, j-1, c, t)

screen = [
    [0,1,2,1,0,0],
    [0,0,1,1,0,0],
    [1,1,2,1,0,0],
    [0,1,2,1,1,0],
    [0,1,2,1,1,0],
]
# paint_fill(screen, 1, 3, 3)
paint_fill2(screen, 1, 3, 3)

for row in screen:
    print(*row)




