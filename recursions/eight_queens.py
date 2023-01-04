def queens(n):
    result = []
    cols = [0] * n
    diag1 = [0] * (n * 2 - 1)
    diag2 = [0] * (n * 2 - 1)
    place_by_row(n, 0, cols, diag1, diag2, [], result)
    # print("\n\n".join(result))
    print(n, len(result))

def place_by_row(n, r, cols, diag1, diag2, curr, result):
    if r == n:
        result.append(build_arrangment(curr))
        return

    for c in range(n):
        d1 = r - c + n - 1
        d2 = r + c
        if cols[c] or diag1[d1] or diag2[d2]: continue
        cols[c] += 1
        diag1[d1] += 1
        diag2[d2] += 1
        curr.append(c)
        place_by_row(n, r + 1, cols, diag1, diag2, curr, result)
        curr.pop()
        cols[c] -= 1
        diag1[d1] -= 1
        diag2[d2] -= 1

def build_arrangment(curr):
    arrangment = []
    for i in curr:
        line = ['-'] * len(curr)
        line[i] = '*'
        arrangment.append(' '.join(line))
    return '\n'.join(arrangment)

def queens2(n):
    result = []
    q = [None] * n
    place_by_row2(0, n, q, result)
    # print("\n\n".join(result))
    print(n, len(result))

def place_by_row2(r, n, q, result):
    if r == n:
        result.append(build_arrangment(q))
        return
    for c in range(n):
        if is_valid(q, r, c):
            q[r] = c
            place_by_row2(r + 1, n, q, result)

def is_valid(q, r, c):
    for i in range(r):
        if c == q[i]: return False
        # if distance between colums equals distance between rows,
        # they are in the same diagonals
        if abs(q[i] - c) == r - i: return False
    return True

# queens(1)
# queens(2)
# queens(3)
queens(8)
queens2(8)