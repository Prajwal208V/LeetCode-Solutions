1class Solution:
2    def integerReplacement(self, n: int) -> int:
3        steps = 0
4        while n != 1:
5            if n % 2 == 0:
6                n //= 2
7            else:
8                if n == 3 or n & 2 == 0:
9                    n -= 1
10                else:
11                    n += 1
12            steps += 1
13        return steps