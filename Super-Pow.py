1class Solution:
2    def superPow(self, a: int, b: list[int]) -> int:
3        MOD = 1337
4
5        def modPow(x: int, n: int) -> int:
6            res = 1
7            x %= MOD
8            while n > 0:
9                if n & 1:
10                    res = res * x % MOD
11                x = x * x % MOD
12                n >>= 1
13            return res
14
15        res = 1
16        for digit in b:
17            res = modPow(res, 10) * modPow(a, digit) % MOD
18        return res