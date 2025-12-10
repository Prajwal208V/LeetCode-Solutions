1class Solution:
2    def removePalindromeSub(self, s: str) -> int:
3        if not s:
4            return 0
5        if s == s[::-1]:
6            return 1
7        return 2
8