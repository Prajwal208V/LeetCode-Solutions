1from typing import List
2
3class Solution:
4    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
5        covered = [0] * 51
6        for l, r in ranges:
7            for i in range(l, r + 1):
8                covered[i] = 1
9        return all(covered[i] for i in range(left, right + 1))