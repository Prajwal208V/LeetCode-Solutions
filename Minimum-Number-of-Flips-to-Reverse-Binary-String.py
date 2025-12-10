1class Solution:
2    def minimumFlips(self, n: int) -> int:
3        s = bin(n)[2:]
4        i, j = 0, len(s) - 1
5        ans = 0
6        while i < j:
7            if s[i] != s[j]:
8                ans += 2
9            i += 1
10            j -= 1
11        return ans
12