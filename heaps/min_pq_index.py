class IndexMinPQ:
    def __init__(self, capacity):
        self.pq = [None] * capacity     # heap position to index
        self.qp = [None] * capacity     # index to heap position
        self.keys = [None] * capacity   # key by index
        self.n = 0

    def push(self, i, item):
        self.pq[self.n] = i
        self.qp[i] = self.n
        self.keys[i] = item
        self.n += 1
        self.swap_up(self.n - 1)

    def pop(self):
        i = self.pq[0]
        self._exch(0, self.n - 1)
        self.n -= 1
        self.swap_down(0)
        self.pq[self.n] = None
        self.qp[i] = None
        self.keys[i] = None
        return i

    def delete(self, i):
        p = self.qp[i]
        self._exch(p, self.n - 1)
        self.n -= 1
        self.swap_down(p)
        self.pq[self.n] = None
        self.qp[i] = None
        self.keys[i] = None

    def contains(self, i):
        return self.qp[i] != None

    def min(self):
        return self.pq[0]

    def min_key(self):
        return self.keys[self.pq[0]]

    def get_key(self, i):
        if not self.contains(i):
            raise Exception("index is not in the priority queue")
        else: return self.keys[i]

    def decrease_key(self, i, key):
        if not self.contains(i):
            raise Exception("index is not in the priority queue")
        if not self.keys[i] > key:
            raise Exception("key should be less than the existing key")
        self.keys[i] = key
        self.swap_up(self.qp[i])

    def increase_key(self, i, key):
        if not self.contains(i):
            raise Exception("index is not in the priority queue")
        if not self.keys[i] < key:
            raise Exception("key should be greater than the existing key")
        self.keys[i] = key
        self.swap_down(self.qp[i])

    def change_key(self, i, key):
        if not self.contains(i):
            raise Exception("index is not in the priority queue")
        self.keys[i] = key
        self.swap_up(self.qp[i])
        self.swap_down(self.qp[i])

    def swap_up(self, i):
        while i > 0:
            j = (i - 1) // 2    # parent
            if self.keys[self.pq[j]] > self.keys[self.pq[i]]:
                self._exch(i, j)
                i = j
            else:
                break
    
    def swap_down(self, i):
        while i * 2 + 1 < self.n:
            j = i * 2 + 1       # left child
            if j < self.n - 1 and self.keys[self.pq[j+1]] < self.keys[self.pq[j]]:
                j = j + 1
            if self.keys[self.pq[i]] > self.keys[self.pq[j]]:
                self._exch(i, j)
                i = j
            else:
                break

    def _exch(self, i, j):
        m = self.pq[i]
        n = self.pq[j]
        self.qp[m], self.qp[n] = self.qp[n], self.qp[m]
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def __len__(self):
        return self.n


if __name__ == '__main__':
    nums = [6, 2, 9, 8, 3, 1, 7, 4, 5, 0]
    pq = IndexMinPQ(len(nums))
    for i, num in enumerate(nums):
        pq.push(i, num)
    while pq:
        print(nums[pq.pop()], end=' ')
    print()
