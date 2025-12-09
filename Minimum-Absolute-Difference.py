1from typing import List
2
3class Solution:
4    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
5        arr.sort()
6        diff = float('inf')
7        for i in range(1, len(arr)):
8            diff = min(diff, arr[i] - arr[i - 1])
9        res = []
10        for i in range(1, len(arr)):
11            if arr[i] - arr[i - 1] == diff:
12                res.append([arr[i - 1], arr[i]])
13        return res
14