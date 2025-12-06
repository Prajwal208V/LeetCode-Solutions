1class Solution:
2    def isScramble(self, s1: str, s2: str) -> bool:
3        from functools import lru_cache
4        
5        @lru_cache(None)
6        def dfs(a, b):
7            if a == b:
8                return True
9            if sorted(a) != sorted(b):
10                return False
11            n = len(a)
12            for i in range(1, n):
13                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
14                    return True
15                if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):
16                    return True
17            return False
18
19        return dfs(s1, s2)
20