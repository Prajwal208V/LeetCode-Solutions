1class Solution:
2    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
3        n = len(intervals)
4        starts = sorted((intervals[i][0], i) for i in range(n))
5        res = [-1] * n
6
7        import bisect
8        for i in range(n):
9            end = intervals[i][1]
10            idx = bisect.bisect_left(starts, (end,))
11            if idx < n:
12                res[i] = starts[idx][1]
13
14        return res