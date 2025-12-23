1class Solution:
2    def similarPairs(self, words: list[str]) -> int:
3        seen = {}
4        res = 0
5        for w in words:
6            key = tuple(sorted(set(w)))
7            res += seen.get(key, 0)
8            seen[key] = seen.get(key, 0) + 1
9        return res