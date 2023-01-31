def pond_sizes(land):
    m = len(land)
    n = len(land[0])
    ans = []
    for i in range(m):
        for j in range(n):
            if land[i][j] == 0:
                ans.append(dfs(land, i, j))    
    return ans

def dfs(land, i, j):
    m = len(land)
    n = len(land[0])
    if i < 0 or i >= m or j < 0 or j >= n or land[i][j] != 0:
        return 0
    size = 1
    land[i][j] = -1
    dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for dir in dirs:
        r = i + dir[0]
        c = j + dir[1]
        size += dfs(land, r, c)
    return size

land = [
    [0, 2, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1]
]
print(pond_sizes(land))
