1from typing import List
2
3class Solution:
4    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
5        if not intervals:
6            return 0
7
8        intervals.sort(key=lambda x: x[1])
9        count = 0
10        prev_end = intervals[0][1]
11
12        for i in range(1, len(intervals)):
13            if intervals[i][0] < prev_end:
14                count += 1
15            else:
16                prev_end = intervals[i][1]
17
18        return count