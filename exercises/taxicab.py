import heapq

def taxicab(n):
    pq = []
    for i in range(1, n+1):
        heapq.heappush(pq, Taxicab(i, i))
    ans = []
    count = 1
    prev = Taxicab(0, 0)
    while pq:
        curr = heapq.heappop(pq)
        if curr == prev:
            count += 1
            if count == 2:
                ans.append((prev, curr))
        else:
            if count > 2:
                ans.pop()
            count = 1
        if curr.j < n:
            heapq.heappush(pq, Taxicab(curr.i, curr.j + 1))
        prev = curr
    return ans

class Taxicab:
    def __init__(self, i, j):
        self.sum = i ** 3 + j ** 3
        self.i = i
        self.j = j

    def __eq__(self, other):
        return self.sum == other.sum

    def __lt__(self, other):
        if self.sum == other.sum:
            return self.i < other.i
        else:
            return self.sum < other.sum

    def __gt__(self, other):
        if self.sum == other.sum:
            return self.i > other.i
        else:
            return self.sum > other.sum

    def __str__(self):
        return f"{self.i}^3+{self.j}^3"

if __name__ == '__main__':
    results = taxicab(20)
    for prev, curr in results:
        print(f"{prev.sum} = {prev} = {curr}")