1class Solution:
2    def binaryGap(self, n: int) -> int:
3        last = -1
4        ans = 0
5        i = 0
6        while n:
7            if n & 1:
8                if last != -1:
9                    ans = max(ans, i - last)
10                last = i
11            n >>= 1
12            i += 1
13        return ans