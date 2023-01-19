import heapq

def merge(arrs):
    pq = []
    for arr in arrs:
        heapq.heappush(pq, (arr[0], arr, 0))

    ans = []
    while pq:
        (item, arr, i) = heapq.heappop(pq)
        ans.append(item)
        i += 1
        if i < len(arr):
            heapq.heappush(pq, (arr[i], arr, i))
    return ans

arrs = [
    [4, 6, 9, 16], [2, 10, 11, 13], [5, 8, 14, 15], [1, 3, 7, 12]
]
print(merge(arrs))


