"""
distinct values
"""
def magic_index(A):
    low = 0
    high = len(A) - 1    
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == mid:
            return mid
        elif A[mid] < mid:
            low = low + 1
        else:
            high = high - 1
    return -1

"""
not distinct values
"""
def magic_index2(A):
    return search(A, 0, len(A) - 1)

def search(A, low, high):
    if low > high: return -1
    mid = (low + high) // 2
    if A[mid] == mid:
        return mid

    index = search(A, low, min(mid - 1, A[mid]))
    if index >= 0: return index
    return search(A, max(mid + 1, A[mid]), high)

A = [-1,0,1,2,3,5,6,7]
print(magic_index(A))

A = [-1,0,2,2,3,6,7,8]
print(magic_index2(A))