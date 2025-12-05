1class Solution:
2    def countPrimes(self, n: int) -> int:
3        if n < 3:
4            return 0
5        sieve = [True] * n
6        sieve[0] = sieve[1] = False
7        p = 2
8        while p * p < n:
9            if sieve[p]:
10                for i in range(p*p, n, p):
11                    sieve[i] = False
12            p += 1
13        return sum(sieve)
14