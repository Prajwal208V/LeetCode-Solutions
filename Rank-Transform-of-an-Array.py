1from typing import List
2
3class Solution:
4    def arrayRankTransform(self, arr: List[int]) -> List[int]:
5        sorted_unique = sorted(set(arr))
6        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
7        return [rank[x] for x in arr]
8