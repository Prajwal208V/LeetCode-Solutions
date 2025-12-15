1class Solution:
2    def countGoodSubstrings(self, s: str) -> int:
3        return sum(1 for i in range(len(s) - 2) if len(set(s[i:i+3])) == 3)