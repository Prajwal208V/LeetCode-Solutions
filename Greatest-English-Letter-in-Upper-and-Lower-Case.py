1class Solution:
2    def greatestLetter(self, s: str) -> str:
3        seen = set(s)
4        for c in range(ord('Z'), ord('A') - 1, -1):
5            ch = chr(c)
6            if ch in seen and ch.lower() in seen:
7                return ch
8        return ""