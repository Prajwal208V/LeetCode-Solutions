1import heapq
2from typing import List
3
4class Solution:
5    def maxTwoEvents(self, events: List[List[int]]) -> int:
6        events.sort()
7        heap = []
8        max_val = 0
9        res = 0
10
11        for start, end, value in events:
12            while heap and heap[0][0] < start:
13                _, v = heapq.heappop(heap)
14                max_val = max(max_val, v)
15
16            res = max(res, max_val + value)
17            heapq.heappush(heap, (end, value))
18
19        return res