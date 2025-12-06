1class Solution:
2    def largestPalindrome(self, n: int) -> int:
3        if n == 1:
4            return 9
5        upper = 10**n - 1
6        lower = 10**(n-1)
7        for left in range(upper, lower-1, -1):
8            s = str(left)
9            pal = int(s + s[::-1])
10            for x in range(upper, lower-1, -1):
11                if x * x < pal:
12                    break
13                if pal % x == 0:
14                    return pal % 1337
15        return 0
16