1from typing import List
2
3class Solution:
4    def isPrefixString(self, s: str, words: List[str]) -> bool:
5        cur = ""
6        for w in words:
7            cur += w
8            if cur == s:
9                return True
10            if len(cur) > len(s):
11                return False
12        return False