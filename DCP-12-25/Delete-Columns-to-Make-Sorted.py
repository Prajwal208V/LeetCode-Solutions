1from typing import List
2
3class Solution:
4    def minDeletionSize(self, strs: List[str]) -> int:
5        count = 0
6        rows = len(strs)
7        cols = len(strs[0])
8
9        for c in range(cols):
10            for r in range(1, rows):
11                if strs[r][c] < strs[r - 1][c]:
12                    count += 1
13                    break
14        return count