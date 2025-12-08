1class Solution:
2    def largeGroupPositions(self, s: str) -> list[list[int]]:
3        n = len(s)
4        res = []
5        i = 0
6        while i < n:
7            j = i
8            while j < n and s[j] == s[i]:
9                j += 1
10            if j - i >= 3:
11                res.append([i, j - 1])
12            i = j
13        return res
14