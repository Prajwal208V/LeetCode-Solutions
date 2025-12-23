1class Solution:
2    def captureForts(self, forts: list[int]) -> int:
3        prev = -1
4        res = 0
5        for i, v in enumerate(forts):
6            if v != 0:
7                if prev != -1 and forts[prev] != v:
8                    res = max(res, i - prev - 1)
9                prev = i
10        return res