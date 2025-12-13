1from typing import List
2
3class Solution:
4    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
5        n = len(matrix)
6        lo, hi = matrix[0][0], matrix[-1][-1]
7
8        def count_le(x: int) -> int:
9            cnt = 0
10            r, c = n - 1, 0
11            while r >= 0 and c < n:
12                if matrix[r][c] <= x:
13                    cnt += r + 1
14                    c += 1
15                else:
16                    r -= 1
17            return cnt
18
19        while lo < hi:
20            mid = (lo + hi) // 2
21            if count_le(mid) < k:
22                lo = mid + 1
23            else:
24                hi = mid
25
26        return lo