1class Solution:
2    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
3        words = set(wordDict)
4        n = len(s)
5        from functools import lru_cache
6
7        @lru_cache(None)
8        def dfs(i):
9            if i == n:
10                return [""]
11            res = []
12            for j in range(i+1, n+1):
13                w = s[i:j]
14                if w in words:
15                    for tail in dfs(j):
16                        res.append(w + ("" if tail == "" else " " + tail))
17            return res
18
19        return dfs(0)