1from collections import Counter
2
3class Solution:
4    def maxNumberOfBalloons(self, text: str) -> int:
5        need = Counter("balloon")
6        have = Counter(text)
7        res = float('inf')
8        for ch in need:
9            res = min(res, have[ch] // need[ch])
10        return res if res != float('inf') else 0
11