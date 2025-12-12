1import heapq
2
3class MedianFinder:
4    def __init__(self):
5        self.small = []  # max-heap (invert values for min-heap)
6        self.large = []  # min-heap
7
8    def addNum(self, num: int) -> None:
9        heapq.heappush(self.small, -num)
10        heapq.heappush(self.large, -heapq.heappop(self.small))
11        if len(self.large) > len(self.small):
12            heapq.heappush(self.small, -heapq.heappop(self.large))
13
14    def findMedian(self) -> float:
15        if len(self.small) > len(self.large):
16            return -self.small[0]
17        else:
18            return (-self.small[0] + self.large[0]) / 2