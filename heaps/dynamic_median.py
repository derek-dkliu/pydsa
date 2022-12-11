import heapq
class DynamicMedian:
    """O(log(N) for each push operation"""

    def __init__(self):
        self.minpq = []
        self.maxpq = []

    def push(self, num):
        """Push num and return median.
        maxpq to keep smaller half
        minpq to keep bigger half
        keep len(minpq) - len(maxpq) <= 1
        if equal, return average of top of both pq
        otherwise, return top of minpq
        """
        # since built-in heapq is actually a min priority queue,
        # to use minpq as the max priority queue, negate the num when
        # push into maxpq, and negate back when pop up from the maxpq

        # the following three operations ensure maxpq keep the smaller half,
        # while minpq keep the bigger half.
        heapq.heappush(self.maxpq, -num)
        max = -heapq.heappop(self.maxpq)
        heapq.heappush(self.minpq, max)

        # after above operations, the size of minpq always increases by one,
        # to rebalance both pq, pop out num from minpq and push it into maxpq
        # if minpq has more than one num than maxpq.
        if len(self.minpq) - len(self.maxpq) > 1:
            min = heapq.heappop(self.minpq)
            heapq.heappush(self.maxpq, -min)

        if len(self.minpq) == len(self.maxpq):
            return (self.minpq[0] + -self.maxpq[0]) / 2
        else:
            return self.minpq[0]

if __name__ == '__main__':
    cases = [
        [3,2,1,9,4,8,5],        # odd size
        [-12,9,-6,8,6,-2,0],    # even size with negative
        [1,2,3,4,5,6],          # ascending order
        [6,5,4,3,2,1]           # descending order
    ]
    for i, case in enumerate(cases):
        dm = DynamicMedian()
        print(f"{'case'.upper()} {i+1}: {case}")
        for num in case:
            print(f"push {num}, median is {dm.push(num)}")
        print()