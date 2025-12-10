1from typing import List
2
3class Solution:
4    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
5        n = len(arr)
6        ans = 0
7        for i in range(n):
8            for j in range(i + 1, n):
9                if abs(arr[i] - arr[j]) <= a:
10                    for k in range(j + 1, n):
11                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
12                            ans += 1
13        return ans    