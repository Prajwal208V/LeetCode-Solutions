1class Solution:
2    def sumAndMultiply(self, n: int) -> int:
3        s = str(n)
4        digits = [c for c in s if c != '0']
5        if not digits:
6            return 0
7        x = int(''.join(digits))
8        total = sum(int(c) for c in digits)
9        return x * total
10