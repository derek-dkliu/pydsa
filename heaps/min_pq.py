class MinPQ:
    def __init__(self, capacity = 1):
        self.pq = [None] * capacity
        self.n = 0

    def push(self, item):
        if self.n == len(self.pq):
            self._resize(self.n * 2)
        self.pq[self.n] = item
        self.n += 1
        self.swap_up(self.n - 1)

    def pop(self):
        item = self.pq[0]
        self._exch(0, self.n - 1)
        self.n -= 1
        self.swap_down(0)
        self.pq[self.n] = None
        if self.n > 0 and self.n == len(self.pq) // 4:
            self._resize(len(self.pq) // 2)
        return item

    def swap_up(self, i):
        while i > 0:
            j = (i - 1) // 2    # parent
            if self.pq[j] > self.pq[i]:
                self._exch(i, j)
                i = j
            else:
                break

    def swap_down(self, i):
        while i * 2 + 1 < self.n:
            j = i * 2 + 1       # left child
            if j < self.n - 1 and self.pq[j + 1] < self.pq[j]:
                j = j + 1
            if self.pq[i] > self.pq[j]:
                self._exch(i, j)
                i = j
            else:
                break

    def _exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

    def _resize(self, capacity):
        temp = [None] * capacity
        for i in range(self.n):
            temp[i] = self.pq[i]
        self.pq = temp

    def __len__(self):
        return self.n

    @staticmethod
    def heapify(arr):
        size = len(arr)
        start = (size - 1 - 1) // 2     # start from last parent
        for i in range(start, -1, -1):
            MinPQ._sink(arr, i, size)

    @staticmethod
    def sort(arr):
        size = len(arr)
        MinPQ.heapify(arr)
        while size > 1:
            arr[0], arr[size - 1] = arr[size - 1], arr[0]
            size -= 1
            MinPQ._sink(arr, 0, size)
        
    @staticmethod
    def _sink(arr, i, size):
        while i * 2 + 1 < size:
            j = i * 2 + 1
            if j < size - 1 and arr[j + 1] < arr[j]:
                j = j + 1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i = j
            else:
                break


if __name__ == '__main__':
    nums = [6, 2, 9, 8, 3, 1, 7, 4, 5, 0]
    pq = MinPQ(len(nums))
    for num in nums:
        pq.push(num)
    while pq:
        print(pq.pop(), end=' ')
    print()
    print(nums)
    MinPQ.sort(nums)
    print(nums)