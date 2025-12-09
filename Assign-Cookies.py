1from typing import List
2
3class Solution:
4    def findContentChildren(self, g: List[int], s: List[int]) -> int:
5        g.sort()
6        s.sort()
7        i = j = 0
8        
9        while i < len(g) and j < len(s):
10            if s[j] >= g[i]:
11                i += 1
12            j += 1
13        
14        return i
15