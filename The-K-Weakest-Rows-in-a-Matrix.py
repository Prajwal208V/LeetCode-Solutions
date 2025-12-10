1from typing import List
2
3class Solution:
4    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
5        strength = []
6        for i, row in enumerate(mat):
7            lo, hi = 0, len(row)
8            while lo < hi:
9                mid = (lo + hi) // 2
10                if row[mid] == 1:
11                    lo = mid + 1
12                else:
13                    hi = mid
14            strength.append((lo, i))
15        strength.sort()
16        return [idx for _, idx in strength[:k]]
17