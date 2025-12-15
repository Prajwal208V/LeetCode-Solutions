1class Solution:
2    def longestNiceSubstring(self, s: str) -> str:
3        def helper(sub):
4            st = set(sub)
5            for i, c in enumerate(sub):
6                if c.lower() not in st or c.upper() not in st:
7                    left = helper(sub[:i])
8                    right = helper(sub[i+1:])
9                    return left if len(left) >= len(right) else right
10            return sub
11        
12        return helper(s)