# time:  O(k^2)
# space: O(k^2)
def diving_board(k, shorter, longer):
    result = set()
    memo = set()
    place(k, shorter, longer, 0, result, memo)
    return result

def place(k, shorter, longer, curr, result, memo):
    if k == 0:
        result.add(curr)
        return
    if (k, curr) in memo: return

    place(k - 1, shorter, longer, curr + shorter, result, memo)
    place(k - 1, shorter, longer, curr + longer, result, memo)
    memo.add((k, curr))

# time:  O(k)
# space: O(k)
def diving_board2(k, shorter, longer):
    if shorter == longer:
        return [k * shorter]
    result = []
    for i in range(k + 1):
        result.append(shorter * i + longer * (k - i))
    return result


print(diving_board(5, 1, 2))
print(diving_board(6, 1, 2))
print(diving_board(6, 2, 5))

print(diving_board2(5, 1, 2))
print(diving_board2(6, 1, 2))
print(diving_board2(6, 2, 5))
