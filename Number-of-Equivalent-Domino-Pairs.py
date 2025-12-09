1from typing import List
2from collections import Counter
3
4class Solution:
5    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
6        counts = Counter()
7        for a, b in dominoes:
8            if a > b:
9                a, b = b, a
10            counts[(a, b)] += 1
11        res = 0
12        for c in counts.values():
13            res += c * (c - 1) // 2
14        return res