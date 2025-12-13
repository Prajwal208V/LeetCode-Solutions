1class Solution:
2    def lastRemaining(self, n: int) -> int:
3        head = 1
4        step = 1
5        remaining = n
6        left = True
7
8        while remaining > 1:
9            if left or remaining % 2 == 1:
10                head += step
11            remaining //= 2
12            step *= 2
13            left = not left
14
15        return head